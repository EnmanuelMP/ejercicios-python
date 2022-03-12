def es_primo(num: int) -> str:
    for n in range(2, num):
        if num % n == 0:
            return print(f'No es primo. {n} es divisor de {num}')
                  
    print("Es primo")

def run():
    num: int = int(input('Inserte un numero: '))
    es_primo(num)

if __name__ == '__main__':
    run() 