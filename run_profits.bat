@echo off
cd /d C:\Users\ifean\TonysTechWorld\Assetvest
call venv\Scripts\activate
python manage.py process_profits >> C:\Users\ifean\TonysTechWorld\profit_log.txt 2>&1
