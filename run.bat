echo OFF

echo starting..
echo IN BETA 0.3.1
echo.
echo.

dir /b > filelist.txt


@REM get the "versionDev.txt" file and get the version number witch is in the first line
set ver = %~f0
set ver = %ver:~0,1
set ver = ver + 1

echo version: %ver%


git status
git add .
git status
git commit -m "last known version 0.3.1-d0001"
git push

echo.
echo.

pip install -r requirements.txt 

echo.
echo.

python3 src\main.py %1

echo.
echo cleaning up...



