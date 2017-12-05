@echo off
start C:\xampped\xampp-control.exe
PING localhost -n 10 >NUL
echo Initializing Estrus Monitor...
python ipcam1.py
pause