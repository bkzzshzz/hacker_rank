from tkinter import E


givenTime = "01:01:00PM"

print(givenTime[:2], givenTime[8:])

if givenTime[:2] == "12" and givenTime[8:] == "AM":
    print("00" + givenTime[2:-2])

elif givenTime[8:] == "AM":
    print(givenTime[:-2])

elif givenTime[:2] == "12" and givenTime[8:] == "PM":
    print(givenTime[:-2])

elif givenTime[8:] == "PM":
    print(str(int(givenTime[:2]) + 12) + givenTime[2:-2])