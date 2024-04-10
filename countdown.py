import time
t=(int(input("how much long countdown you need:")))
   
def countdown(t):
      while t:
        print(t)
        time.sleep(1)
        t -= 1

if __name__ == "__main__":
    countdown(int(t))
    print("done")
