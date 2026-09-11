'''
class Flipkart:
    discount = 30
    def info(self,name,phoneno,address):
        self.name = name
        self.phoneno = phoneno
        self.address = address
        print(f'Welcome to the Flipkart',self.name)

lucky = Flipkart()
lucky.info('lucky',9997775553,'Hyd')
eswar = Flipkart()
eswar.info('eswar',8886664442,'Bnglr')
sakhi = Flipkart()
sakhi.info('sakhi',7779995553,'Mumb')
----------------------------------------------
'''
class Flipkart:
    discount = 30

    @classmethod
    def updatediscount(cls):
        cls.discount= 50
        print("Updated Discount:",cls.discount)

    def info(self,name,phoneno,address):
        self.name = name
        self.phoneno = phoneno
        self.address = address
        print(f'Welcome to the Flipkart',self.name)

    @staticmethod
    def banner():
        print(f'{Flipkart.discount}% discount is going, grab the discount')

lucky = Flipkart()
lucky.info('lucky',9997775553,'Hyd')
lucky.updatediscount()
lucky.banner()

eswar = Flipkart()
eswar.info('eswar',8886664442,'Bnglr')
eswar.updatediscount()
eswar.banner()
 
sakhi = Flipkart()
sakhi.info('sakhi',7779995553,'Mumb')
sakhi.updatediscount()
sakhi.banner()
