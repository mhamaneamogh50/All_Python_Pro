class Human:
    def __init__(self,n,o):
        
        self.name=n
        self.occupation=o


    def do_work(self):
        if self.occupation=="Football Player":
            print(self.name,"plays football")
        elif self.occupation=="actor":

            print(self.name,"shots filf")



    def speaks(self):
        print(self.name,"HRU")

tom=Human("tom","actor")
tom.do_work()
tom.speaks()
nay=Human("Naymer","Football Player")
nay.do_work()
nay.speaks()
