# cleanup.ps1
# PowerShell script to clean up CFFI build artifacts

Write-Host "Cleaning up CFFI build artifacts..." -ForegroundColor Green

# Function to safely remove items
function Remove-SafelyIfExists {
    param([string]$Path, [string]$Description)
    
    if (Test-Path $Path) {
        try {
            Remove-Item $Path -Recurse -Force -ErrorAction Stop
            Write-Host "✓ Removed $Description" -ForegroundColor Yellow
            return $true
        }
        catch {
            Write-Host "✗ Failed to remove $Description : $_" -ForegroundColor Red
            return $false
        }
    }
    else {
        Write-Host "  $Description not found (already clean)" -ForegroundColor Gray
        return $true
    }
}

# Remove compiled extension files
$pydFiles = Get-ChildItem -Name "_example*.pyd" -ErrorAction SilentlyContinue
if ($pydFiles) {
    Remove-Item "_example*.pyd" -Force
    Write-Host "✓ Removed .pyd files" -ForegroundColor Yellow
}

# Remove generated C source
Remove-SafelyIfExists "_example.c" "generated C source"

# Remove build directory
Remove-SafelyIfExists "build" "build directory"

# Remove Release directory and all contents
Remove-SafelyIfExists "Release" "Release directory"

# Remove Visual Studio build artifacts
$buildArtifacts = @("*.exp", "*.lib", "*.obj", "*.pdb", "*.ilk")
foreach ($pattern in $buildArtifacts) {
    $files = Get-ChildItem -Name $pattern -ErrorAction SilentlyContinue
    if ($files) {
        Remove-Item $pattern -Force
        Write-Host "✓ Removed $pattern files" -ForegroundColor Yellow
    }
}

# Remove setuptools/distutils artifacts
Remove-SafelyIfExists "dist" "dist directory"

# Remove egg-info directories
Get-ChildItem -Directory -Name "*.egg-info" -ErrorAction SilentlyContinue | ForEach-Object {
    Remove-SafelyIfExists $_ "egg-info directory ($_)"
}

# Remove __pycache__ directories
Remove-SafelyIfExists "__pycache__" "__pycache__ directory"

# Remove .pyc files recursively
$pycFiles = Get-ChildItem -Recurse -Name "*.pyc" -ErrorAction SilentlyContinue
if ($pycFiles) {
    Get-ChildItem -Recurse -Name "*.pyc" | Remove-Item -Force
    Write-Host "✓ Removed .pyc files" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "✅ Cleanup complete!" -ForegroundColor Green

# Show remaining files for verification
Write-Host ""
Write-Host "📁 Remaining files in directory:" -ForegroundColor Cyan
Get-ChildItem -Name | Where-Object { 
    $_ -notlike "cleanup.*" -and 
    $_ -notlike "*.md" -and 
    $_ -notlike "*.py" 
} | ForEach-Object {
    Write-Host "  ⚠️  $_" -ForegroundColor Yellow
}

$remainingFiles = Get-ChildItem -Name | Where-Object { 
    $_ -notlike "cleanup.*" -and 
    $_ -notlike "*.md" -and 
    $_ -notlike "*.py" 
}

if ($remainingFiles.Count -eq 0) {
    Write-Host "  ✅ Only source files remain" -ForegroundColor Green
}
