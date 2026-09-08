#create function that return total Bytes of given GB, MB and KB. in this example MB and KB optional. 
def getbytes(GB,MB=0,KB=0):
    totalbytes = (GB * 1024**3) + (MB * 1024**2) + (KB * 1024)
    return totalbytes
        

GB = int(input('enter GB'))
MB = int(input('enter MB'))
KB = int(input('enter KB'))

result = getbytes(GB,MB,KB)
print('result into bytes using 3 argument',result)

result = getbytes(GB,MB)
print('result into bytes using 2 argument',result)

result = getbytes(GB)
print('result into bytes using 1 argument',result)


