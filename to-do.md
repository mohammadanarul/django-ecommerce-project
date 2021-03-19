1.Account
    1. Username
    2. email

#Done  
2. Category
    1. category name
    2. slug
#Done
3. Brand
    1. brand name
    2. slug
#Done
4. Product
    1. product title
    2. product discription
    3. product image
    4. category
    5. brand
    6. price
    7. discount price
    8. product avoilable adn unavoilable
    9. slug
#Prosessing   
5. OrderItem
    1. user(AUTH_USER_MODEL)
    2. item(Product)
    3. quantity
    4. ordered(Boolean=Flase)
#Prosessing   
6. Order
    1. user(AUTH_USER_MODEL)
    2. items(OrderITem)
    3. ordered(Boolean=Flase)
