# Como usuario de la aplicación quiero que se clasifique cualquier número entero según 
# sea múltiplo de 3, de 5, de ambos o de ninguno para que el juego muestre 
# la respuesta correcta.

def fizzbuzz(num):
    if num == 0:
        return "FizzBuzz"
    if num % 3 == 0:
            return "Fizz"
    if num % 5 == 0:
            return "Buzz"
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    return num

#Bug en producción: python -m unittest -v
#El problema es el orden de las condiciones. 
#Cuando num es 15, es divisible por 3, así que el primer 
#if se cumple y la función retorna "Fizz" de inmediato, 
#sin llegar nunca a la condición de FizzBuzz.

print(fizzbuzz(0))


