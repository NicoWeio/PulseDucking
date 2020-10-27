import fileinput

foo = list()

for line in fileinput.input():
    foo.append(line)

print("DONE")
print(foo)
