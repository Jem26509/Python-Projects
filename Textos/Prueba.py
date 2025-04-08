
import os
import Capital

pdf_directory = input('Directorio: ') #'D:\8 - Linkedin\BI'
Carpeta = os.chdir(pdf_directory)

for Nombre in os.listdir():
    print('1', Nombre)
    #print(os.path.splitext(Nombre))
    texto, extension = os.path.splitext(Nombre)
    if extension == '.pdf':
      texto = Nombre.replace('_',' ')
      texto = texto.replace('  ',' ')
      #print('2', texto)

      nombre = texto.split(" 173")
      #print('3', nombre[0])
      if len(nombre) == 1:
         texto = nombre[0]
         #print('4', texto)

      if len(nombre) == 2:
          texto = nombre[0] + extension
          #print('4', texto)
    
      texto = Capital.Capital(texto).capital()
      print('9', texto)
      os.rename(Nombre,texto)
print("FIN")