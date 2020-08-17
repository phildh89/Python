#Given a military time return the angle between the minute and hour hand


def ClockAngle():
    inputTime = int(input("Enter a 4 digit military time: "))

    hour = int(inputTime / 100)
    print(hour)
    min = int(inputTime % 100)
    print(min)

    if(hour < 0 or hour > 24 or min < 0 or min > 60):
        print("invalid input")
    else:
        hourAngle = 30 * hour
        minAngle = 6 * min
        angle = abs(minAngle - hourAngle)
        print("The angle for the time " , inputTime , " = " , angle)




ClockAngle()