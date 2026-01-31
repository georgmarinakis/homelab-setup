


class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def show(self):
        print("Hello my name is " + self.name + " and I" + " work in " + self.company + ".")


obj = GFG("John", "GeeksForGeeks")
obj.show()


class GFF:
    def __init__(someone, name, company):
        someone.name = name
        someone.company = company

    def show(someone):
        print("Hello my name is " + someone.name + " and I" + " work in " + someone.company + ".")

tet = GFF("Terry","Taylor")
tet.show()

        
