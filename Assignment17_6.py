# Write a script that schedules multiple tasks: one to print "Lunch time!" at 1 pm, and another to print "Wrap up work" at 6 pm

import schedule
import time
import datetime

def displayX():
    print("Lunch Time")

def displayY():
    print("Wrap up work")

def main():

    print("current time is : ",datetime.datetime.now())

    schedule.every().day.at("01:00").do(displayX)

    schedule.every().day.at("06:00").do(displayY)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()