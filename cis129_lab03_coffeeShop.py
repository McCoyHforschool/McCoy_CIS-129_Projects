#CIS 129
#McCoy Hernandez
#This program will print a reciept

Muffins = int(input('Number of muffins bought: ')) #This requests how many muffins were bought and stores it in a variable called muffin
Donuts = int(input('Number of Donuts bought: ')) #this requests how many donuts were bought
Markers = int(input('Number of Markers bought: ')) #This requests how many markers were bought
Coffee = int(input('Number of Coffees bought: ')) #This requests how many coffees were bought and stores it in a variable called cofee
muffinCost = 4*Muffins #this creates a variable that holds the cost of the total of muffins
donutCost = 5*Donuts
markerCost = 8*Markers #This and the previous line create a cost variable for Donuts and markers
coffeeCost = 5*Coffee #This does the same as the last line but for coffee
taxTotal = (muffinCost + coffeeCost + markerCost + donutCost) * 0.06 #This assigns a six percent tax to the subtotal
total = muffinCost + coffeeCost + dontCost + markerCost + taxTotal #This adds all the totals
print('***************************************\nMy Coffee and Muffin Shop\nNumber of Coffees bought?\n',
    Coffee,
    "\nNumber of Muffins bought?\n",
    Muffins,
    "\nNumber of Donuts bought?\n",
    Donuts,
    "\nNumber of Markers bought?\n",
    Markers,
    "\n***************************************\n\n***************************************\nMy Coffee and Muffin Shop Receipt\n",
    Coffee, "Coffee at $5 each: ${:.2f}".format(coffeeCost), "\n",
    Muffins, "Muffins at $4 each: ${:.2f}".format(muffinCost), "\n",
    Donuts, "Donuts at $5 each: ${:.2f}".format(donutCost), "\n",
    Markers, "Markers at $8 each: ${:.2f}".format(markerCost), "\n",
    "6% tax: ${:.2f}".format(taxTotal),
    "\n---------\nTotal: $ {:.2f}".format(total),
    "\n***************************************\nTHANK YOU")#This prints out the reciept and formats everything correctly
