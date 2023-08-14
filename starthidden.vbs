Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "startturn.bat" & Chr(34), 0
Set WshShell = Nothing