@echo off
setlocal enabledelayedexpansion

:: Check if a codelab name was provided
if "%~1"=="" (
    echo USAGE: %0 ^<CODELAB_NAME^>
    echo.
    exit /b 1
)

:: Get current directory
set "SCRIPT_DIR=%~dp0"

:: Codelab name from first argument
set "CODELAB_NAME=%~1"

:: Get Git username (requires Git for Windows to be installed)
for /f "delims=" %%a in ('git config user.name') do set "AUTHOR_NAME=%%a"

:: Define file paths
set "MARKDOWN_TEMPLATE=%SCRIPT_DIR%markdown\template\markdown.template"
set "PACKAGE_JSON_TEMPLATE=%SCRIPT_DIR%markdown\template\package.json"
set "CODELAB_MARKDOWN_FILE=%SCRIPT_DIR%markdown\%CODELAB_NAME%\%CODELAB_NAME%.md"
set "CODELAB_PACKAGE_JSON=%SCRIPT_DIR%markdown\%CODELAB_NAME%\package.json"

:: Validate template files exist
if not exist "%MARKDOWN_TEMPLATE%" (
    echo ERROR: Markdown template not found
    exit /b 1
)
if not exist "%PACKAGE_JSON_TEMPLATE%" (
    echo ERROR: Package.json template not found
    exit /b 1
)

:: Create directory for codelab
mkdir "%SCRIPT_DIR%markdown\%CODELAB_NAME%"
xcopy /E /I "%SCRIPT_DIR%markdown\template\*" "%SCRIPT_DIR%markdown\%CODELAB_NAME%"
del "%SCRIPT_DIR%markdown\%CODELAB_NAME%\markdown-iguide.template"

:: Rename markdown template
move "%SCRIPT_DIR%markdown\%CODELAB_NAME%\markdown.template" "%CODELAB_MARKDOWN_FILE%"

:: Replace placeholders in markdown file
powershell -Command "(Get-Content '%CODELAB_MARKDOWN_FILE%') | ForEach-Object { $_ -replace 'CODELAB_NAME.*', '%CODELAB_NAME%' -replace 'AUTHOR_NAME.*', '%AUTHOR_NAME%' } | Set-Content '%CODELAB_MARKDOWN_FILE%'"

:: Replace placeholders in package.json
powershell -Command "(Get-Content '%CODELAB_PACKAGE_JSON%') | ForEach-Object { $_ -replace 'CODELAB_NAME', '%CODELAB_NAME%' } | Set-Content '%CODELAB_PACKAGE_JSON%'"

:: Use PowerShell to update the "watch" script in package.json
powershell -Command `
    "$packageJsonPath = '%CODELAB_PACKAGE_JSON%'; `
    $content = Get-Content -Path $packageJsonPath -Raw; `
    $updatedContent = $content -replace '\"watch\":\s*\"nodemon --watch CODELAB_NAME\\.md --exec \\\""claat export -o temp/ CODELAB_NAME\\.md && ./node_modules/kill-port/cli\\.js --port 9090 && cd temp/CODELAB_NAME && claat serve\\\""', `
    '\"watch\": \"nodemon --watch CODELAB_NAME.md --exec \\\""npx claat export -o temp/ CODELAB_NAME.md; npx kill-port --port 9090; cd temp\\\\CODELAB_NAME; npx claat serve\\\""'; `
    $updatedContent | Set-Content -Path $packageJsonPath"
    
echo Markdown file created! Find it at %CD%\markdown\%CODELAB_NAME%

:: Check for required commands
where claat >nul 2>nul
if errorlevel 1 echo Note: claat does not exist. Please install it if you would like to run the codelab locally.

where go >nul 2>nul
if errorlevel 1 echo Note: go does not exist. Please install it if you would like to run the codelab locally.

:: Change to the codelab directory
cd "%SCRIPT_DIR%markdown\%CODELAB_NAME%"