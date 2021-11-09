products = ['Soap','Shampoo','Oil']
product_category = [{'Dove':20,'pears':25},{'Pantene':27,'Silk':24},{'Coconut':10,'Olive':15}]
cart_items = []
price = []

while True:
    user_input = input('Want to enter items in cart?\n Y/N \n')

    if user_input.upper() == 'Y':
        print('Available products are: ')

        for names in products:
            print(names)
        user_productName = input('Enter the product name: ')
        indexing = products.index(user_productName)

        for categoryName,Price in product_category[indexing].items():
            print(categoryName,":",Price)
        user_categoryName= input('Enter the category name: ')
        quantity = int(input('Enter the quantity of the product: '))
        cart_items.append(user_categoryName)
        price.append(product_category[indexing][user_categoryName]*quantity)

    if user_input.upper() == 'N':
        break

    print(cart_items,price,sum(price))












