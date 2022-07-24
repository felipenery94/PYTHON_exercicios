f = str(input('digite uma frase:')).strip().upper()
palavra = f.split()
junto =''.join(palavra)
inverso=''
for letra in range(len(junto)-1, -1,-1):
    inverso += junto[letra]
print(junto,inverso)


