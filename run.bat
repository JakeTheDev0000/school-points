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

pip install -r requirements.txt %1

echo.
echo.

python3 src\main.py 

echo.
echo cleaning up...

