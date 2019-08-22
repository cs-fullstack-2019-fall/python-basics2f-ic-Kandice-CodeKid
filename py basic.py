import random
# practice: random and f-string
name_list =['james', 'joe', 'clark', 'mark']

# random_number = random.randint(1, 10)
random_number= random.randint(0, len(name_list)-1)

# print(name_list[random_number])
# print(random_number)

# Can use with arrays/lists

rand_people=random.sample(name_list, 2)
print(rand_people)
