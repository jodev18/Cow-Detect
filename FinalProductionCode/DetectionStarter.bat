@echo off
:BEGINNING
start C:\xampped\xampp-control.exe
PING localhost -n 10 >NUL
echo Initializing Estrus Monitor...
python CowOverlapDetection.py

echo Press any key to restart the program.
pause
goto BEGINNING