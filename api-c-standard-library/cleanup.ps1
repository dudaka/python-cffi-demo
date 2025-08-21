# PowerShell cleanup script for CFFI build artifacts
# Run this to clean up after building the CFFI extension

Write-Host "Cleaning CFFI build artifacts..." -ForegroundColor Green

# Function to safely remove files/directories
function Remove-IfExists {
    param([string]$Path, [string]$Description)
    
    if (Test-Path $Path) {
        try {
            if ((Get-Item $Path) -is [System.IO.DirectoryInfo]) {
                Remove-Item $Path -Recurse -Force
            } else {
                Remove-Item $Path -Force
            }
            Write-Host "Deleted $Description" -ForegroundColor Yellow
        }
        catch {
            Write-Host "Failed to delete $Description`: $($_.Exception.Message)" -ForegroundColor Red
        }
    }
}

# Remove compiled extension modules
Remove-IfExists "_example.pyd" "_example.pyd"
Get-ChildItem "_example.cp*.pyd" -ErrorAction SilentlyContinue | ForEach-Object {
    Remove-IfExists $_.Name $_.Name
}

# Remove generated C source
Remove-IfExists "_example.c" "_example.c"

# Remove build directories
Remove-IfExists "build" "build directory"
Remove-IfExists "Release" "Release directory"

# Remove test files
$testFiles = @("test_file.txt", "demo.txt", "sample.txt", "small.txt", "medium.txt", "empty.txt")
foreach ($file in $testFiles) {
    Remove-IfExists $file $file
}

# Remove Python cache
Remove-IfExists "__pycache__" "__pycache__ directory"

# Remove .pyc files
Get-ChildItem "*.pyc" -ErrorAction SilentlyContinue | ForEach-Object {
    Remove-IfExists $_.Name $_.Name
}

# Remove egg-info directories
Get-ChildItem "*.egg-info" -Directory -ErrorAction SilentlyContinue | ForEach-Object {
    Remove-IfExists $_.Name "$($_.Name) directory"
}

# Remove dist directory if it exists
Remove-IfExists "dist" "dist directory"

Write-Host ""
Write-Host "Cleanup completed!" -ForegroundColor Green
Write-Host ""
Write-Host "Remaining files:" -ForegroundColor Cyan
Get-ChildItem -Name "*.py", "*.md", "*.bat", "*.ps1" | Sort-Object
