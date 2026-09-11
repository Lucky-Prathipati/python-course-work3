'''class whatsappv1:
    def status(self):
        print("you can upload the status for 24hrs")

class whatsappv2(whatsappv1):
    def status(self):
        super().status()        
        print("you add mudic and you can react")

a = whatsappv1()
a.status()
b= whatsappv2() 
b.status() 
-----------------------
 '''


class whatsappv1:
    def status(self):
        print("you can upload the status for 24hrs")

class whatsappv2:
    def status(self):     
        print("you add mudic and you can react")

class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2 .status(self)
        print('you can add to the cross platforms')

a = whatsappv1()
a.status()

b= whatsappv2() 
b.status() 

c = whatsappv3()
c.status()