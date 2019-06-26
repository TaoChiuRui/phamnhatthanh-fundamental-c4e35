prices={'banana': 4,'apple': 2,'orange': 1.5,'pear': 3}
stock={'banana': 6,'apple': 0,'orange': 32,'pear': 15}
# for key in prices:
#     print(key)
#     print('price:',prices[key])
#     print('stock:',stock[key])
total=0
for key in prices:
    revenue=prices[key]*stock[key]
    total=total+revenue
print(total)