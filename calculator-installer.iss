; -- Inno Setup Script File --

[Setup]
AppName=Calculator
AppVersion=1.0
DefaultDirName={pf}\Calculator
DefaultGroupName=Calculator

[Files]
Source: "dist\calculator.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Calculator"; Filename: "{app}\calculator.exe"

[Tasks]
; Corrected line - GroupDescription removed
