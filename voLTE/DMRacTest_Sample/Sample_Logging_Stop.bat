@echo off

echo [IP Address] 127.0.0.1 > "[Logging Stop] Result.txt"
DMRacTest.exe 127.0.0.1 -le >> "[Logging Stop] Result.txt"
echo.>> "[Logging Stop] Result.txt"

