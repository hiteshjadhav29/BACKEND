from payment import payment
from product import product
class order(product,payment):
    def bill(self):
        qty= int(input("enter the quantity: "))
        total=self.price*qty
        print(self.show_product())
        print(self.pay(total))

obj=order("car",5000)
obj.bill()