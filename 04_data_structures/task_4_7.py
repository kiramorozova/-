mac  = "AAAA:BBBB:CCCC"
numbers = "101010101010101010111011101110111100110011001100"
b_i_n = " ". join(format(int(x,16),"08b") for x in mac.split(":"))
print(b_i_n)
