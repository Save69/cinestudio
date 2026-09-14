@echo off
title Agente Studio - Server Locale & Google Calendar
cd /d "%~dp0"

echo ===================================================
echo             AVVIO AGENTE STUDIO
echo ===================================================
echo.
echo Avvio del server locale su porta 8080...
echo Il server locale e necessario per autorizzare il collegamento
echo sicuro OAuth 2.0 con Google Calendar.
echo.

start "" cmd /c "timeout /t 2 /nobreak >nul & start http://localhost:8080/AgenteStudio.html"

python -m http.server 8080

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Python non trovato o porta occupata, provo con Node.js npx http-server...
    npx -y http-server . -p 8080 -o /AgenteStudio.html
)

pause
