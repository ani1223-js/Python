def average(*num):
    sum = 0
    for i in num:
        sum = sum + i
    print("Avg is ", sum/len(num))

    
average(2,3,4,5,6)    