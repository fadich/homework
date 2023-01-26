# LESSON_2

# Task 2:

# Just values
a = 'Gaia Project'
b = 'This War of Mine'
c = 'Alchemists'
d = 'Sagrada'
e = 'Bunny Kingdom'

# I love to play board games! 😁
print('I love to play board games!', '😁', sep=' ', end='\n')

# My favorite games are:
print('My favorite games are', end=':\n🌟')

# 🌟Gaia Project;
# 🌟This War of Mine;
# 🌟Alchemists;
# 🌟Sagrada;
# 🌟Bunny Kingdom.
print(a, b, c, d, e, sep=';\n🌟', end='.\n')

# And what are your favorites?
print('And what are your favorites', end='?🐍\n')



# Task 3:

hor_line = 9 * '#'
dots_line = '#\t#'.expandtabs()

print(hor_line + '\n' + 3 * (dots_line + '\n') + hor_line, '\n')
print(2 * (dots_line + '\n') + hor_line + '\n' + 2 * (dots_line + '\n'))