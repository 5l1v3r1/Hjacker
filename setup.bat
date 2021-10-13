@echo off
if exist setuped.hjacker (
    exit
) else (
    echo 0 >> setuped.hjacker
    pip install -r Impulse\requirements.txt
    pip install -r hjackerfiles\setuplist.txt
)
pause