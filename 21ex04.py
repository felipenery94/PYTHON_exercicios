def leiaint(msg):
   ok = False
   valor = 0
   while True:
       n = str(input(msg))
       if n.isnumeric():
           valor = int(n)
           ok = True
       else:
           print('\033[0;32mERRO!!! DIGITE NOVAMENTE UM NÚMERO VÁLIDO\033[m')
       if ok:
            break
   return valor

n = leiaint('DIGITE UM NÚMERO')
print(f'O NÚMERO DIGITADO FOI {n}')
