import sys, time


try:
    while True:

        list = [1,2,3,4,5]

        for i in list:
            frontLine = ('%s%s'% (' '*int(i),'*********'))
            print(frontLine)
            time.sleep(0.25)    

        for y in reversed(list):
            backLine = ('%s%s'% (' '*int(y),'*********'))
            print(backLine)
            time.sleep(0.25)
except KeyboardInterrupt:
    sys.exit()
