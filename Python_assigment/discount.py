# Input
prices = ["₹350 (Mixer Grinder)", "₹1200 (Gas Stove)", 
          "₹999 (Pressure Cooker)", "₹4500 (Refrigerator)"]

# Extract prices from strings
base_prices = list(map(lambda x: int(x.split()[0].strip('₹')), prices))

# Apply 10% tax
taxed = list(map(lambda x: int(x * 1.1), base_prices))

# Update prices with names
updated_prices = []
for i in range(len(prices)):
    name = prices[i].split(' ', 1)[1]
    updated_prices.append(f"₹{taxed[i]} {name}")
#list comprehension
# updated_prices = [f"₹{taxed[i]} {prices[i].split(' ', 1)[1]}" for i in range(len(prices))]
# Output
print("Original Prices:", prices)
print("Taxed Prices:", updated_prices)
