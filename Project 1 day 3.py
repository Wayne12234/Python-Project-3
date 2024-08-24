print("Welcome to Domino's")
size= input("What size of pizza would you like to have? S,M or L?")
pepperoni = input("Do you want to add pepperoni? Y for yes N for no" )
cheese = input("Would you like to add cheese? Y for yes and N for no")
total_bill=0


if size=="S":
    bill=10
    p_price=2
    che_se=3
    total_bill=p_price+che_se+bill
    print(f"Your total is {total_bill}")

elif size=="M":
    bill=15
    p_price = 2
    che_se = 3
    total_bill =p_price+che_se+ bill
    print(f"Your total is ${total_bill}")

if size == "L":
    bill = 20
    p_price = 2
    che_se = 3
    total_bill = p_price + che_se + bill
    print(f"Your total is ${total_bill}")








