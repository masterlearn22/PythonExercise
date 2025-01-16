my_list = [1,2,3,4,5]
for item in my_list:
    print(item,end=" ")

print()
my_set={1,2,3,4,5}
for item in my_set:
    print(item,end="-")
    
print()
my_tuple=(1,2,3,4,5)
for item in reversed(my_tuple):
    print(item,end="_")
    
print()
my_dictionary= {"name":"John",
                "age":30,
                "city":"New York",
                "country":"USA"
                }
for key,value in my_dictionary.items():
    print(f"{key}:{value}")
print()
for key in my_dictionary:
    print(key,end=" ")
print()
for value in my_dictionary.values():
    print(value, end=" ")
print()
for key in my_dictionary.keys():
    print(key,end=" ")
    
