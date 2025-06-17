# create a task that runs once everyday at 9:00 am and prints "Namaskar..."
import schedule
import time
import datetime

def display():
    print("current time is : ",datetime.datetime.now())
    print("Namaskar...")

def main():

    print("Inside main : ")

    print("current time is : ",datetime.datetime.now())
    
    schedule.every().day.at("09:00").do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()