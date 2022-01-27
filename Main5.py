from Helpers import Helper
from Cargo import Cargo
from Empleados import Empleado
import os

def buscempleado(cod):
    cargo=0
    codigo = 0     
    for pos in range(0,len(Empleado.Empleados)):
        Cargo = Cargo.cargo[pos]
        if empleado["codigo"] == cod:
           Cargo= empleado  ["cargo"]
           break
    return cargo
helper = Helper()
lista = ["1) Cargo","2) Departamento","3) Empleados","4) Salir"]
opcion=""
while opcion != "4":
  os.system("cls")
  opcion = helper.menu(lista,"Menu Ficha Personal")
  if opcion == "1":
     opc1=""  
     while opc1 != "4":
      os.system("cls")
      opc1 = helper.menu(["1) Ingreso","2) Consulta","3) Salir"],"Menu Cargos")
      os.system("cls")
      if opc1 == "1":
        print("Ingresar empleado")
        nombre= input("Nombre del Empleado: ")
        numero=int(input("ingrese numero de cdula"))
        cargo= input("cargo: ")
        departamento=input("ingrese departamento: ")
        ficha= empleado(input(nombre,numero,cargo,departamento))
        empleado = ficha.registro()
        Empleado.Empleados.append(empleado)
        input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
      elif opc1 == "2":
        print("*"*20,"Consultar de empleado ","*"*20)
        print("Codigo"," "*5,"Empleado"," "*5,"Cargo","     Departamento   ","  Nombre")
        for ficha in Empleado.Empleados:
            cod = empleado["codigo"]
            car=empleado["cargo"]
            depa =empleado["departamento"] 
            emple =buscempleado(cod)
            nomb = empleado["nombre"]
            print(" "*2,cod," "*8,car," "*(15-len(depa)),emple," "*(15-len(emple)),nomb)
        input("Presione una tecla para continuar...")       
  elif opcion == "3":
    print("Ingreso de Empleados")
    if opc1 == "1":
        print("Ingreso de empleados")
        nombre= input("Nombre del Empleado: ")
        cargo = empleado(nombre)
        cardoregistro = cargo.registro()
        empleado.empleados.append(cargo)
        input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
  elif opcion == "4":
    print("Salir")
        
print("Gracias por visitarnos")   
    



    