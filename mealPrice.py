def count_subtotal(childMealPrice, adultMealPrice, childrenCount, adultsCount):
 return childMealPrice * childrenCount + adultMealPrice * adultsCount

def count_sales_tax(subtotal, salesTaxPercentage): 
    return subtotal * salesTaxPercentage / 100

def count_total(subtotal, salesTax): 
    return subtotal + salesTax

def count_change(total, paymentAmount):
    return paymentAmount - total

def format(value):
    return str(round(value, 2))

childMealPrice = float(input("What is the price of a child's meal? "))
adultMealPrice = float(input("What is the price of an adult's meal? "))
childrenCount = int(input("How many children are there? "))
adultsCount = int(input("How many adults are there? "))
salesTaxPercentage = float(input("What is the sales tax rate? "))

subtotal = count_subtotal(childMealPrice, adultMealPrice, childrenCount, adultsCount)
salesTax = count_sales_tax(subtotal, salesTaxPercentage)
total = count_total(subtotal, salesTax)
 
print(f"\nSubtotal: ${format(subtotal)}")
print(f"Sales Tax: ${format(salesTax)}")
print(f"Total: ${format(total)}\n")

payment_amount = float(input("What is the payment amount? "))
change_amount = count_change(total, payment_amount)

if(change_amount < 0) :
    print("You don't have enough money.")
else :
    print(f"Change: ${format(change_amount)}")
