import time

def countdown(seconds):
    while seconds:
        min,sec=divmod(seconds,60)
        time_="%2d min %05.2f sec" % (min,sec)
        print(time_, end="\r")
        time.sleep(1)
        seconds-=1
    print("00 min 00.00 sec")

# print("\r") moves the cursor to the start of the current line and then starts a new line. (backspace)

seconds=int(input("Enter a time in seconds:- "))
countdown(seconds)