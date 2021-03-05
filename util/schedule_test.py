import schedule
import time
import os

def job():
    os.system("python3 Runner.py")


#schedule.every(1).minutes.do(job)

schedule.every().day.at("08:30:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(10)
