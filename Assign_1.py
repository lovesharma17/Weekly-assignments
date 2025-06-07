# Lower triangular code

n = int(input("Enter your number :"))
for i in range(n , 0 , -1):
     print('*'*(n+1-i) )  


# Upper triangular code

n = int(input("Enter your number :"))
for i in range(0 , n+1):
     print(' '*(i),end='')
     print('*'*(n-i) )


# Pyramid pattern code
  
n = int(input("Enter your number :"))
for i in range(1,n+1):
    print(' '*(n-i),end='')
    print('*'*(2*i-1), end='')
    print('')