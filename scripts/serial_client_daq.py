#!/usr/bin/env python3

import serial
import nidaqmx
import time
import matplotlib.pyplot as plt

PORT = 'COM?'       # The com port to receive data
BAUD = 115200       # Baud rate used by the com port
TIMEOUT_S = 1

DEVICE = "Dev1/ai0" # DAQ device and channel

dataList = []

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan(DEVICE)
    print(task.read())
    for i in range(100):
        data = task.read()
        print(data)
        dataList.append(data)
        time.sleep(0.01)


figureWidth=5.5
figureHeight=3

plt.figure(figsize=(figureWidth, figureHeight))

panelWidth = 4.5
panelHeight = 2

panel = plt.axes([0.1,0.2,panelWidth/figureWidth,panelHeight/figureHeight])
panel.plot(dataList)

plt.show()

# Open the connection
# with serial.Serial(PORT, BAUD, timeout=TIMEOUT_S) as com:
    
#     # Keep receiving data until FicTrac closes
#     while com.is_open:
#         # Receive one data frame
#         data = com.readline()
#         if (not data):
#             break
            
#         line = data.decode('UTF-8')
        
#         # Tokenise
#         toks = line.split(", ")
        
#         # Fixme: sometimes we read more than one line at a time,
#         # should handle that rather than just dropping extra data...
#         if ((len(toks) < 24) | (toks[0] != "FT")):
#             print('Bad read')
#             continue
        
#         # Extract FicTrac variables
#         # (see https://github.com/rjdmoore/fictrac/blob/master/doc/data_header.txt for descriptions)
#         cnt = int(toks[1])
#         dr_cam = [float(toks[2]), float(toks[3]), float(toks[4])]
#         err = float(toks[5])
#         dr_lab = [float(toks[6]), float(toks[7]), float(toks[8])]
#         r_cam = [float(toks[9]), float(toks[10]), float(toks[11])]
#         r_lab = [float(toks[12]), float(toks[13]), float(toks[14])]
#         posx = float(toks[15])
#         posy = float(toks[16])
#         heading = float(toks[17])
#         step_dir = float(toks[18])
#         step_mag = float(toks[19])
#         intx = float(toks[20])
#         inty = float(toks[21])
#         ts = float(toks[22])
#         seq = int(toks[23])
        
#         # Do something ...
#         print(cnt)
