# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
frase =  input('Digite uma frase: ')
print(frase)
print('Abaixo a frase sem espaços:')
print(frase.strip().replace('s','$'))