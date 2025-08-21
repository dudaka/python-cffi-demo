# cleanup.ps1
# PowerShell script to clean up CFFI build artifacts

Write-Host "Cleaning up CFFI build artifacts..." -ForegroundColor Green

# Remove compiled extension files
$pydFiles = Get-ChildItem -Name "_example*.pyd" -ErrorAction SilentlyContinue
if ($pydFiles) {
    Remove-Item "_example*.pyd" -Force
    Write-Host "Removed .pyd files" -ForegroundColor Yellow
}

# Remove generated C source
if (Test-Path "_example.c") {
    Remove-Item "_example.c" -Force
    Write-Host "Removed generated C source" -ForegroundColor Yellow
}

# Remove build directory
if (Test-Path "build" -PathType Container) {
    Remove-Item "build" -Recurse -Force
    Write-Host "Removed build directory" -ForegroundColor Yellow
}

# Remove __pycache__ directories
$pycacheDir = Get-ChildItem -Name "__pycache__" -Directory -ErrorAction SilentlyContinue
if ($pycacheDir) {
    Remove-Item "__pycache__" -Recurse -Force
    Write-Host "Removed __pycache__" -ForegroundColor Yellow
}

# Remove .pyc files recursively
$pycFiles = Get-ChildItem -Recurse -Name "*.pyc" -ErrorAction SilentlyContinue
if ($pycFiles) {
    Get-ChildItem -Recurse -Name "*.pyc" | Remove-Item -Force
    Write-Host "Removed .pyc files" -ForegroundColor Yellow
}

Write-Host "Cleanup complete!" -ForegroundColor Green
