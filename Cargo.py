class Cargo:
    secuencia=2
    cargos = [{"codigo":1,"descripcion":"Analista"},{"codigo":2,"descricion":"Jefe"}]
    def __init__(self,cargo, id):
        Cargo.secuencia +=1
        self.codigo=cargo.secuencia
        self.descripcion=cargo
        self.identificacion = id
    def mostrar(self):
        print("{} - {} - {} ".format(self.codigo,self.descripcion,self.identificacion))
        
    def datos(self):
        return [self.codigo,self.descripcion,self.identificacion]
    
    def registro(self):
        return {"codigo":self.codigo,"cargo":self.descripcion,"id":self.identificacion}

    def __init__ ( self , id , cargo ):
        self.identificación  = id 
        self.cargo = cargo
    def  id ( self ):
        return self.__id 
    def getDepto(self):
        return str(self.id)+"%"+self.cargo
