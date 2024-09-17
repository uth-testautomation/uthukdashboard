@echo off

echo [IP Address] 127.0.0.1 > "[Autocall Start] Result.txt"
DMRacTest.exe 127.0.0.1 -as Autocall_Sample >> "[Autocall Start] Result.txt"
echo.>> "[Autocall Start] Result.txt"

