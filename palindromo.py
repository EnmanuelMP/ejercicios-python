def is_palindromo(string: str) -> bool:
    string = string.lower().replace(' ','')
    return (string == string[::-1])

def run():
    print(is_palindromo('Ana'))
    
if __name__ == '__main__':
    run()