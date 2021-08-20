class father:
    def __init__(self):
        self.familyname=("father")
   
    def showf(self):
        print("Father class")


class mother:
    def __init__(self):
        self.familyname=("mother")
    def showm(self):
        print("From mother class")


class  son(father,mother):
     def __init__(self):
        self.familyname=("son")
     def shows(self):
        print("From son class")


s=son()
s.showf()
s.shows()

