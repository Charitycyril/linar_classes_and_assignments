def tricky_list(lst):
    return lst[:-1] and lst[:-2] \
    if len(lst[1]) == len(lst[-1]) \
else lst[1:]

names= ["ben", "ken", "len"]
print(tricky_list(names))