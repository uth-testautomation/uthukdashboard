@echo off

echo [IP Address] 127.0.0.1 > "[Autocall Stop] Result.txt"
DMRacTest.exe 127.0.0.1 -ae >> "[Autocall Stop] Result.txt"
echo.>> "[Autocall Stop] Result.txt"

