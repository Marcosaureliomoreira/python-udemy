
from dis import dis

print(ord('a')) # Retorna o código da letra.


abc = list('dvfevwrvwrvefvwertvadsgbvlm')
print({ord(letra) for letra in abc})  #Retornando valores com "set", portanto não há códigos de letras repetidos.


print([ord(letra) for letra in abc])  #Aqui estamos retornando os valores com lista, portanto há valores repetidos.


print({str(ord(letra)) for letra in abc if ord(letra) <= 105}) #Convertendo para strings emostrando apenas os valores que sejam menores que 105.


print({str(ord(letra)) if ord(letra) <= 105 else ord(letra) for letra in abc}) #Quando usamos "if" e "else" na mesma linha, o "for" vem por último.

