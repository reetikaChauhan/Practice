steps = int(input().strip())
path = input()


def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    count = 0
    countd = 0
    for i in path: 
        if i =='U':
            altitude = altitude + 1
        elif i == 'D':
            countd = countd+1
            altitude = altitude - 1
        if countd > 2 :
            if altitude==0 and i == 'U':
                count = count + 1
        print(count)
            
    print('valley',count)



countingValleys(steps,path)            

        




   