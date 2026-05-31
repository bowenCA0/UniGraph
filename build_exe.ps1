$ErrorActionPreference = "Stop"

python -m pip install -r requirements.txt
python -m pip install pyinstaller

New-Item -ItemType Directory -Force -Path "assets" | Out-Null
$splashPath = "assets\splash.png"
Add-Type -AssemblyName System.Drawing
$bitmap = New-Object System.Drawing.Bitmap 760, 420
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit
$bg = New-Object System.Drawing.Drawing2D.LinearGradientBrush(
  (New-Object System.Drawing.Rectangle 0, 0, 760, 420),
  [System.Drawing.Color]::FromArgb(31, 35, 42),
  [System.Drawing.Color]::FromArgb(25, 48, 64),
  25
)
$graphics.FillRectangle($bg, 0, 0, 760, 420)
$accent = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(47, 129, 247))
$white = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(245, 248, 252))
$muted = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(174, 184, 198))
$logoPath = New-Object System.Drawing.Drawing2D.GraphicsPath
$logoRadius = 18
$logoPath.AddArc(72, 74, $logoRadius, $logoRadius, 180, 90)
$logoPath.AddArc(72 + 78 - $logoRadius, 74, $logoRadius, $logoRadius, 270, 90)
$logoPath.AddArc(72 + 78 - $logoRadius, 74 + 78 - $logoRadius, $logoRadius, $logoRadius, 0, 90)
$logoPath.AddArc(72, 74 + 78 - $logoRadius, $logoRadius, $logoRadius, 90, 90)
$logoPath.CloseFigure()
$graphics.FillPath($accent, $logoPath)
$fontLogo = New-Object System.Drawing.Font "Segoe UI", 34, ([System.Drawing.FontStyle]::Bold)
$fontTitle = New-Object System.Drawing.Font "Segoe UI", 34, ([System.Drawing.FontStyle]::Bold)
$fontBody = New-Object System.Drawing.Font "Microsoft YaHei", 16, ([System.Drawing.FontStyle]::Regular)
$fontSmall = New-Object System.Drawing.Font "Segoe UI", 11, ([System.Drawing.FontStyle]::Regular)
$graphics.DrawString("U", $fontLogo, $white, 94, 88)
$graphics.DrawString("UniGraph", $fontTitle, $white, 178, 80)
$graphics.DrawString("Starting...  正在启动...  Chargement...", $fontBody, $muted, 182, 142)
$graphics.DrawString("Preparing the desktop plotting workspace", $fontSmall, $muted, 184, 186)
$pen = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(80, 255, 255, 255)), 2
$graphics.DrawLine($pen, 184, 244, 576, 244)
$progressPen = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(47, 129, 247)), 5
$graphics.DrawLine($progressPen, 184, 244, 374, 244)
$graphics.DrawString("Copyright bowen", $fontSmall, $muted, 184, 294)
$bitmap.Save($splashPath, [System.Drawing.Imaging.ImageFormat]::Png)
$graphics.Dispose()
$bitmap.Dispose()

python -m PyInstaller `
  --noconfirm `
  --clean `
  --onefile `
  --windowed `
  --splash $splashPath `
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
