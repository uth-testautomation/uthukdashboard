@echo off

echo [IP Address] 127.0.0.1 > "[Logging Start] Result.txt"
DMRacTest.exe 127.0.0.1 -ls Logging_Sample >> "[Logging Start] Result.txt"
echo.>> "[Logging Start] Result.txt"

