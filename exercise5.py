# Get salary

current_payment=int(input("enter your current monthly payment :"))
percentage=int(input("Enter your percentage increase:"))

percentage2=float((percentage+100)/100)
new_payment=float(current_payment*percentage2)
print("your new sallary is:",new_payment)
