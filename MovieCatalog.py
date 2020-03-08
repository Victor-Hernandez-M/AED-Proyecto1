from Nucleo.LinkedList import *
class MovieCatalog:
    def __init__(self):
        self.catalog = LinkedList()
    
    def add(self,obj):
        if isinstance(obj,Movie):
            self.catalog.push(obj)
            return True
        return False

    def remove(self,pos):
        if (not self.catalog.first):
            return False
        if (isinstance(pos,int) and pos>-1):        
            self.catalog.remove(pos)
    
    def edit(self,obj,pos):
        if (not self.catalog.first):
            return False
        if isinstance(obj,Movie):
            if (isinstance(pos,int) and pos>-1):
                self.catalog.edit(obj,pos)
                return True
        return False 

    def table(self):
        count = 0
        current = self.catalog.first
        table = ""
        for i in range(self.catalog.lenght()):
            if (i==0):
                table += "-"*60  +"\n"
                table += "id   |   name     |    duration     |     description      \n"
                table += "-"*60  +"\n"
                table += "%s   |   %s       |     %s           |     %s               \n" %(count,current.value.name,current.value.duration,current.value.description)
                table += "-"*60  +"\n"
            else:
                table += "%s   |   %s       |     %s           |     %s               \n" %(count,current.value.name,current.value.duration,current.value.description)
       return table
                table += "-"*60  +"\n"
            count += 1
            current = current.next
 
