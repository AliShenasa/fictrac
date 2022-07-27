@echo off
rem Script to run fictrac
cd %~dp0
cd ..\TEsetup
call ..\bin\Release\fictrac.exe config.txt
pause