$ErrorActionPreference = "Stop"

python -m pip install -r requirements.txt
python -m pip install pyinstaller

python -m PyInstaller `
  --noconfirm `
  --clean `
  --onefile `
  --windowed `
  --name UniGraph `
  --collect-all matplotlib `
  --collect-all pandas `
  --collect-all numpy `
  --collect-all openpyxl `
  app.py

New-Item -ItemType Directory -Force -Path "web\downloads" | Out-Null
Copy-Item -Force "dist\UniGraph.exe" "web\downloads\UniGraph.exe"

Write-Host "Build complete: dist\\UniGraph.exe"
Write-Host "Website download copy: web\\downloads\\UniGraph.exe"
