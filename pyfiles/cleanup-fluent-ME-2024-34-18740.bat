echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v241\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\v241\fluent\ntbin\win64\tell.exe" ME-2024-34 64739 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\v241\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="ME-2024-34" (%KILL_CMD% 6092) 
if /i "%LOCALHOST%"=="ME-2024-34" (%KILL_CMD% 18740) 
if /i "%LOCALHOST%"=="ME-2024-34" (%KILL_CMD% 11804)
del "C:\Users\snair322\OneDrive - Georgia Institute of Technology\2 projects\ServerStacks\pyfiles\cleanup-fluent-ME-2024-34-18740.bat"
