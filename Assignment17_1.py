# write a python scripts that print "Jay Ganesh..." every 2 seconds. Use the schedule.every(2).seconds.do(...)function.
import schedule
import time
import datetime

def ganesh():
    print("Jay Ganesh...")

def main():
    print("Inside main function : ",datetime.datetime.now())

    schedule.every(2).seconds.do(ganesh)

    print("In a waiting state")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()