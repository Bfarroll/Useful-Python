meal = 44.50
tax = 0.0675
tip = 0.15

""" The code above is where we are declaring our variables and their own indvidual prices. 
The code below is where we use the math to work out the total sum of the meal. 
Lastly the print is where it will print out the variable 'total' which is the anwser we're looking for. 

"""

meal = meal + meal * tax
total = 47.96 + 44.50 * 0.15

print("%.2f" % total)
