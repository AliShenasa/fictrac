@echo off
rem Script to run the daq client and fictrac in order to log all data from fictrac
rem Requires conda to be added to PATH
call conda.bat activate balltrack
cd %~dp0
cd ..\TEsetup
start python ..\scripts\socket_client_daq.py
call ..\bin\Release\fictrac.exe config.txt
pause