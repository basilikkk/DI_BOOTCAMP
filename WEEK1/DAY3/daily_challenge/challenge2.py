"""Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
Sort the list in alphabetical order.
Return “Nothing” if you can’t afford anything from the store.
Hint : make sure to convert the amount from dollars to numbers. Create a program that deletes the $ sign, and the comma (for thousands)

Examples

The key is the product, the value is the price

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"

➞ ["Bread", "Fertilizer", "Water"]

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100" 

➞ ["Apple", "Bananas", "Fan", "Honey", "Spoon"]

# In fact the prices of Apple + Honey + Fan + Bananas + Pan is more that $100, so you cannot by the Pan, 
# instead you can by the Spoon that is $2

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1" 

➞ "Nothing"""

items = {'apple':'5$', 'waffles':"12$", 'computer':'1004$', 'sausage':'15$','dog food':'20$'}

deposit=int(input('type please how much you have in your wallet'))

converted_items={item:int(price.replace('$','').replace(',','')) for item, price in items.items()}

items_sorted=dict(sorted((converted_items.items()),key=lambda item: item[1]))

print(items_sorted)

purchased_items=[]
total_cost=0

for item, price in items_sorted.items():
    if total_cost+price <=deposit:
        purchased_items.append(item)
        total_cost+=price
    else:
        break    





if purchased_items:
    print(purchased_items.sort())
else:
    print('Nothing')        