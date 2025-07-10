productos = {
    '001HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '002HD': ['Lenovo', 14.4, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    '003HD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    '004HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    '005HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '006HD': ['Lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '007HD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    '008HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
} # Marca [0], pantalla [1], RAM [2], disco [3], GB de DD [4], procesador [5], video [6]

stock = {
    '001HD': [387500, 10],
    '002HD': [700670, 3],
    '003HD': [1300599, 7],
    '004HD': [600990, 11],
    '005HD': [460000, 4],
    '006HD': [680000, 15],
    '007HD': [429678, 2],
    '008HD': [598400, 0],
} # Precio [0], Stock [1]

print ("¡Bienvenido a Pybooks!")

while True: # Inicia MENÚ PRINCIPAL
    try:
        print ("""
*** MENÚ PRINCIPAL ***
1. Stock marca.
2. Búsqueda por precio.
3. Actualizar precio.
4. Salir.""")
        opcion_menu_principal = int (input ("\nIngrese el número de la opción deseada: "))

        if (opcion_menu_principal < 1) or (opcion_menu_principal > 4):
            print ("\nLa opción ingresada no es válida. Debe ingresar una opción dentro del menú principal.") # En caso de ingresar fuera del rango
            continue
            
# OPCIÓN 1: Stock Marca

        elif (opcion_menu_principal == 1): 
            stock_por_marca = input ("\nIngrese la marca del equipo a consultar: ").strip().lower() # Ignora espacios, pasa todo a minúscula

            stock_total = 0 # Iniciar variable para guardar los stocks
            found = False

            for producto_id, producto_info in productos.items():
                    if producto_info[0].lower() == stock_por_marca:
                            stock_devuelto = stock.get(producto_id, [0])[1] # Recoge el stock [1] del diccionario 'Stock'. Si no hay, devuelve 0
                            stock_total = stock_total + stock_devuelto
                            found = True # Marca que la marca existe
                    
            if not found: # Si la marca no existe en los registros
                    print (f"\n¡Lo sentimos! La marca '{stock_por_marca}' no existe en nuestros registros.")
                    continue
            
            else: # Si la marca existe y la búsqueda es exitosa
                    print (f"\nEl stock de la marca '{stock_por_marca.capitalize()}' es: {stock_total}")
                    continue # .capitalize() sólo estético, para que aparezca lindo el nombre de la marca si sí existe (primera letra mayúscula)

# OPCIÓN 2: Búsqueda por precio

        elif (opcion_menu_principal == 2):
              while True:
                    try:
                          precio_minimo = int (input("\nIngrese el precio mínimo: "))
                          precio_maximo = int (input("Ingrese el precio máximo: "))

                          if (precio_minimo > precio_maximo): # En caso de que se ingrese un mínimo mayor que el máximo
                                print ("\nEl rango de precio ingresado no es válido. El precio mínimo debe ser menor que el precio máximo.")
                                continue
                          
                          else:
                                precio_en_rango = [] # Lista vacía para guardar los equipos dentro del rango de precio

                                for producto_id, producto_info in productos.items():
                                      precio = stock[producto_id][0]
                                      cantidad_stock = stock[producto_id][1]

                                      if (precio_minimo <= precio <= precio_maximo) and (cantidad_stock > 0):
                                             precio_en_rango.append(f"{producto_info[0]} -- {producto_id}")

                                precio_en_rango.sort() # Ordenar alfabéticamente
                                if precio_en_rango:
                                        print ("\nLos modelos encontrados en el rango de precio ingresado son:\n")
                                        for modelo in precio_en_rango:
                                                print (f"- {modelo}")
                                                continue
                                
                                else:
                                      print ("\n¡Lo sentimos! No existen modelos dentro del rango de precio ingresado.")
                                      break
                                
                          break # Siguiendo la línea del If y el Else
                    
                    except ValueError: # except Value en caso de que se ingrese cualquier cosa que no sea número entero en los precios
                          print ("\nEl rango de precio ingresado no es válido. Debe ingresar números enteros.")
                          continue           

# OPCIÓN 3: Actualizar precio
      
        elif (opcion_menu_principal == 3):
              while True:
                    try:
                          modelo_actualizar = input ("""\nIngrese el ID del modelo que desea actualizar: 
                                                     
001HD = ('HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050')
002HD = ('Lenovo', 14.4, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050)
003HD = ('Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti')
004HD = ('HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada')
005HD = ('Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050')
006HD = ('Lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada')
007HD = ('Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050)
008HD = ('Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050')
\n""").strip().upper()
                          
                          if modelo_actualizar in stock:
                                while True:
                                      try:
                                            nuevo_precio = int (input("\nIngrese el precio nuevo: "))
                                            if (nuevo_precio < 0): # Para que no se ingresen negativos
                                                  print ("\nEl precio ingresado no es válido. Debe ingresar un número positivo.") 
                                                  continue
                                            
                                            else:
                                                  stock[modelo_actualizar] = [nuevo_precio]
                                                  print (f"\n¡Precio actualizado con éxito! El nuevo precio del modelo '{modelo_actualizar}' es: ${nuevo_precio}.")
                                                  
                                                  while True:
                                                              continuar = input ("\n¿Desea actualizar otro precio? (s/n): ").strip().lower()
                                                              if continuar == 's':
                                                                    break
                                                              
                                                              elif continuar == 'n':
                                                                    break
                                                              
                                                              else:
                                                                    print ("\nLa opción ingresada no es válida. Debe ingresar s (sí) o n (no).")
                                                                    continue
                                                              
                                                  if continuar == 's':     
                                                        break
                                                  
                                                  elif continuar == 'n':
                                                        break       
                                                  
                                      except ValueError: # except Value si se ingresa cualquier cosa que no sea entero
                                            print ("\nEl precio ingresado no es válido. Debe ingresar un número entero.")
                                            continue
                                      
                                if continuar == 'n':
                                      break
                                
                                else:
                                      continue

                          else:
                                print ("\nEl ID ingresado no es válido. Debe ingresar un ID de la lista.")
                                continue

                    except ValueError: # except Value para los ID's
                          print ("\nEl ID ingresado no es válido. Debe ingresar un ID de la lista.")
                          continue
                                 
# OPCIÓN 4: Salir

        elif (opcion_menu_principal == 4):
              print ("\nPrograma finalizado.")     
              exit()

    except ValueError: # Except Value del Menú Principal 
        print ("\nLa opción ingresada no es válida. Debe ingresar un dígito dentro del menú principal.")