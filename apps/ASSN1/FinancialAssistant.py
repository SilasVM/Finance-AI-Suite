"""
Simon Virtual Bank Assistant

Perform Bank Transactions

Created on Saturday September 2025

@author: V_Morgan
"""

import pyttsx3
import pandas as pd
from datetime import datetime
from PyPDF2 import PdfReader

#reader = PdfReader("bankBook.pdf")

bot_talk = pyttsx3.init()

class BankingChatbot:
    def create_DFrame(self):
        self.df = pd.DataFrame.from_dict({
            "Account Type": ['Savings', 'Checkings', 'Savings', 'Checkings'],
            "Account Number": [1050, 2689, 4080, 4525],
            "Account Balance": [236, 4013, 173, 10375],
        })

    def deposit(self):
        try:
            accountNumber = int(input("Enter the account number for your deposit: "))
            amount = float(input("Enter the amount you're depositing: "))

            if accountNumber in self.df["Account Number"].values:
                self.df.loc[self.df["Account Number"] == accountNumber, "Account Balance"] += amount
                print("Deposit Compelete.")
            else:
                print("Account not found.")
        except invalidValue:
            print("Please enter a valid numbers")
    def withdraw(self):
        try:
            accountNumber = int(input("Enter the account number for your withdrawl: "))
            amount = float(input("Enter the amount you're withdrawing: "))
            currentBalance = self.df.loc[self.df["Account Number"] == accountNumber, "Account Balance"].iloc[0]
            
            if accountNumber in self.df["Account Number"].values:
                    if amount <= currentBalance:
                        self.df.loc[self.df["Account Number"] == accountNumber, "Account Balance"] -= amount
                        print("Withdrawl Compelete.")
                    else:
                        print("This transaction will result in an overdraft. Cancelling Transaction.")
            else:
                print("Account not found.")
        except ValueError:
            print("Please enter a valid numbers")
    def transfer(self):
        print("Transferring is currently unavailable")
    def view_checkings(self):
        checkings = self.df[self.df["Account Type"] == "Checkings"]
        print(checkings)
    def view_savings(self):
        savings = self.df[self.df["Account Type"] == "Savings"]
        print(savings)    
    def view_overall(self):
        balance = self.df["Account Balance"].sum()
        print("Your total balance accross accounts is:", balance)
    def initialize_bot(self):
        self.set_voice()
        self.create_DFrame()
        self.sections = {
            1: ("View Balances", {
                1: ("View a Checkings account Balance", self.view_checkings),
                2: ("View a Savings account Balance", self.view_savings),
                3: ("Receive Overall Balance across accounts", self.view_overall)
            }),
            2: ("Perform Transaction", {
                1: ("Deposit", self.deposit),
                2: ("Withdraw", self.withdraw),
                3: ("Transfer", self.transfer)
            })
        }
    def set_voice(self):
        voices = bot_talk.getProperty("voices")
        male_keywords = ["Simon", "Victor", "Jordan", "Matthew", "male"]

        for v in voices:
            if any(keyword in v.name.lower() for keyword in male_keywords):
                bot_talk.setProperty("voice", v.id)
                return

        bot_talk.setProperty("voice", voices[0].id)
        
    def speak(self, text):
        print(text)
        bot_talk.say(text)
        bot_talk.runAndWait()
    def sub_menu(self, main_choice):
        title, options = self.sections[main_choice]
        self.speak(f"You selected {title}. Please select a banking subtopic.")

        print("\nBanking Sub Menu:")
        for key, (subtitle, _) in options.items():
            print(f"{key}. {subtitle}")
        print("0. Go back")

        try:
            sub_choice = int(input("Choose: "))
            if sub_choice in options:
                subtitle, action = options[sub_choice]
                self.speak(f"Now responding to {subtitle}...")
            if callable(action):
                action()
            else:
                self.speak("Back to main menu.")
                return
        except ValueError:
            self.speak("Please enter a number.")
            
    def getTime(self):
        # Get the current time in a 24 hour format
        hour = datetime.now().hour
    
        if 5 <= hour < 12:
            return "Morning"
        elif 12 <= hour < 17:
            return "Afternoon"
        elif 17 <= hour < 21:
            return "Evening"
        else:
            return "Day"
            
    def main_menu(self):  
        time = self.getTime()
        
        if time == "Morning":
            self.speak("Good Morning I'm Simon, your virtual chat bot.")
        elif time == "Afternoon":
            self.speak("Good Afternoon I'm Simon, your virtual chat bot.")
        elif time == "Evening":
            self.speak("Good Evening I'm Simon, your virtual chat bot.")
        else:
            self.speak("Good Day I'm Simon, your virtual chat bot.")

        self.speak("I have simpler way to perform the transactions you'd like.")
        
        while True:
            print("\nBanking Main Menu:")
            for key, (title, _) in self.sections.items():
                print(f"{key}. {title}")
            print("0. Quit")

            try:
                main_choice = int(input("Choose (1-4) or 0 to Quit: "))
                if main_choice == 0:
                    self.speak("Goodbye! Stay safe online")
                    break
                if main_choice in self.sections:
                    self.sub_menu(main_choice)
                else:
                    self.speak("Invalid option.")
            except ValueError:
                self.speak("Please enter a number.")             
                
                
                
# ---------------------- Class Driver ----------------------
bot = BankingChatbot()
bot.initialize_bot()
bot.main_menu()