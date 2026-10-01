#Ex1
r = float(input("Circle radius = "))
S = r**2 * 3.14
print("Circle area =", S)

#Ex2
a = float(input("Celsius: "))
b = a*1.8 +32
print(a, "(C) =", b, "(F)")

#Ex3
n = int(input("n = "))
if n <2:
    print(n, "is not a prime number")
else:
    prime = True
    for i in range(2,n):   
        if n % i == 0:
            prime = False
            break
    if prime:
            print(n, "is a prime number")
    else:
            print(n, "is not a prime number")

#Ex4
def is_perfect_number(n):
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n

n = int(input("n = "))
if is_perfect_number(n):
    print(n, "is a perfect number")
else:
    print(n, "is not a perfect number")

#Ex5
colors = ["red", "green", "blue", "yellow", "orange"]
user_color = input("Enter a color: ")
if user_color in colors:
     index = colors.index(user_color)
     print(f"Your color is at index {index} in my list")
else:
     print("Sorry, I could not find your color")

#Ex6
range1 = list(range(0,7))
print(range1)
range2 = list(range(1,11,3))
print(range2)
range3 = list(range(5,0,-1))
print(range3)
range4 = list(range(6,-3,-2))
print(range4)

#Ex7
def remove_dollar_sign(s):
    return s.replace("$", "")
s = input("Enter a string with a dollar sign: ")
print(remove_dollar_sign(s))

#ex8
def extract_even(I):
    return [n for n in I if n % 2 == 0]
I = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(extract_even(I))

#ex9
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))
print(f"The factorial of {n} is {factorial(n)}")

#ex10
def divisors(n):
    for i in range(1, n + 1): 
        if n % i == 0:
            print(i)

n = int(input("n = "))
divisors(n)

#ex11
xa = float(input("xa = "))
ya = float(input("ya = "))
xb = float(input("xb = "))
yb = float(input("yb = "))
distance = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
print("Distance between points A and B =", distance)

#ex12
def print_pattern(m, n):
    if m <= 0 or n <= 0:        
        return

    for i in range(m):
        if i == 0 or i == m - 1:
            print("*"* n)
        else:
            if n == 1:
                print("*")
            else:
                print("*" + " " *(n - 2) + "*")

m = int(input("number of rows: "))
n = int(input("number of columns: "))
print_pattern(m, n)