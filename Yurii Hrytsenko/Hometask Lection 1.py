# Hometask Lection 3
# Task 3

full_str = "#"*9 + "\n"
empty_str = "#" + "\t"*2 + "#" + "\n"

big_o = full_str + (empty_str )*3 + full_str
big_h = (empty_str )*2 + full_str + (empty_str)*2

print(big_o)
print(big_h)