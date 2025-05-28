
import os
import Capital
import sys

if len(sys.argv) > 1:
    Directory = sys.argv[1]
    if len(sys.argv) > 2:
        Txt_1 = input('Texto: ')
        Txt_2 = input('Reemplazo: ')
    else:  
        Txt_1 = Txt_2 = ""
else:
    Directory = input('Directorio: ')
    Txt_1 = input('Texto: ')
    Txt_2 = input('Reemplazo: ')
Carpeta = os.chdir(Directory)

for Nombre in os.listdir():
    print('1', Nombre)
    Archivo, Extension = os.path.splitext(Nombre)
    Archivo = Archivo.replace('  ',' ')
    Archivo = Archivo.replace('+',' ')
    #Archivo = Archivo.replace('-',' ')
    #Archivo = Archivo.replace('_',' ')
    Archivo = Archivo.replace('!','')
    Archivo = Archivo.replace('¡','')
    if Archivo[0] != "_":
        Archivo = Archivo.replace('_',' ')

    if Extension != '':
        Texto = Archivo.split(" 169")
        Archivo = Texto[0]

        Archivo = Capital.Capital(Archivo).capital() + Extension.lower()
        if Txt_1 != "": #and Txt_2 != "":
            if sys.argv[2] == 'X':
                Archivo = Archivo.replace(Txt_1,Txt_2)

            if sys.argv[2] == '1':
                Archivo = Archivo.replace(Txt_1,Txt_2,1)


        print('9', Archivo)
        os.rename(Nombre,Archivo)
print("FIN")