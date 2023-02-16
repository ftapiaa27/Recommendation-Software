from heapq import heappop, heappush
from ui import *
from data import *
from LinkedList import LinkedList



skill_names = LinkedList()


class recommendation_system:
    def __init__(self):
        self.skills = LinkedList()
        self.current_skill = None

    def load_data(self):
        for key, value in calisthenics_skills.items():
            self.skills.insert_beginning([key, value])
            print(f"{key} added")
            print{f"{value}"}

    def get_skill(self):
        print("What calisthenics skill are you interested in?", 
        "Type the beggining of of the name and press enter to see if it's here:", sep = "\n")
        answer = input()
        answer = answer.lower()
        coincidences = []
        for skill in self.skills[0]:
            if skill:
                skill = skill.lower()
                if answer == skill[:len(answer)]:
                    coincidences.append(skill)
        if len(coincidences) == 0:
            print("No matches were found for " + answer)
            print("Try again: ")
            self.get_skill()
        elif len(coincidences) == 1:
            print("The only match for your search is {0}".format(coincidences[0]))
            continue_or_not = input("Do you want to continue with this skill?\n[Y or N]: ")
            if continue_or_not == "Y" or "y":
                self.get_choice_between_description_and_progressions(coincidences[0])
            else:
                self.get_skill()
        else:
            print("Here are the matches to your search: ")
            for match in coincidences:
                print(match)
            print("Try again: ")
            self.get_skill()

    def get_choice_between_description_and_progressions(self, skill):
        choice = int(input(f"What do you want to learn about the {skill}?\nDescription [1], or progressions [2]: "))
        if choice == 1:
            pass
        elif choice == 2:
            pass
        else:
            print("Please select a valid option.")
            self.get_choice_between_description_and_progressions()

    def show_description(self, name):
        skill = self.skills.get_node(name)
        print(skill[name][0])

    def main(self):
        welcome()
        self.get_skill()
        

cal_skills = recommendation_system()
cal_skills.load_data()
cal_skills.main()
    
