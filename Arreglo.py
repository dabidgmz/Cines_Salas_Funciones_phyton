import json

class Arreglo:

    def __init__(self):
        self.lista=[]
        
    def create(self, func):
        self.lista.append(func)
        
    def read(self):
        result=[]
        for i in range(len(self.lista)):
            result.append(str(self.lista[i]))
        return result
    
    def update(self, id, func):
        for i in range(len(self.lista)):
            if id==i:
                self.lista[i]=func
                
    def delete(self, func):
        self.lista.remove(func)
        
    def search(self, nombre):
        for i in range(len(self.lista)):
            if nombre==i:
                return str(self.lista[i])
    def __iter__(self):
        return iter(self.lista)
    
    def over_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.get_output(), file, ensure_ascii=False, indent=2)