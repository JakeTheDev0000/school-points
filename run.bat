echo OFF

echo starting..
echo IN BETA 0.3.1
echo.
echo.

dir /b > filelist.txt


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
echo pushing to github
echo.
git status
git add .
git status
git commit -m "last known version 0.3.1-%newVer%"
git push
echo.
echo.
echo done, newest version uploaded to github at version 0.3.1-%newVer%

echo.
echo cleaning up...



