$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPython = Join-Path $scriptDir ".venv/Scripts/python.exe"
$gameScript = Join-Path $scriptDir "src/alien_invasion.py"

if (-not (Test-Path $venvPython)) {
    Write-Error "Ambiente virtual não encontrado em $venvPython"
    exit 1
}

& $venvPython $gameScript
