[Setup]
AppName=Instalador Completo
AppVersion=1.0
DefaultDirName={pf}\Instalador_Fabrica
DefaultGroupName=Instalador_Fabrica
OutputDir=C:\Users\rafae\OneDrive\Desktop\instalador\tentativa2
OutputBaseFilename=Instalador_Fabrica
Compression=lzma
SolidCompression=yes
DiskSpanning=yes


[Files]
; Python installer
Source: "C:\Users\rafae\OneDrive\Desktop\Dependencias\python-3.13.0-amd64.exe"; DestDir: "{tmp}"; Flags: ignoreversion
; Tesseract installer
Source: "C:\Users\rafae\OneDrive\Desktop\Dependencias\tesseract-ocr-setup-3.02.02.exe"; DestDir: "{tmp}"; Flags: ignoreversion
; Arquivos descomprimidos do software CardioEmotion
Source: "C:\Users\rafae\OneDrive\Desktop\Dependencias\instaladorCardioEmotion\*"; DestDir: "{tmp}\instaladorCardioEmotion"; Flags: ignoreversion recursesubdirs createallsubdirs
; Pasta leitura com scripts Python
Source: "C:\Users\rafae\OneDrive\Desktop\Dependencias\leitura\*"; DestDir: "{app}\leitura"; Flags: ignoreversion recursesubdirs createallsubdirs

[Run]
; Instalar Python de forma silenciosa
Filename: "{tmp}\python-3.13.0-amd64.exe"; Parameters: "/quiet InstallAllUsers=1 PrependPath=1"; Flags: waituntilterminated

; Executar o setup.exe da pasta descomprimida do CardioEmotion
Filename: "{tmp}\instaladorCardioEmotion\setup.exe"; Flags: waituntilterminated

; Instalar Tesseract normalmente
Filename: "{tmp}\tesseract-ocr-setup-3.02.02.exe"; Flags: waituntilterminated

; Instalar dependências do requirements.txt utilizando o PIP
Filename: "{cmd}"; Parameters: "/C {tmp}\python-3.13.0-amd64.exe -m pip install -r ""{app}\requirements.txt"""; Flags: runhidden waituntilterminated

[Icons]
; Atalho para o aplicativo principal
Name: "{group}\Instalador_Fabrica"; Filename: "{app}\Instalador_Fabrica.exe"
; Atalho para a pasta "leitura" com os scripts
Name: "{group}\Leitura"; Filename: "{app}\leitura"

[UninstallDelete]
; Remover a pasta leitura no desinstalador
Type: filesandordirs; Name: "{app}\leitura"
