#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")
print ("Available sizes")
print(" > Small")
print(" > Large")
print(" > Extra Large")

#Kaffe liste og størrelses liste med feil om ikke riktig kaffe fra menyen.
coffee_list = ["Espresso", "Americano", "Latte", "Cappuccino", "Macchiato", "Mocha", "Flat White"]
size_list = ["Small", "Large", "Extra Large"]

while True:
    coffee = input("What type of coffee would you like?").title()
    if coffee in coffee_list:
        break
    else:
        print("Sorry, we don't have that coffee. Please choose from the menu.")
#forskjellige priser for hvilke type kaffe som velges.
price = 0
if coffee=="Espresso":
   price = price + 2.50
elif coffee=="Americano":
   price = price + 3
elif coffee=="Latte":
   price = price + 2.50
elif coffee=="Cappuccino":
   price = price + 3
elif coffee=="Macchiato": 
   price = price + 3.50
elif coffee=="Mocha":
   price = price + 3.50
elif coffee=="Flat White":
   price = price + 3.50

#Hvilke størrelse kaffe og feil om ikke riktig størrelse og ekstra pris for typen kopp.
while True:
    size = input("What size would you like?").title()
    if size in size_list:
        break
    else:
        print("Sorry, we don't have that size. Please choose from the menu.")

if size == "Small":
    price = price + 0
elif size == "Large":
    price = price + 1
elif size == "Extra Large":
    price = price + 1.50
#om man vil spise inne eller ta med og ekstra pris for å spise inne.
while True:
    eat_in_or_takeaway = input("Would you like to eat in or take away?").title()
    if eat_in_or_takeaway == "Eat In":
        price = price + 0.50
        break
    elif eat_in_or_takeaway == "Take Away":
        price = price + 0
        break
    else:
        print("Sorry, that option is not available. Please choose Eat In or Take Away.")

print("----------------------------")
print("Total Cost: £" + str(price))