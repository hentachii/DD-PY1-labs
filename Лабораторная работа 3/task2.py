# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator = ","):
    set1 = set(first_group.split(separator))
    set2 = set(second_group.split(separator))
    return sorted(set1 & set2)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


participants2 = find_common_participants(participants_first_group, participants_second_group, separator= "|")
print(participants2)

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group)
print(participants)








