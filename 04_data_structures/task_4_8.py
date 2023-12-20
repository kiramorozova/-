ip = "192.168.3.1".split(".")
output = ""
for i in ip:
    output+= str(i) + str(" " * (8- len(str(i)))) + '  '
output += "\n"
for i in ip:
        output += str(format(int(i), "08b")) + '  '
print(output)