# Write a script that simulates chgecking for email updates every 10 seconds.(Use a print statement like "checking mail..." instead of real email logic)
import schedule
import time
import datetime
def display():
    print("Checking Email")

def main():

    schedule.every(10).seconds.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()