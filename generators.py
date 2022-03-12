import time

def FiboGen(max: int):
    num1 = 0
    num2 = 1
    counter = 0
    
    while True:
        if counter == 0:
            counter +=1
            yield num1
        elif counter == 1:
            counter +=1
            yield num2
        else:
            aux = num1 + num2

            if not max or aux >= max:
                num1, num2 = num2, aux
                counter += 1
                yield aux
            else:
                break
            
if __name__ == '__main__':
    fibonacci = FiboGen(5)

    for element in fibonacci:
        print(element)
        time.sleep(1)