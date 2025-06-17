# Schedule the task that displays the current date and time every minute using the datetime module.

import schedule
import datetime
import time

def display():
    print("The current time is : ",datetime.datetime.now())

def main():

    schedule.every(1).minutes.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()