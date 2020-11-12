products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q' :
		break
	price = input('請輸入商品價格：')
	price = int(price)
	products.append([name, price])
print(products)

products[0][0]


for product in products:
	print(product)
	print(product[0],'的價格是', product[1])

with open('products.csv', 'w', encoding= 'utf-8') as f :
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')