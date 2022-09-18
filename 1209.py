# # 1209
def find_big(v):
    small_letters = 0
    big_letters = 0
    for letter in v:
        if letter.islower():
            small_letters += 1    
        else:
            big_letters += 1
        if big_letters > small_letters:
            return True
        else:
            return False

def homework(v):
    strings = v.split()
    string_len = len(strings)
    big_str = 0
    small_str = 0 
    for string in strings:
        if find_big(string):
            big_str += 1
        else:
            small_str += 1
            
    first = big_str / string_len * 100
    second = small_str / string_len * 100
    
    print("big :{0} percent, small :{1} percent".format(first,second))  
    
homework("kvsKVS IkIiki kvsiki")

