def make_division_by(n):
    def division(num):
        return num / n
    return division

def run():
    division_by3 = make_division_by(3)
    print(division_by3(18))
    
if __name__ == '__main__':
    run()