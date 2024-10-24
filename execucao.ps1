# Caminho para o aplicativo
$appPath = "C:\Users\rafae\OneDrive\Desktop\cardioEmotion.appref-ms"

# Caminho para o script AutoHotkey
$ahkScriptPath = "C:\Users\rafae\OneDrive\Documentos\AutoHotkey\fabrica_de_projetos.ahk"

# Executa o aplicativo
Start-Process -FilePath $appPath

# Aguarda 5 segundos para o aplicativo carregar (ajuste se necessário)
Start-Sleep -Seconds 20

# Executa o script AutoHotkey
Start-Process -FilePath $ahkScriptPath
