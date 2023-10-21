@echo off

echo MEMORY ALLOCATION 1.0

:loop
echo 0: exit
echo 1: FIFO
echo 2: LRU
echo 3: MRU
echo 4: LFU
echo 5: MFU
echo 6: 2nd Chance
set /P var=Choose type of memory allocation: 
cls
if %var%==1 (goto fifo)
if %var%==2 (goto lru)
if %var%==3 (goto mru)
if %var%==4 (goto lfu)
if %var%==5 (goto mfu)
if %var%==6 (goto 2nd)
goto end

:fifo
echo FIFO
python FIFO.py
goto loop

:lru
echo LRU
python LRU.py
goto loop

:mru
echo MRU
python MRU.py
goto loop

:lfu
echo LFU
python LFU.py
goto loop

:mfu
echo MFU
python MFU.py
goto loop

:sec
echo Second Chance
python Sec.py
goto loop

:end
echo Goodbye
pause
