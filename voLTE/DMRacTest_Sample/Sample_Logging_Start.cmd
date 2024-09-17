@echo off
setlocal
set "batch_dir=%~dp0"

echo [IP Address] 127.0.0.1 > "[Logging Start] Result.txt"
%batch_dir%DMRacTest.exe 127.0.0.1 -ls Logging_Sample >> "[Logging Start] Result.txt"
echo.>> "[Logging Start] Result.txt"

endlocal


