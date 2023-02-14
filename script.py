from heapq import heappop, heappush
from ui import *
from data import *
from LinkedList import LinkedList



skill_names = LinkedList()
for element in calisthenics_skills_list:
    skill_names.insert_beginning(element)


def get_skill():
    answer = input()
    answer = answer.lower()
    coincidences = []
    for skill in skill_names:
        if skill:
            skill = skill.lower()
            if answer in skill:
                coincidences.append(skill)
                print("Yeeha")
    if len(coincidences) == 0:
        print("No matches were found for " + answer)
        print("Try again: ")
        get_skill()
    else:
        return coincidences

def main():
    welcome()
    matches = get_skill()
    print("Here are the matches to your search: ")
    for match in matches:
        print(match)

main()
    
