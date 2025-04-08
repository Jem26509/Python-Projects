
import Capital
import pyperclip

Texto = input('texto: ')
Texto = Capital.Capital(Texto).capital()
pyperclip.copy(Texto)
print('Texto:', Texto)
