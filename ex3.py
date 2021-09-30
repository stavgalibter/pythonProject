# Revers digits

num=int(input("enter 3 digits number:"))

n1=num%10

n2=num//10%10

n3=num//100

print(f"{n1}{n2}{n3}")