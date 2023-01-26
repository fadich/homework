#ex2
pet_1 = "dogs"
pet_2 = "cats"
pet_3 = "fish"
pet_4 = "birds"
pets_all = "my pets"
#"Neither dogs, nor cats, nor fish, nor parrots allowed!"
print("Neither " + pet_1, pet_2, pet_3, pet_4, sep = ", nor ", end = ' allowed!\n')

#where are my dogs... where are my cats... where are my fish... where are my birds?!
print("" + pets_all, pet_1, pet_2, pet_3, pet_4, sep = "... where are my ", end = '?!\n')

#Here's all my pets: my wonderful dogs, my wonderful cats, my wonderful fish, my wonderful birds...
print("Here's all " + pets_all + ": " + pet_1, pet_2, pet_3, pet_4, sep = ",", end = '...\n')

#ex3
line_one = "#" * 9
line_two = "#" + " "*7 + "#"
print(line_one, line_two, line_two, line_two, line_one, sep = "\n", end = "\n")
print(line_two, line_two, line_one, line_two, line_two, sep = "\n", end = "\n")

#питання по цьому рішенню: змінна умовно містить дію (конкатенацію стрінги?), чи не буде кожен раз,
#коли ця зміна викликається, цей процес виконуватися заново і таким чином перевантажувати пам'ять?
#є якесь "елегантніше" рішення, чи присвоєння конкатенації стрінги у змінну - це ок?