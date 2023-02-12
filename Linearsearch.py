
#Linearsearch

"""
def search(A,N,X):
    for i in range(0,N):
        if A[i]==X:
            return i 
    return -1


if __name__=="__main__":
    A=[2,4,6,8,10]
    N=len(A)
    X=6

result=search(A,N,X) 
if result==-1:
    print("Element is not present at index")
else:
    print("Element is present at index",result)


"""

N=int(input("Enter numbers:"))
A=[]
for i in range(N):
    A.insert(i,int(input()))
X=int(input("Enter a number to search:"))
for i in range(N):
    if A[i]==X:
        index=i 
        break 
    else:
        index=-1
print("The number is at index:",index)