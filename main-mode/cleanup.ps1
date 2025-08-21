# PowerShell cleanup script for CFFI build artifacts

Write-Host "Cleaning up build output files and directories..." -ForegroundColor Green
Write-Host ""

# Define file patterns to delete
$filesToDelete = @(
    "*.obj",           # Object files
    "*.lib",           # Library files  
    "*.dll",           # Dynamic libraries
    "*.exp",           # Export files
    "*.ilk",           # Incremental linker files
    "*.pdb",           # Debug files
    "*.manifest",      # Manifest files
    "_pi_cffi.c",      # Generated CFFI C file
    "_pi_cffi.*.pyd",  # Python extension modules (versioned)
    "_pi_cffi.pyd"     # Python extension modules (unversioned)
)

# Define directories to delete
$dirsToDelete = @(
    "build",
    "Release",
    "__pycache__",
    "dist"             # Setuptools distribution directory
)

# Delete files
foreach ($pattern in $filesToDelete) {
    $files = Get-ChildItem -Name $pattern -ErrorAction SilentlyContinue
    if ($files) {
        Write-Host "Deleting files matching: $pattern" -ForegroundColor Yellow
        Remove-Item $pattern -Force
    }
}

# Delete directories
foreach ($dir in $dirsToDelete) {
    if (Test-Path $dir) {
        Write-Host "Deleting directory: $dir" -ForegroundColor Yellow
        Remove-Item $dir -Recurse -Force
    }
}

# Delete .egg-info directories (setuptools creates these)
$eggInfoDirs = Get-ChildItem -Directory -Name "*.egg-info" -ErrorAction SilentlyContinue
if ($eggInfoDirs) {
    foreach ($dir in $eggInfoDirs) {
        Write-Host "Deleting .egg-info directory: $dir" -ForegroundColor Yellow
        Remove-Item $dir -Recurse -Force
    }
}

Write-Host ""
Write-Host "Cleanup completed!" -ForegroundColor Green
Write-Host ""
Read-Host "Press Enter to continue..."
