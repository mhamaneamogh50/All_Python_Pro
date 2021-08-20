class father:
    def __init__(self):
        self.fathername = "alok"
        
    def show(self):
        print("constroctor from father")


class son(father):
    def shows(self):
        print(" son class ")

s=son()
s.shows()
s.show()
print(s.fathername)
