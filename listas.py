datos=[]

op =1
while op==1:
    nom = input("Nombres: ")
    correo = input("Correo: ")
    lista=[nom, correo]
    datos= datos.append(lista)
    op = int(input("Desea continua[1/0]: "))
print(datos)
nom = input("Ingresar nombre a buscar: ")
for i in range(0,len(datos)):    
    print(datos[i][0])
