#1 . first we need to sort the list 
lis = sorted([3,6,5,7,8,9,4,8,2])
#taking list from user 
#lis = sorted(list(map(int , input().split())))

low = 0 ; high = len(lis)-1
val = int(input('enter the element to search:'))

#2.applying binary search

def binary_search(lis , low , high , val):
    #high = 0 case , first element case
    if(high>=0):
        mid = (low+high)//2
        if(lis[mid] == val):
            print(val ,'found at index' , mid)
        elif(lis[mid] > val):
            binary_search(lis , low , mid-1 , val)
        else:
            binary_search(lis , mid+1 , high , val)
            
    else:
        print('element not found')
        
print(lis)
binary_search(lis , low , high , val)
    
