"""
Created November 9th

Finance Game-like Animation fully Autonomous

@author: V_Morgan
"""

from time import sleep
import os
import random
import threading

class FinanceAnimate:

    def setup_animate(self, delay, sleep):
        self.delay = delay
        self.sleep = sleep
        self.tips = []
        self.tipIndex = 0
        #Animation-like output
        self.finance_text = (
            "                                                            Fi",
            "                                                         Fin  ",
            "                                                       Fina   ",
            "                                                   Finan     ",
            "                                                Financ       ",
            "                                            Finance          ",
            "                                        Finance G            ",
            "                                   Finance Ga                ",
            "                               Finance Gam                   ",
            "                           Finance Game                      ",
            "                        Finance Game P                       ",
            "                     Finance Game Pl                         ",
            "                   Finance Game Pla                          ",
            "                 Finance Game Play                           ",
            "               Finance Game Playi                            ",
            "             Finance Game Playin                             ",
            "           Finance Game Playing                              ",
            "         Finance Game Playing                                ",
            "       Finance Game Playing                                  ",
            "    Finance Game Playing                                     ",
            "  Finance Game Playing                                       ",
            "nce Game Playing                                             ",
            "ce Game Playing                                              ",
            "e Game Playing                                               ",
            "Game Playing                                                 ",
            "me Playing                                                   ",
            "Playing                                                      ",
            "ng                                                           ",
            "ng                                                           ",
        )
        #List of finance-tips
        with open("Finance.txt", "r") as file:
            for line in file:
                cleaned = line.strip().strip('",')
                if cleaned:  # skip empty lines
                    self.tips.append(cleaned)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def animate_text(self):
        random.shuffle(self.tips)
        while True:
            print("\n Finance Awareness Animation \n")
            tip_index = self.tipIndex

            while tip_index < len(self.tips):
                self.clear_screen()
                for frame in self.finance_text:
                    print(frame)
                    #timer to make display animated(not all at once)
                    sleep(self.delay)

                print("\n Finance Awareness Message ")
                #Printing the tip at index value tip_index
                print(f"Tip {tip_index+1}: {self.tips[tip_index]}")
                print(f"\n Animation restarting in {self.sleep} seconds...\n")

                #wait n seconds
                sleep(self.sleep)
                #Incrementing tip_index to print next value when loop runs
                tip_index += 1

            self.get_input()
        
    def get_input(self, timeout = 10):
        user_input = [None]  # use a list to store input (mutable in inner scope)
        
        def input_thread():
            user_input[0] = input("Enter a new tip to be recorded to your file")
    
        thread = threading.Thread(target=input_thread)
        thread.start()
        thread.join(timeout)
    
        if thread.is_alive():
            print("\nNo input received in time.")
            return

        else:
            new_tip = user_input[0].strip()
            if new_tip:
                # Create Tip n string
                new_tip
    
                # Add to tips array
                self.tips.append(new_tip)
    
                # Append to file
                with open("Finance.txt", "a") as file:
                    file.write(f'{new_tip}\n')
                return




# ------------------ Driver Code ------------------
#Fully Autonomous
game = FinanceAnimate()

game.setup_animate(delay=0.25, sleep = 2)

game.animate_text()