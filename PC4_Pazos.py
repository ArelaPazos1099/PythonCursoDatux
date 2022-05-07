#PREGUNTA 1
n=0
while n<1 or n>10:
    n = int(input('Ingrese un nro del 1 al 10: '))
    with open(f'./tabla-{n}.txt', 'w') as f:
        for i in range(1, 13):
            texto=f'{i} x {n} = {i*n}\n'
            f.write(texto)

        for i in range(1, 13):
            print(f'{i} x {n} = {i*n}\n')

#PREGUNTA 2
m = int(input('Introduce un número entero entre 1 y 10: '))
nombre_archivo = 'tabla-' + str(m) + '.txt'
try: 
    a = open(nombre_archivo, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', m)
else:
    print(a.read())

#PREGUNTA 3
import re
s = "@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%"
palabra= "@robot3!"
buscar=re.search(palabra,s)
if buscar:
    print("Se ha encontrado la palabra ",palabra)
else: print("No se ha encontrado la palabra ", palabra)

#PREGUNTA 4

s = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"
patron = r"User_mentions\D\d, likes\D\d"
print(re.findall(patron,s))
patron2 = r"\Dlikes\D\d"
print(re.findall(patron2,s))
patron3= r"number of retweets\D\d"
print(re.findall(patron3,s))

#PREGUNTA 5
analisis_sentimientos = datos.read_pandas(path,780,782)
regex = r"[aAeEiIoOUu]{2}+.txt"  # complete aqui
for tweet in analisis_sentimientos:
    print(tweet)
    
    #Encuentre todos los casos
    print(re.findall(regex, tweet))

#PREGUNTA 6

# Escriba una expresión regular para validar un correo
regex = r"[1-9a-zA-Z!#%&*$.]+@[\w]+\.com"

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
for example in emails:
    # Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))   

#PREGUNTA7
 
regex = r"^4|5|6[0-9]{16}"

cuentas_bancarias=["4123456789123456",
"5123-4567-8912-3456",
"61234-567-8912-3456",
"4123356789123456",
"5133-3367-8912-3456",
"5123 - 3567 - 8912 - 3456"]

for ejemplo in cuentas_bancarias:
    if re.match(regex,ejemplo):
        print("la cuenta bancaria {cuenta} es una cuenta válida".format(cuenta=ejemplo))
    else:
        print("la cuenta bancaria {cuenta} es una cuenta inválida".format(cuenta=ejemplo))
