; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{E1E512AB-4749-41CD-81A7-9DD5716C1FD0}
AppName=PlayWithRythm_2013180016
AppVersion=1.5
;AppVerName=PlayWithRythm_2013180016 1.5
AppPublisher=My Company, Inc.
AppPublisherURL=http://www.example.com/
AppSupportURL=http://www.example.com/
AppUpdatesURL=http://www.example.com/
DefaultDirName={pf}\PlayWithRythm_2013180016
DisableProgramGroupPage=yes
OutputDir=C:\Users\user\Desktop
OutputBaseFilename=PlayWithRythm_2013180016_Setup.exe
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\user\PycharmProjects\PlayWithRythm\dist\mygame.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\user\PycharmProjects\PlayWithRythm\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\PlayWithRythm_2013180016"; Filename: "{app}\mygame.exe"
Name: "{commondesktop}\PlayWithRythm_2013180016"; Filename: "{app}\mygame.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\mygame.exe"; Description: "{cm:LaunchProgram,PlayWithRythm_2013180016}"; Flags: nowait postinstall skipifsilent

