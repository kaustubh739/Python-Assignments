# schedule a job that runs every 5 minutes to write a current time to a file marvellous.txt
import os
import schedule
import datetime
import time
def display():
    current_time = datetime.datetime.now()

    fobj = open("marvellous.txt",'a')
    fobj.write (str (current_time)+ "\n")

    print(f"current time is : ",{current_time})

def main():
    
    print("statrting in 1 minutes")

    schedule.every(5).minutes.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()