@echo off
rem Script to run fictrac
:: Connect to NAS if it is not available
if not exist z:\ (net use z: "\\TurnerEvans-NAS\Lab Storage" /user:ahshenas cupcake)
:: change directory to NAS
Z:
:: location to store data
cd "Z:\Live Fly Imaging data\fictrac"
:: call fictrac
call C:\Users\exx\Documents\GitHub\fictrac\bin\Release\fictrac.exe C:\Users\exx\Documents\GitHub\fictrac\fictracCalibrationFiles\config.txt
pause