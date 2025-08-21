# PowerShell cleanup script for out-of-line ABI example

Write-Host "Cleaning up generated files..." -ForegroundColor Yellow

# Function to safely remove files/directories
function Remove-SafelyIfExists {
    param([string]$Path, [string]$Description)
    
    if (Test-Path $Path) {
        try {
            Remove-Item $Path -Recurse -Force -ErrorAction Stop
            Write-Host "✓ Deleted $Description" -ForegroundColor Green
            return $true
        }
        catch {
            Write-Host "✗ Failed to delete $Description : $_" -ForegroundColor Red
            return $false
        }
    }
    else {
        Write-Host "  $Description not found (already clean)" -ForegroundColor Gray
        return $true
    }
}

# Remove generated FFI module
Remove-SafelyIfExists "_simple_example.py" "generated FFI module (_simple_example.py)"

# Remove Python cache directories
Remove-SafelyIfExists "__pycache__" "__pycache__ directory"

# Remove setuptools build directory
Remove-SafelyIfExists "build" "build directory"

# Remove distribution directory
Remove-SafelyIfExists "dist" "dist directory"

# Remove egg-info directories
Get-ChildItem -Directory -Name "*.egg-info" | ForEach-Object {
    Remove-SafelyIfExists $_ "egg-info directory ($_)"
}

# Remove compiled Python files
Get-ChildItem -File -Name "*.pyc" | ForEach-Object {
    Remove-SafelyIfExists $_ "compiled Python file ($_)"
}

# Remove any temporary setup files
Remove-SafelyIfExists "setup.cfg" "setup.cfg"

# Remove any build artifacts that might be left behind
$buildArtifacts = @("*.egg", "*.whl", ".coverage", ".pytest_cache", ".tox")
foreach ($pattern in $buildArtifacts) {
    Get-ChildItem -Name $pattern -ErrorAction SilentlyContinue | ForEach-Object {
        Remove-SafelyIfExists $_ "build artifact ($_)"
    }
}

Write-Host ""
Write-Host "Cleanup complete!" -ForegroundColor Green

# Optional: Show remaining files
Write-Host ""
Write-Host "Remaining files in directory:" -ForegroundColor Cyan
Get-ChildItem -Name | Where-Object { 
    $_ -notlike "cleanup.*" -and 
    $_ -notlike "*.md" -and 
    $_ -notlike "*.py" -and 
    $_ -notlike "*.toml" -and 
    $_ -notlike "MANIFEST.in"
} | ForEach-Object {
    Write-Host "  $_" -ForegroundColor Yellow
}

if ((Get-ChildItem -Name | Where-Object { 
    $_ -notlike "cleanup.*" -and 
    $_ -notlike "*.md" -and 
    $_ -notlike "*.py" -and 
    $_ -notlike "*.toml" -and 
    $_ -notlike "MANIFEST.in"
}).Count -eq 0) {
    Write-Host "  (All generated files cleaned up)" -ForegroundColor Green
}
