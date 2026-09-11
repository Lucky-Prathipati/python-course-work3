class whatsappv1:
    def message(self):
        print("you can send a message")

class whatsappv2(whatsappv1):
    def status(self):                                          # single inheritance
        print("you can upload the status for 24 hrs")

ravi = whatsappv1()
ravi.message()       

sakhi = whatsappv2()
sakhi.message()
sakhi.status()





'''class whatsappv1:
    def message(self):
        print("you can send a message")

class whatsappv2(whatsappv1):
    def status(self):                                          # multilevel inheritance
        print("you can upload the status for 24 hrs")


class whatsappv3(whatsappv2):
    def groups(self):
        print("you can create groups and communicate with multiple people at atime")        

ravi = whatsappv1()
ravi.message()       

sakhi = whatsappv2()
sakhi.message()
sakhi.status()

lucky = whatsappv3()
lucky.message()
lucky.status()
lucky.groups()'''


class whatsappv1:
    def message(self):
        print("you can send a message")

class whatsappv2(whatsappv1):
    def status(self):                                          # multilevel inheritance
        print("you can upload the status for 24 hrs")          #multiple inheritance
                                                               # hybrid inheritance 


class whatsappv3(whatsappv2):
    def groups(self):
        print("you can create groups and communicate with multiple people at atime")    


class  whatsappv4:
    def community(self):
        print("you can combine multiple groups")

class whatsappv5(whatsappv3,whatsappv4):
    def channels(self):
        print("you can access to different channels")


lucky = whatsappv5()
lucky.message()
lucky.status()
lucky.groups()
lucky.community()
lucky.channels()



class whatsappv1:
    def message(self):
        print("you can send a message")

class whatsappv2(whatsappv1):
    def status(self):                                          
        print("you can upload the status for 24 hrs")          # hirarchial inheritance
                                                            


class whatsappv3(whatsappv1):
    def groups(self):
        print("you can create groups and communicate with multiple people at atime")    


class  whatsappv4(whatsappv1):
    def community(self):
        print("you can combine multiple groups")




lucky = whatsappv1()
lucky.message()
lucky = whatsappv2()
lucky.message()
lucky.status()
lucky = whatsappv3()
lucky.message()
lucky.groups()
lucky = whatsappv4()
lucky.message()
lucky.community()