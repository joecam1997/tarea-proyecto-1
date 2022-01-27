from Cargo import Cargo

class Empleado:
  secuencia=2             
  Empleados = [ {"codigo":1,"nombre":"Johanna","cedula":"0951275539","cargo":1,"departamento":1,"sueldo":500.50},
              {"codigo":2,"nombre":"Joel","cedula":"0956234740","cargo":2,"departamento":2,"sueldo":600.30},
            
            ] 

  def __init__(self,id,nombre,cedula,Cargo,Departamento,sueldo):
    Empleado.secuencia +=1
    self.codigo=Empleado.secuencia
    self.identificacion=id
    self.nombre=nombre
    self.cedula=cedula
    self.cargo=Cargo
    self.departamento=Departamento
    self.sueldo=sueldo
    
  def mostrar(self):
    print("{} - {} - {} - {} - {} - ".format(self.codigo,self.identificacion,self.nombre,self.cedula,self.cargo,self.departamento,self.sueldo))

  def registro(self):
    return {"codigo":self.codigo,"identificacion":self.identificacion,"nombre":self.nombre,"cedula":self.cedula,"cargo":self.cargo,"departamento":self.departamento,"sueldo":self.sueldo}