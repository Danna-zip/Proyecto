#Simulador de Cajero Supermercado
#Danna Paola Pimentel Gonzalez
'''
¿Qué es y para qué este programa?
Este programa es un pequeño simulador de un cajero de un supermercado, muestra una lista de productos
y con respecto a estos se puede comprar lo que se desee, casi como en una tienda virtual.
'''
'''
|   o |_  __ _  __ o  _
|__ | |_) | (/_ |  | (_|
'''
#Libreria de los productos junto con los precios de los mismos.
LibreriaPrecios={
  "Azúcar":30,
  "Sal":10,
  "Café":150,
  "Arroz":25,
  "Harina":20,
  "Fideos":20,
  "Leche":25,
  "Aceite":50,
  "Salsa de tomate":20,
  "Queso rallado":100,
  "Huevos":50,
  "Pan":30,
  "Carne":150,
  "Yogurt":30,
  "Mantequilla":100,
  "Galletas":20,
}
'''
 __
|_    __  _  o  _ __  _  _
|  |_|| |(_  | (_)| |(/__>
'''
#Inicio de las funciones

def MenuInicioCompra():

    print("Productos y Precios")
    for Producto,Precio in LibreriaPrecios.items():
      print(f"{Producto}: ${Precio}") #Imprime el producto y el precio

#definiendo lista y variables
    ListadeCompra=[]
    TotalCompra=0
    Producto=""

    while True:#Bucle

      Producto=input("\n\n Ingrese nombre del producto (. para salir/terminar):  ") #Se pide el Producto.
      if Producto==".":
        break

      if Producto in LibreriaPrecios:
        while True:#Repeticion del Try-Except
          try:
            Cantidad=int(input("Ingrese la cantidad que necesita del producto: ")) #Se pide la Cantidad del Producto.
            break
          except ValueError:# Si en el try hay un error se ejecuta el except
            print("Cantidad no valida")
            print("Favor de ingresar un número entero")
     
        Precio=LibreriaPrecios[Producto]
        TotalCompra+=Precio*Cantidad #En la variable se suma el precio por la cantidad
        ListadeCompra.append((Producto,Cantidad,Precio))#Unimos los productos,cantidad y precio.

      else:
        print("Producto no encontrado") #En caso de que no se encuentre el producto

#Resumen de la compra
    print("\nLista de Compra:")
    for Producto, Cantidad, Precio in ListadeCompra:
            print(f"- {Producto} x {Cantidad} = ${Precio * Cantidad}") #Calculo de la compra
    print(f"Total: ${TotalCompra}")#Total final de la compra
'''
___               
 | __  o  _  o  _ 
_|_| | | (_  | (_)
'''
def Inicio():#Funcion para la repeticion de los menús
    while True:
#Primer Menú
        print("\n                       INICIO:\n                       1-Iniciar Compra\n                       2-Salir \n\n  ")
        
        while True:#Repeticion de Try
            try: #Inicio del Try
              eleccion=int(input("Elige una opcion: "))
              break
            except ValueError: #Si el try tiene un error se ejecuta:
              print("Opcion no valida.")
              print("Favor de ingresar un número entero.")
        
#Segundo Menú
        if eleccion==1:
            MenuInicioCompra()
#Opcion Salir del Programa
        elif eleccion==2:
            print("Saliendo del Programa")
            break
#Cualquier otra opcion es invalida
        else:
            print("Opcion no valida")
Inicio()
 
                