def linear_search(arr):
    key=int(input("enter a number to check:"))
    found =False
    for i in range (len(arr)):
        if arr[i] == key:
            print(f"{key} is found at index",i)
            found=True
            break
    if found == False:
            print(f"{key} is not found")



l=int(input(f"enter total numbers of elements:"))
arr=[]  

for i in range(l):
    a=int(input("enter  the  element:"))
    arr.append(a)
linear_search(arr)
