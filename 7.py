def generator(num):
    for el in (10, 20, 30):
        yield el

g = generator(20)
print(g)

for el in g:
    print(el)
