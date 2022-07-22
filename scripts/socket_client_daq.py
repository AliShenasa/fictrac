#!/usr/bin/env python3

import socket
import select
import nidaqmx
import time

HOST = '127.0.0.1'  # The (receiving) host IP address (sock_host)
PORT = 2000         # The (receiving) host port (sock_port)

DEVICE = "Dev1/ai0"

t = time.time()
exec_time = time.strftime('%Y%m%d_%H%M%S', time.localtime(t))
filename = "fictrac-daq-" + exec_time + ".dat"

# TCP
# Open the connection (ctrl-c / ctrl-break to quit)
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#    sock.connect((HOST, PORT))

# UDP
# Open the connection (ctrl-c / ctrl-break to quit)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock, nidaqmx.Task() as task, open(filename, 'w') as datfile:
    sock.bind((HOST, PORT))
    sock.setblocking(0)
    
    # initialize daq channel
    task.ai_channels.add_ai_voltage_chan(DEVICE)
    
    # Keep receiving data until FicTrac closes
    data = ""
    timeout_in_seconds = 1
    while True:
        # Check to see whether there is data waiting
        ready = select.select([sock], [], [], timeout_in_seconds)
    
        # Only try to receive data if there is data waiting
        if ready[0]:
            # Receive one data frame
            new_data = sock.recv(1024)
            
            # Uh oh?
            if not new_data:
                break
            
            # Decode received data
            data += new_data.decode('UTF-8')
            
            # Find the first frame of data
            endline = data.find("\n")
            line = data[:endline]       # copy first frame
            data = data[endline+1:]     # delete first frame
            
            # Tokenise
            toks = line.split(", ")
            
            # Check that we have sensible tokens
            if ((len(toks) < 24) | (toks[0] != "FT")):
                print('Bad read')
                continue
            
            # Extract FicTrac variables
            # (see https://github.com/rjdmoore/fictrac/blob/master/doc/data_header.txt for descriptions)
            cnt = toks[1]

            # Get voltage from DAQ
            volt = str(task.read())
 
            # Do something ...
            print(cnt)
            dataList = toks[1:25+1]
            dataList.append(volt)
            datfile.write(", ".join(dataList)+"\n")
        
        else:
            # Didn't find any data - try again
            print('retrying...')
