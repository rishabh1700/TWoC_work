#WAP which take two inputs cost price and selling price of a product from user and return following ... 1.Profit from this sale and 2.What should be the selling price if we want to increase our current profit by 5%

cp = float(input("Enter the cost price of product : "))
sp = float(input("Enter the selling price of product : "))
if sp>cp:
    
    print("Profit from this sale : ",sp-cp)
    print("If you want to increase your current profit by 5% then the selling price should be ",sp+((sp-cp)*5/100))

else:
    print("There is no profit")
