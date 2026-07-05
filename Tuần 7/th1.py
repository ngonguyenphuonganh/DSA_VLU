def hash_key( key, m): 
    return (key % m) 
m = 7
print(f'The hash value is {hash_key(15,m)}') 
print(f'The hash value is {hash_key(2,m)}')
print(f'The hash value is {hash_key(3,m)}')
print(f'The hash value is {hash_key(9,m)}')
print(f'The hash value is {hash_key(11,m)}')
print(f'The hash value is {hash_key(7,m)}')