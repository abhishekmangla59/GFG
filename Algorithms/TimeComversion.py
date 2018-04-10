def timeConversion(s):
    AMPM = s[8:]
    time = s[2:8]
    print(time)
    if(AMPM == "AM"):
        flag = 0
    else:
        flag = 1

    hour = int(s[:2])

    if(flag==0 and hour==12):
        hour = hour-12
        finaltime = str(0)+str(hour)+time
        return finaltime

    elif(flag==1 and hour==12):
        finaltime = str(hour)+time
        return finaltime
    elif(flag==1 and hour<12):
        hour = hour+12
        finaltime = str(hour)+time
        return finaltime
    elif(flag==0 and hour<12):
        finaltime = s[0:8]
        return finaltime





print(timeConversion("06:02:00AM"))