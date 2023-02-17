from heapq import heappop, heappush
from ui import *
from data import *
from LinkedList import LinkedList



skill_names = LinkedList()

class recommendation_system:
    def __init__(self):
        self.skills = LinkedList()
    
    def load_data(self):
        for name, details in calisthenics_skills.items():
            self.skills.insert_beginning([name, details])
            print(f"{name} added")

    def get_skill(self):
        while True:
            print("What calisthenics skill are you interested in?", 
            "Type the beggining of of the name and press enter to see if it's here:",
            "(Or type 0 to exit)", sep = "\n")
            answer = input()
            if answer == "0":
                break
            answer = answer.lower()
            coincidences = []
            for skill in self.skills:
                if skill:
                    skill_name = skill[0].lower()
                    if answer == skill_name[:len(answer)]:
                        coincidences.append(skill)
            if len(coincidences) == 0:
                print("No matches were found for " + answer)
                print("Try again: ")
                self.get_skill()
            elif len(coincidences) == 1:
                print("The only match for your search is {0}".format(coincidences[0][0]))
                continue_or_not = input("Do you want to continue with this skill?\n[Y or N]: ")
                if continue_or_not.lower() == "y":
                    self.get_choice_between_description_and_progressions(coincidences[0])
                else:
                    continue
            else:
                print("Here are the matches to your search: ")
                for match in coincidences:
                    print(match[0])
                print("Try again: ")
                self.get_skill()

    def get_choice_between_description_and_progressions(self, skill):
        try:
            current_skill = skill.copy()
            choice = int(input(f"What do you want to learn about the {current_skill[0]}?\nDescription [1], progressions [2], exit[3]: "))
            if choice == 1:
                print(current_skill[1][0])
                self.get_choice_between_description_and_progressions(current_skill)
            elif choice == 2:
                while (True):
                    current_progression = heappop(current_skill[1][1])
                    print("Progression #{0}: {1}.\nDescription: {2}".format(current_progression[0], current_progression[1], current_progression[2]))
                    choice = int(input("Do you want to see the next progression [1] or exit to main menu [2]? "))
                    if choice == 1:
                        continue
                    elif choice == 2:
                        break
            elif choice == 3:
                exit
            else:
                print("Please select a valid option.")
                self.get_choice_between_description_and_progressions()
        except:
            print("There are no more progressions to display, returning to main menu")

    def main(self):
        welcome()
        self.get_skill()
        

cal_skills = recommendation_system()
cal_skills.load_data()
cal_skills.main()
    
