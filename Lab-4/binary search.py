def binary_search(arr):
    low=0
    high=len(arr)-1
    key=int(input("enter a number to search:"))
    found=False

    while low <= high:

        mid= (low+high)//2
        if arr [mid] ==key:
            print(f"{key} is found at index:",mid)
            found=True
            break
        elif arr[mid] > key:
            high =mid-1

        elif arr[mid] < key:
                low=mid+1

    if found == False:
            print(f"{key} is not found")


l= int(input("enter a total number of elemants:"))
arr = []

for i in range (l):
    a=int(input(f"Enter {i+1}st elements:"))
    arr.append(a)
    arr.sort()


binary_search(arr)
