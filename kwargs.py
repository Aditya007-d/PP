# Keyworded variable length arguments

def person(name, **data):
    print(name)
    print(data)
    for i, j in data.items():
        print(i, j)


person("Aditya", Age = 24, City = "Mumbai", ph = 9945678212  )