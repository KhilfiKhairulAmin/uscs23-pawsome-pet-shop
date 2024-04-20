"""
Program: db.py
Author: Khilfi, Murfiqah, Zainatul
Perform database operations for reading, and saving data from all text file.
"""


def loadOrders():
  orders: list[dict] = []
  with open('db/orders.txt') as file:
    next(file)  # Skip data header
    for line in file:
      (id, userId, address, datetime, status, totalPrice, *products_) = line.split(',')  

      # Parse products into list of dictionaries
      i = 2
      products = []
      while i < len(products_):
        products.append({
          "id": products_[i-2],
          "price": float(products_[i-1]),
          "quantity": int(products_[i])
        })
        i += 3

      orders.append({
        "id": id,
        "userId": userId,
        "address": address,
        "datetime": datetime,
        "status": True if status == "True" else False,
        "totalPrice": float(totalPrice),
        "products": products
      })
  
  return orders


def saveOrders(orders: list[dict]):
  header = "id,userId,address,datetime,status,totalPrice,productId,price1,productId2,price2,...,productIdN,priceN"
  raw_data = header + '\n'
  for order in orders:
    raw_data += f'{order["id"]},{order["userId"]},{order["address"]},{order["datetime"]},{order["status"]},{order["totalPrice"]}'

    for product in order["products"]:
      v = list(product.values())
      while len(v) > 0:
        raw_data += f',{v.pop(0)},{v.pop(0)},{v.pop(0)}'
    raw_data += '\n'

  with open('db/orders.txt', 'w') as file:
    file.write(raw_data)


def saveProducts(stocks):
  file = open("db/products.txt", 'w')
  file.write("id,imageId,company,name,price,unit,sold\n")
  for stock in stocks:
    file.write("{},{},{},{},{},{},{}\n".format(stock["id"], stock["imageId"], stock["company"], stock["name"], stock["price"], stock["unit"], stock["sold"]))
  file.close()


def loadProducts():
  file = open('db/products.txt', 'r')
  next(file)  # Skip data header
  stocks = []
  for line in file:
    id_, imageId, company, name, price, unit, sold = line.strip().split(",")
    stocks.append({
        "id": id_,
        "imageId": imageId,
        "company": company,
        "name": name,
        "price": float(price),
        "unit": int(unit),
        "sold": int(sold)
    })
  file.close()
  return stocks


def loadUsers():
  users = []
  with open('db/users.txt', 'r') as file:
    next(file)
    for line in file:
      id_, username, password = line.split(',')
      users.append({
          "id": id_,
          "username": username,
          "password": password,
      })
  return users


def saveUsers(users):
  header = "id,username,password"
  raw_data = header + '\n'
  for user in users:
    raw_data += f"{user['id']},{user['username']},{user['password']}"
  
  with open('db/users.txt', 'w') as file:
    file.write(raw_data)


if __name__ == "__main__":
  print("\nTEST 1: Load orders")
  orders = loadOrders()
  print(orders)

  print("\nTEST 2: Save orders (Refer orders.txt for output)")
  saveOrders(orders)

  print("\nTEST 3: Load products")
  overallProducts = loadProducts()
  for product in overallProducts:
      print(product)

  print("\nTEST 4: Save products (Refer products.txt for output)")
  saveProducts(overallProducts)

  print("\nTEST 5: loadUsers")
  users = loadUsers()
  print(users)

  print("\nTEST 6: saveUsers (Refer users.txt for output)")
  saveUsers(users)
