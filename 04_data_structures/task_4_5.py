command1 = "switchport trunk allowed vlan 1,2,3,5,8".split()
command2 = "switchport trunk allowed vlan 1,3,8,9".split()
s = command1[-1].split(",") 
v = command2[-1].split(",")
result = (set(s)&set(v))
print(result)