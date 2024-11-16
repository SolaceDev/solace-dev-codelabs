# init.ps1
# Automate these steps to get yourself up and running with Codelab in Windows
# * Create boilerplate for Codelab
# * Configure a nodemon watch command to rebuild your codelab on save

# Function to check if a command exists
function command_exists {
    param ($cmd)
    if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
        Write-Host "Note: $cmd does not exist. Please install it if you would like to run the codelab locally."
    }
}

# Validate that a codelab name was included as an argument
if ($args.Count -ne 1) {
    Write-Host "USAGE: .\init.ps1 <CODELAB_NAME>"
    exit 1
}

# Variables
$CODELAB_NAME = $args[0]
$AUTHOR_NAME = git config user.name

$codelab_markdown_filename = "markdown\$CODELAB_NAME\$CODELAB_NAME.md"
$codelab_package_json_filename = "markdown\$CODELAB_NAME\package.json"
$markdown_template = "markdown\template\markdown.template"
$package_json_template = "markdown\template\package.json"

# Validate that markdown template and package.json exist
if (-not (Test-Path $markdown_template) -or -not (Test-Path $package_json_template)) {
    Write-Host "ERROR: Could not find one of the following files:"
    Write-Host "  - $markdown_template"
    Write-Host "  - $package_json_template"
    exit 1
}

# Create a new directory for the codelab
New-Item -ItemType Directory -Force -Path "markdown\$CODELAB_NAME"
Copy-Item -Recurse -Force -Path "markdown\template\*" -Destination "markdown\$CODELAB_NAME"
Remove-Item -Force "markdown\$CODELAB_NAME\markdown-iguide.template"

# Rename markdown template file
Rename-Item -Path "markdown\$CODELAB_NAME\markdown.template" -NewName "$CODELAB_NAME.md"

# Replace placeholder codelab id in markdown template file with name provided by command line argument
(Get-Content $codelab_markdown_filename) -replace "CODELAB_NAME.*", $CODELAB_NAME | Set-Content $codelab_markdown_filename

# Replace placeholder author name with Git username
(Get-Content $codelab_markdown_filename) -replace "AUTHOR_NAME.*", $AUTHOR_NAME | Set-Content $codelab_markdown_filename

# Replace placeholder codelab name in the watch command with name provided in command line argument
(Get-Content $codelab_package_json_filename) -replace "CODELAB_NAME", $CODELAB_NAME | Set-Content $codelab_package_json_filename

Write-Host "Markdown file created! Find it at $PWD\markdown\$CODELAB_NAME"

# Check if claat or go commands are available
command_exists claat
command_exists go

# Change to the new directory
Set-Location -Path "$PWD\markdown\$CODELAB_NAME"
