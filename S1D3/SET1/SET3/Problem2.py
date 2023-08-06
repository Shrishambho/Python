def add(dict, name, age):
    dict["name"] = name
    dict["age"] = age
    return dict

def delet(dict1, key):
    del dict1[key]
    return dict1

def up(dict,key,value):
    dict[key]=value;
    return dict;

dict_ = {}
print(dict_)

dict1 = add(dict_, "John", 25)
print(dict1)

dict2 = up(dict1, "John",26)
print(dict2)
