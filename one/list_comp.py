lst1 = [5, 6, 7, 8, 9]
dict_exmaple = {'Policja': 997, "Pizza": 384, "Mama": 567}

tup = tuple(lst1)
def kwadrat(lst):
    return [item ** 2 for item in lst]

def inver_dict(dict):
    return {v: k for k,v in dict.items()}


if __name__ == '__main__':
    print(lst1[0])
    print(lst1)
    print(tup)
    print(kwadrat(lst1))

    print(dict_exmaple.keys())
    print(dict_exmaple.values())
    print(dict_exmaple.items())
    print(dict_exmaple['Mama'])
    print(inver_dict(dict_exmaple))
