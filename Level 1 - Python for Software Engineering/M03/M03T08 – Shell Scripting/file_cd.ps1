# Create three new folders
"folder1", "folder2", "folder3" | ForEach-Object { New-Item -ItemType Directory -Name $_ }

# Navigate into folder1
Set-Location -Path ".\folder1"

# Create three new folders inside folder1
"subfolder1", "subfolder2", "subfolder3" | ForEach-Object { New-Item -ItemType Directory -Name $_ }

# Remove two subfolders
Remove-Item -Path ".\subfolder1", ".\subfolder2" -Recurse