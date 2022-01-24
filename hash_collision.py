import hashlib
import os
import random
import string

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    characters = string.ascii_lowercase
    characters = characters + string.ascii_uppercase
    characters = characters + string.digits
    characters = characters + string.punctuation
    
    x = get_string(20, characters)
    y = get_string(20, characters)

    x_bits = get_bits(x,k)
    y_bits = get_bits(y,k)
    count =0
    list_of_strings = [x]
    new_bits = y_bits

    while ((get_bits(x,k))!=(get_bits(y,k))):
        new_string = get_string(20,characters)
        new_bits = get_bits(new_string, k)

        for i in range(len(list_of_strings)):
            x_bits = get_bits(list_of_strings[i],k)
            if (new_bits==x_bits):
                x = list_of_strings[i]
                y = new_string
                break

        list_of_strings.append(new_string)        

        count= count + 1
        #print(count)
    #Collision finding code goes here


    x = x.encode('utf-8')
    y = y.encode('utf-8')
    
    return( x, y )

def get_bits(string, k):
    hex_str = hashlib.sha256(string.encode('utf-8')).hexdigest()
    bit_str = bin(int(hex_str, 16)).zfill(8)
    return(bit_str[-k:])

def get_string(length, characters):
    
    string = ''.join(random.choice(characters) for i in range(length))
    return string
