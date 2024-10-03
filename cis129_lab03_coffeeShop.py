#CIS 129
#McCoy Hernandez
#This program will print a reciept

Muffins = int(input('Number of muffins bought: ')) #This requests how many muffins were bought and stores it in a variable called muffin
Coffee = int(input('Number of Coffees bought: ')) #This requests how many coffees were bought and stores it in a variable called cofee
muffinCost = 4*Muffins #this creates a variable that holds the cost of the total of muffins
coffeeCost = 5*Coffee #This does the same as the last line but for coffee
taxTotal = (muffinCost + coffeeCost) * 0.06 #This assigns a six percent tax to the muffin and coffee subtotal
total = muffinCost + coffeeCost + taxTotal #This adds all the totals
print('***************************************\nMy Coffee and Muffin Shop\nNumber of coffees bought?\n',
    Coffee,
    "\nNumber of muffins bought?\n",
    Muffins,
    "\n***************************************\n\n***************************************\nMy Coffee and Muffin Shop Receipt\n",
    Coffee, "Coffee at $5 each: ${:.2f}".format(coffeeCost), "\n",
    Muffins, "Muffins at $4 each: ${:.2f}".format(muffinCost), "\n",
    "6% tax: ${:.2f}".format(taxTotal),
    "\n---------\nTotal: $ {:.2f}".format(total),
    "\n***************************************")#This prints out the reciept and formats everything correctly