class hotstar:
    def __init__(self,name):
        print(f'Welcome to the hotstar,{name}')
    def auth (self):
        print("you can login/register")
    def dashboard(self):
        print("you can see the dash board")
    def search(self):
        print("you can search")
    def history(self):
        print("you can see the history")
    def playcontrollers(self):
        print("you resume the vedio")                
    def  download(self):
        print("you can't download")
    def ads(self):
        print("ads will be run")
    def quality(self):
        print("you have limited quality")        
    def devices(self):
        print("acces to single device")
    def access(self):
        print("limitted access")           
    
class premiumhotstar(hotstar):
    def __init__(self,name):
        print(f'Welcome to the premium hotstar,{name}')
    def  download(self):
        print("you can download")
    def ads(self):
        print("ads will not  be run")
    def quality(self):
        print("you have high quality")        
    def devices(self):
        print("acces to multiple devices")
    def access(self):
        print("unlimitted access")                

lucky = hotstar("lucky")
lucky.auth ()
lucky.dashboard()
lucky.search()
lucky.history()
lucky.playcontrollers()
lucky.download()
lucky.ads()
lucky.quality()
lucky.devices()
lucky.access()


lucky = premiumhotstar("lucky")
lucky.auth ()
lucky.dashboard()
lucky.search()
lucky.history()
lucky.playcontrollers()
lucky.download()
lucky.ads()
lucky.quality()
lucky.devices()
lucky.access()