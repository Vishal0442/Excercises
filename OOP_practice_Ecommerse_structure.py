# Python program for OOP practice
# Ecommerce domain structure


# part-I - defining all classess

class Vendor:
    def __init__(self,vid, vname, vaddr, vacco,vinventory):
        self.venId = vid
        self.venName = vname
        self.venAddress = vaddr
        self.venAccount = vacco
        self.venInventory = vinventory
        self.venDeliveredOrders = []

    def __str__(self):
        return (f'''
            Vendor ID : {self.venId}
            Vendor Name : {self.venName}
            Vendor Address : {self.venAddress}
            Vendor Account : {self.venAccount}
            Vendor Inventory : {self.venInventory}
            Vendor Delivered Orders : {self.venDeliveredOrders}
            ''')

    def __repr__(self):
        return str(self)

class Customer:
    def __init__(self,cid,cname,cage,caddr,cacco):
        self.custId = cid
        self.custName = cname
        self.custAge = cage
        self.custAddress = caddr
        self.custAccount = cacco
        self.custOrders = []

    def __str__(self):
        return (f'''
            Customer ID : {self.custId}
            Customer Name : {self.custName}
            Customer Age : {self.custAge}
            Customer Address : {self.custAddress}
            Customer Account : {self.custAccount}
            Customer Orderes : {self.custOrders}
            ''')

    def __repr__(self):
        return str(self)

class Address:
    def __init__(self,addrid,addrcity,addrstate,addrpin):
        self.addrId = addrid
        self.addrCity = addrcity
        self.addrState = addrstate
        self.addrPincode = addrpin

    def __str__(self):
        return (f'''
                    Address ID : {self.addrId}
                    Address City : {self.addrCity}
                    Address State : {self.addrState}
                    Address Pincode : {self.addrPincode}      
        ''')

    def __repr__(self):
        return str(self)

class Account:
    def __init__(self,accono, accotype, accobal):
        self.accoNumber = accono
        self.accoType = accotype
        self.accoBalance = accobal

    def __str__(self):
        return (f'''
                    Account No. : {self.accoNumber}
                    Account Type : {self.accoType}
                    Account Balance : {self.accoBalance}
        ''')

    def __repr__(self):
        return str(self)


class Product:
    def __init__(self,pid,pname,pcate,pprice,pqty):
        self.prodId = pid
        self.prodName = pname
        self.prodCategory = pcate
        self.prodPrice = pprice
        self.prodQty = pqty

    def __str__(self):
        return (f'''
            Product ID : {self.prodId}
            Product Name : {self.prodName}
            Product Category : {self.prodCategory}
            Product Price : {self.prodPrice}
            Product Quantity : {self.prodQty}
        ''')

    def __repr__(self):
        return str(self)


class Categories:
    def __init__(self,cid, cname = "Other"):
        self.categoryId = cid
        self.categoryName = cname

    def __str__(self):
        return (f'''
                    Category ID : {self.categoryId}
                    Category Name : {self.categoryName}
        ''')

    def __repr__(self):
        return str(self)

class Order:
    def __init__(self, oid, ven, cust, oprod, offer = None):
        self.orderId = oid
        self.orderVendor = ven
        self.orderCustomer = cust
        self.orderProducts = []
        self.a = None
        if type(oprod) == list:
            self.orderProducts.extend(oprod)
        else:
            self.orderProducts.append(oprod)

        if offer and offer.offerProduct and offer.offerProduct.prodId == oprod.prodId:
            self.discount = oprod.prodPrice * offer.offerPercent
            self.finalAmount = oprod.prodPrice - self.discount

            self.a = (f'''
                    Offer applicable : {offer.offerName} 
                    Available discount : {offer.offerPercent*100}%
                    Discounted price : {self.finalAmount}
                    ''')

    def __str__(self):
        return (f'''
            Order ID : {self.orderId}
            Order Product : {self.orderProducts}
            Offer Applicable : {self.a}
            Order from Vendor : {self.orderVendor}
            Order to Customer : {self.orderCustomer}
        ''')

    def __repr__(self):
        return str(self)

class Offer:
    def __init__(self,offerid,offername,offerproduct,offerpercent):
        self.offerId = offerid
        self.offerName = offername
        self.offerProduct = offerproduct
        self.offerPercent = offerpercent

    def __str__(self):
        return (f'''
            Offer ID : {self.offerId}
            Offer Name : {self.offerName}
            Offer on Product : {self.offerProduct}
            Offer Percentage : {self.offerPercent}
            ''')

    def __repr__(self):
        return str(self)



# part-II - generating offers

JAN50 = Offer(offerid=11004568,offername="JAN50",offerproduct=None,offerpercent=0.5)
FEB40 = Offer(offerid=11004568,offername="FEB40",offerproduct=None,offerpercent=0.4)
MAR30 = Offer(offerid=11004568,offername="MAR30",offerproduct=None,offerpercent=0.3)
APR20 = Offer(offerid=11004568,offername="APR20",offerproduct=None,offerpercent=0.2)

offerlist = [JAN50, FEB40, MAR30, APR20]



# part-III - generating customer & vendor details

def initalizeInfo():

    cat1 = Categories(1111, cname = "Shirts")
    cat2 = Categories(2222, cname = "Pants")
    cat3 = Categories(3333, cname = "Footware")
    cat4 = Categories(4444, cname = "Accessories")
    cat5 = Categories(5555, cname = "Jackets")
    cat6 = Categories(6666, cname = "T-Shirts")

    categoryList = [cat1, cat2, cat3, cat4, cat5, cat6]

    prod1 = Product(1215,"Watch",cat4,2599,32)
    MAR30.offerProduct = prod1

    inventoryProducts = []
    count = 101
    if count == 1215:
        count += 1

    for i in range(30):
        product = Product(pid=count,
                          pname=get_random_name(),
                          pcate=categoryList[random.randint(0,5)],
                          pprice=(random.randint(499,4999)),
                          pqty=(random.randint(10,100)))
        count += 1
        inventoryProducts.append(product)

    inventoryProducts.insert(random.randint(0,29),prod1)

    Customer1 = Customer(123456,"Ravi",26,caddr=None,cacco=None)
    Customer1.custAddress = Address(12452,"Pune","MH",416208)
    Customer1.custAccount = Account(5006004287952, "Saving", 14485.65)

    Vendor1 = Vendor(12485976, "Myntra", vaddr=None, vacco=None,vinventory=None)
    Vendor1.venAddress = Address(42659,"Benglore","KN",225876)
    Vendor1.venAccount = Account(12457963548325, "Current",287563.26)
    Vendor1.venInventory = inventoryProducts

    return Customer1, Vendor1

import random
def get_random_name():
    prodname = ''
    for i in range(random.randint(4,8)):
        prodname += chr(random.randint(65,90))
    return prodname.title()



# part-IV - defining sample function - purchase product

def purchase_product(cust, ven, ctprod, ctcat, ctqty):
    print (ven.venName, "Service Operations Started")

    prodflag = False
    for prod in ven.venInventory:
        if prod.prodName == ctprod and prod.prodCategory.categoryName == ctcat and prod.prodQty >= ctqty:
            prodflag = True
            bill_amount = prod.prodPrice * ctqty
            a = None
            for offer in offerlist:
                if offer.offerProduct and offer.offerProduct.prodName == prod.prodName:
                    a = offer
                    print ("Billing amount before discount : ",bill_amount)
                    print ("Discount available for this order : ",((prod.prodPrice*offer.offerPercent)*ctqty))
                    bill_amount -= ((prod.prodPrice*offer.offerPercent)*ctqty)

            print ("Final billing amount : ",bill_amount)

            prod.prodQty -= ctqty
            cust.custAccount.accoBalance -= bill_amount
            ven.venAccount.accoBalance += bill_amount

            order = Order(oid=4578935246, ven=ven, cust=cust, oprod=prod, offer=a)

            ven.venDeliveredOrders.append(order)
            cust.custOrders.append(order)

            print ("Order placed successfully")

    if prodflag == False:
        print ("Out of stock / Not enough quantities available / Product not found")



# Starter

if __name__ == "__main__":
    cust, ven = (initalizeInfo())
    purchase_product(cust, ven, "Watch","Accessories",5)






