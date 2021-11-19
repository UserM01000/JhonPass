import itertools
import os

# colores
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
white='\033[97m'

os.system("clear")  

ban = '''
                                                    '''

print(red+'''
     _ _   _  ___  _   _           ____
    | | | | |/ _ \| \ | |         |  _ \ 
 _  | | |_| | | | |  \| |  _____  | |_) |
| |_| |  _  | |_| | |\  | |_____| |  __/ 
 \___/|_| |_|\___/|_| \_|         |_|         ''')

print('''\033[91m
        \033[91m [\033[96m~\033[91m] \033[97mContact Developer\033[91m \033[91m[\033[96m~\033[91m] 
          \033[97mhttps://t.me/HackForAll1/

''')

print("\033[36m[!]Proporciona un tamaño a escala para el texto")
scale = input('\033[36m[!] Ejemplo --> 4:8 : ')
    
start = int(scale.split(':')[0])
final = int(scale.split(':')[1])
opcion = str(input("\n\033[36m[?] Quieres añadir informacion de la persona? [y] [n]: "))
if opcion == 'y':
	primero = str(input("\n\033[36m[*] Primer nombre: "))
	segundo = str(input("\n\033[36m[*] Segundo nombre: "))
	dia = str(input("\n\033[36m[*] Dia de nacimiento: "))
	mes = str(input("\n\033[36m[*] Mes de nacimiento: "))
	año = str(input("\n\033[36m[*] Año de nacimiento: "))
	chrs = primero + segundo + dia + mes + año
else:
	chrs = 'abcdefghijklmnopqrstuvwxyz'
	pass

chrs_mayusculas = chrs.upper()
chrs_especiales = '!\][/?.,~-=";:><@#$%&*()_+\' '
chrs_numeros = '1234567890'

Arch = input('\n\033[36m[!] Ingresa un nombre para tu Archivo mas el .txt --> ')
arq = open(Arch, 'w')
if input('\n\033[36m[?] Quieres usar mayusculas? [y] [n]: ') == 'y':
	chrs = ''.join([chrs, chrs_mayusculas])
if input('\n\033[36m[?] Quieres usar caracteres especiales? [y] [n]: ') == 'y':
	chrs = ''.join([chrs, chrs_especiales])
if input('\n\033[36m[?] Quieres usar numeros? [y] [n]: ') == 'y':
	chrs = ''.join([chrs, chrs_numeros])

for i in range(start, final+1):
	for j in itertools.product(chrs, repeat=i):
		temp = ''.join(j)
		print(temp)
		arq.write(temp + '\n')
arq.close()

if os.path.exists(Arch):
    os.system("clear")
    print(white+"Archivo creado exitosamente....\n")
    print("Gracias por usar mi script :D \nrecuerda seguirme en Github")
    print("y darle estrellas a lo que mas te guste, pronto subire mas script")
    print("esperalos ;D")
else:
    print("File was not found")
