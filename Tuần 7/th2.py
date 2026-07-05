def display_hash(hashTable): 
    for i in range(len(hashTable)):
        print(i, end = " ")

    for j in hashTable[i]:
        print("-->", end = " ")
    print(j, end = " ")

print()
HashTable = [[] for _ in range(10)] 
def Hashing(keyvalue): 
    return (keyvalue % len(HashTable))
def insert(Hashtable, keyvalue, value): 
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)
insert(HashTable, 10, 'MachineLearning') 
insert(HashTable, 45, 'DataScience')
insert(HashTable, 20, 'DataAnalytics')
insert(HashTable, 9, 'BigData')
insert(HashTable, 21, 'DataStructure ')
insert(HashTable, 41, 'IoT')
insert(HashTable, 35, 'Probability')
display_hash (HashTable) 