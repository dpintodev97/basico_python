#Escritura en fichero
#Cómo haría para escribir en fichero en el disco duro?

#FUNCION
def guarda_en_discoduro():
   with open('ejemplo.txt', 'w') as archivo:
    # Escribe líneas en el archivo
      archivo.write('Este es un ejemplo de cómo escribir en un archivo en Python.\n')
      archivo.write('Puedes escribir múltiples líneas también.\n')
      archivo.write('¡Es muy útil para guardar datos o resultados!\n')

guarda_en_discoduro()
#CREARÁ UN ARCHIVO LLAMADO "EJEMPLO.TXT" EN EL DIRECTORIO ACTUAL (O SOBREESCRIBIRÁ EL ARCHIVO SI YA EXISTE)
# Y ESCRIBIRÁ LAS TRES LÍNEAS DE TEXTO PROPORCIONADAS EN ÉL.