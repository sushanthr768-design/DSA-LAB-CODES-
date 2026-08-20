def search(arr,target,s):

    if (arr[s]==target):
        return s
    if(s==0 and arr[s]!=target):
        return -1

    return search(arr,target,s-1)

arr = [3,45,233,5,6,89,32,4,23,32]
print(search(arr,10,len(arr)-1))
