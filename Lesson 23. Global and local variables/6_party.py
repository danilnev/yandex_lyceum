def add_friends(name_of_person, list_of_friends):
    global friends
    if name_of_person not in friends:
        friends[name_of_person] = list_of_friends
    else:
        friends[name_of_person] += list_of_friends


def are_friends(name_of_person1, name_of_person2):
    global friends
    return name_of_person2 in friends[name_of_person1]


def print_friends(name_of_person):
    global friends
    friends_of_person = friends[name_of_person]
    friends_of_person.sort()
    print(' '.join(friends_of_person))


friends = dict()
# add_friends("Алла", ["Марина", "Иван"])
# print(are_friends("Алла", "Мария"))
# add_friends("Алла", ["Мария"])
# print(are_friends("Алла", "Мария"))

# add_friends("Катя", ["Женя", "Даша"])
# print(are_friends("Катя", "Филипп"))
# add_friends("Катя", ["Филипп"])
# print(are_friends("Катя", "Филипп"))
# print(are_friends("Катя", "Даша"))
