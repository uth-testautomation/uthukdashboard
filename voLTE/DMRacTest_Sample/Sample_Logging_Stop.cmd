@echo off
setlocal
set "batch_dir=%~dp0"

echo [IP Address] 127.0.0.1 > "[Logging Stop] Result.txt"
%batch_dir%DMRacTest.exe 127.0.0.1 -le >> "[Logging Stop] Result.txt"
echo.>> "[Logging Stop] Result.txt"

endlocal
