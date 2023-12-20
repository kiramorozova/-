config = "switchport trunk allowed vlan 1,3,10,20,30,100".split()
result = list(config [-1].split(','))
print(result)