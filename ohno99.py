import subprocess
sum = 0
while True:
    if sum == 0:
        subprocess.call(["say", "-v", "Sinji", "wo shi sha bi"])
    new_val = input("new value: ")
    if new_val == "reset" or new_val == "r":
        sum = 0
        continue
    elif new_val == "quit" or new_val == "q":
        quit()
    try:
        sum += int(new_val)
        print("Current sum: ", sum)
        if sum == 98:
            subprocess.call(["say", "-v", "Sinji", "爆炸"])
            continue
        subprocess.call(["say", "-v", "Sinji", f"\"{sum}\""])
    except:
        pass
