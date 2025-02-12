echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v241\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\v241\fluent\ntbin\win64\tell.exe" ME-2024-03 51852 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\v241\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="ME-2024-03" (%KILL_CMD% 8736) 
if /i "%LOCALHOST%"=="ME-2024-03" (%KILL_CMD% 8832) 
if /i "%LOCALHOST%"=="ME-2024-03" (%KILL_CMD% 12368)
del "C:\Users\snair322\OneDrive - Georgia Institute of Technology\Desktop\ServerStacks\cleanup-fluent-ME-2024-03-8832.bat"
