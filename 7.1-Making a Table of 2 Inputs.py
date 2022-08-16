#Make a Multiplication Table with 2 Times User Input

n=int(input("Enter the Table:"))
r=int(input("How much time do you want to display:"))
for i in range(1,r+1):
   print(format(n,"<2"),"*" ,format(i,"<2"),"=",n*i)
