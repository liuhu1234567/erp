import time
import datetime

def time_format(t):
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y/%m/%d')
    # timeStruct = time.strptime(t, "%Y-%m-%d")
    # strTime = time.strftime("%Y/%m/%d", timeStruct)
    return nowDate

if __name__ == '__main__':
    t = "2017-10-12"
    print(time_format(t))