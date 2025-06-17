# Write a program that schedules a function to print "Do coding..!" every 30 minutes.
import schedule
import time
import datetime

def display():
    print("Do Coding..!")

def main():

    print("Inside main function")

    schedule.every(30).minutes.do(display)

    print("In a waiting state")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()