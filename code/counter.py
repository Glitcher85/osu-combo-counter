import os, time, datetime
from keyboard import read_key

class Counter():
    def __init__(self):
        self.first_key = None
        self.second_key = None
        
    def check_for_keybinds(self):
        if self.first_key and self.second_key: return self.get_limitation()
        else: return self.get_keybinds()

    def get_keybinds(self):
        print("What is your first keybind?")
        self.first_key = read_key(); print(self.first_key); time.sleep(0.5)
        print("What is your second keybind?")
        self.second_key = read_key(); print(self.second_key); time.sleep(0.5)
        input("|| Press [ENTER] to proceed forward ||"); os.system("cls")
        return self.get_limitation()

    def get_limitation(self):
        limit = input("[NOTE]: Any buttons pressed other than the specified keybinds won't be counted.\nHow many combos do you want to stream?\n>")
        if self.check_for_valid_number(limit):
            return self.start(int(limit))
        else:
            input("Please enter a valid number.\n")
            return self.get_limitation()

    def check_for_valid_number(self, limit):
        try: int(limit)
        except: return False
        return True

    def start(self, limit:int):
        os.system("cls")
        limit = limit
        print("3..."); time.sleep(0.6)
        print("2..."); time.sleep(0.6)
        print("1..."); time.sleep(0.6)
        print("Start!")
        start_date = datetime.datetime.now()
        while limit:
            key = read_key()
            if self.first_key == key or self.second_key == key:
                limit -=1
                time.sleep(0.05)
        end_date = datetime.datetime.now()
        start_date = start_date.hour*3600 + start_date.minute*60 + start_date.second; end_date = end_date.hour*3600 + end_date.minute*60 + end_date.second
        delta_time = end_date - start_date; delta_time_minute = delta_time // 60; delta_time_second = delta_time % 60
        print(f"Your stream lasted {delta_time_minute} minutes and {delta_time_second} seconds.")
        time.sleep(3); input("|| Press [ENTER] to proceed forward ||"); os.system("cls")
        restart_consent = input("Do you want to restart?(y/n)\n>")
        if restart_consent == "y" or restart_consent == "yes":
            os.system("cls")
            return self.get_limitation()
        else: exit()
                
    def run(self):
        print("Osu combo counter by Hype Glitcher.")
        return self.check_for_keybinds()

if __name__ == "__main__":
    application = Counter()
    application.run()
        
            
        
