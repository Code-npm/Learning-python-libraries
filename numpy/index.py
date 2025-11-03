# a=[2, 4,5, 6,8,3]
# b=a[3:]
# b[2]=400
# print(b)
# print(a)

# a=[10 , 20 ,30]

# arr=[]

# for n in a:
#     n=n+5
#     arr.append(n)
# print(arr)



prices=[100 , 200 , 300 , 400  , 500 , 600 , 700 , 800 , 900 , 1000]

discount=10

final_prices=[]

for price in prices:
    final_price=price-((price*discount)/100)
    final_prices.append(final_price)

print(final_prices)