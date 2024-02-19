random_clown1 = {'name': 'Artur', 'age': 22, 'sex': 'male', 'city': 'Kharkov'}
random_clown1['job'] = 'Student'
print(random_clown1)
del random_clown1['sex']
print(random_clown1)
clown_name = random_clown1['name']
print(clown_name)
animal_sounds = {'dog': 'bark', 'cat': 'meow', 'cow': 'mooo', 'pig': 'oink-oink'}
cat_sound = animal_sounds['cat']
print(cat_sound)

random_clown1.update(animal_sounds)
print(random_clown1)
