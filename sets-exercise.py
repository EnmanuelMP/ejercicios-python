
def remove_duplicates(list):
    set_list = set(list)
    convert_to_list = [x for x in set_list]
    print(convert_to_list)
          
def run():
    remove_duplicates([1,8,8,8,8,2,3,54])
    
    
if __name__ == '__main__':
    run()