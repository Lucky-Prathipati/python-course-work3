#POVIDNG SECURITY TO DATA
'''1. Public Proctection : allowe  inclass , inchildclass ,outsideClass
2. private Protection : allowed inclass [we use double underscore "__"]
3. protected method   : allowed inclass, inChildClass,outsideClass(not recommended)  [we use single underscoe " _"]'''



'''class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []

    def getpassword(self):
        return self.__password

    @property
    def accesspost(self):
        return self._post        

lucky = Instagram('lucky','12345')

print(lucky.username)
print(lucky.getpassword())
print(lucky.accesspost) '''



class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []

    def getpassword(self):
        return self.__password

    def setpassword(self,setpassword):
        self.__password  = setpassword   

    @property
    def accesspost(self):
        return self._post   

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)


lucky = Instagram('lucky','12345')

lucky.username = "lucky_123"
print(lucky.username)

lucky.setpassword('teddy#123')
print(lucky.getpassword())

lucky.accesspost ="python"
lucky.accesspost ="strings"
lucky.accesspost ="project" 
print(lucky.accesspost)