sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]

dict={
    keys[0]:sample_dict[keys[0]],
    keys[1]:sample_dict[keys[1]]
}
print(dict);