echo OFF

echo starting..
echo IN BETA 0.4.0
echo.
echo.

dir /d > filelist.txt


for /f "Delims=" %%a in (versionDev.txt) do (
set ver=%%a
)

echo version: %ver%

set /a newVer=%ver% + 1

echo %newVer% > versionDev.txt



echo.
echo.

pip install -r requirements.txt 

echo.
echo.

python3 src\main.py %1

echo.
echo.
echo ==============================
echo = pushing to github          =
echo ==============================
echo.
git status
git add .
git status
git commit -m "last known version 0.4.0-%newVer%"
git push
echo.
echo.
echo =====================================================================
echo = done, newest version uploaded to github at version 0.4.0-%newVer% =
echo =====================================================================

echo.
echo cleaning up...



