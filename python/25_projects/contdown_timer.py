import time
            
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end = "\r")
        time.sleep(1)
        t -= 1
    print("Time's up!")

def main():
    while True:
        t = input("How many seconds you want to count down from? ")
        countdown(int(t))

main()