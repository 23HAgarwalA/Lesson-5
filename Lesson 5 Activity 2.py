costprice = float(input("What was the cost price of the item"))
sellingprice = float(input("What was the selling price of the item"))
if sellingprice > costprice:
    profit = sellingprice - costprice
    print ("Your profit is", profit)
else:
    loss = costprice - sellingprice
    print ("Your loss is", loss)
