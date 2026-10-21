@echo off
if not exist "%~dp0index.html" (
  echo index.html not found. Extract the complete project folder first.
  pause
  exit /b 1
)
start "" "%~dp0index.html"
