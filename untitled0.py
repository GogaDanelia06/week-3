#Task1
print("Task_1")
def avg(num1,num2):
    print("avg: ",end="")
    return (num1+num2)/2
print(avg(15, 23))
print(avg(2, 15))
print(avg(88, 13))

#Task3
print("Task_3")
def cube(num):
    print("num cube: ",end="")
    return num**3
print(cube(9))
print(cube(2))
print(cube(15))

#Task4
print("Task_4")
def m(num1,num2):
    if num1>num2:
        print("min num: ",end="")
        return num1
    elif num2>num1:
        print("max num: ",end="")
        return num2
    else:
        print("num equal")
print(m(6, 6))
print(m(12, 3))
print(m(76, 22))

#Task5
print("Task_5")
def odd(num):
    if num%2==0:
        return False
    else:
        return True
print(odd(15))
print(odd(8))
print(odd(81))

#Task6
print("Task_6")
def factorial_count(n):
    factorial = 1
    if n==0:
        print("factorial: ",1)
    else:
        for i in range(1,n+1):
            factorial = factorial*i
        return factorial
number = int(input("enter integer num: "))
print("factorial: ",factorial_count(number))

#Task7
print("Task_7")
def factorial_recursive(n):
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)
number = int(input("enter integer num: "))
print("factorial: ",factorial_recursive(number))

#Task8
print("Task_8")
numbers = [15,2,24,41,91]
sum = 0
for i in numbers:
    sum+=i
print("number sum: ",sum)
maximum = max(numbers)
minimum = min(numbers)
avg = sum/len(numbers)
print("max: ",maximum)
print("min: ",minimum)
print("avg: ",avg)
numbers.append(102)
print("102 added to last: ",numbers)
numbers.insert(2,205)
print("205 added to third position : ",numbers)
numbers.pop(3)
print("delete from fourth position: ",numbers)
numbers.sort()
print("increasing: ",numbers)


#Task9
print("Task_9")
def com(l1,l2):
    l = list(set(l1).intersection(l2))
    if l:
        return True
    else:
        return False
list1 = [11,4,3,12,13,6]
list2 = [3, 8, 2, 9]
print(com(list1,list2))


#Task11
print("Task_11")
import numpy as n
first = n.array([1, 2, 3, 4])
second = n.array([2, 3, 4, 5])
third = n.add(first,second)
print(third)
import numpy as np
randnums1= np.random.randint(1,101,5)
randnums2= np.random.randint(1,101,5)
result=[]
for i in range(0,5):
  result.append(randnums1[i]+randnums2[i])
print(randnums1)
print(randnums2)
print("sum: ",result)

