echo OFF

echo starting..
echo IN BETA 0.3.1
echo.
echo.

git status
git add .
git status
git commit -m "last known version 0.3.1"
git push

echo.
echo.

pip install -r requirements.txt 

echo.
echo.

python3 src\main.py %1

echo.
echo cleaning up...

dir /b > dir.txt

