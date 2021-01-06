#This is regular recursion using fibonacci.
def fib(n):
    	if n<=0:
		return 1
	return fib(n-1)+fib(n-2)

#This is head recursion using fibonacci.
def head_fib(n,num1=0,num2=1):
    if n>0:
        return head_fib(n-1,num1=num2,num2=num1+num2)
    else:
        return num1+num2

#This is tail recursion using fibonacci.
def tail_fib(n,num1=0,num2=1):
    if n<=0:
        return num1+num2
    else:
        return tail_fib(n-1,num1=num2,num2=num1+num2)

num=100
#Checking.
print("head fib:")
print(head_fib(num))
print("\ntail fib:")
print(tail_fib(num))
print("\nfib function:")
print(fib(num))

