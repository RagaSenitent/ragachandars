num=[]
el=int(input("Enter number of elements:"))
for i in range(1,el+1):
    b=int(input("Enter element:"))
    num.append(b)
num.sort()
print("Largest element is:",num[el-1])
