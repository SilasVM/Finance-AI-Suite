"""
Loan Acceptance Reflex Agent

Created Sept, 2025

@author: V_Morgan
"""

import sqlite3
import random
import time
import names


class SimpleReflexAgent:
    #If their score is between 700 and 750 income must be considered
    LOW_THRESHOLD = 700
    #Passing income is used if user lies within the threshold. Income(in thousands) will then be used to consider acceptance
    INCOME_PASSING = 87
    GOOD_THRESHOLD = 750

    #moved from environment function to class variable for more global use.
    delay_seconds = 2
    
    def environment(self):                         
        self.temp_Data_Generator()                            
        
        rows = self.rows
        
        #Using perception function to select each entry and determine how the system will act on the environment
        for temp_id, tempName, tempScore in rows:
            self.perception_decision(tempName, tempScore)       
            time.sleep(self.delay_seconds)
         
    #Creation of the database
    def temp_Data_Generator(self):        
        
        #Opening connection to database or creating it if not already created
        conn = sqlite3.connect("LAagentDB")

        #Creating the database table if it doesn't already exist. Added space for name
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS temp_table
                        (temp_id INTEGER, tempName TEXT, tempScore REAL)''')       

        #Clearing the table. This executes regardless of if the table was just created or not
        #Empty table
        cur.execute("DELETE FROM temp_table")
        conn.commit()

        #Generating 20 random, realistic names and credit scores, then storing them in the table.
        for i in range(20):
            temp_value = random.randint(500, 850)
            temp_name = names.get_full_name()
            cur.execute('''INSERT INTO temp_table (temp_id, tempName, tempScore) VALUES (?, ?, ?)''', (i, temp_name, temp_value))
        conn.commit()               
        
        #Pulling elements from the table 
        cur.execute("SELECT * FROM temp_table")
        
        rows = cur.fetchall()
        self.rows = rows        

        #Closing connection to database
        cur.close()
        conn.close()

    def perception_decision(self, name, score):                
        income = 0
        print(f"\n Current user = {name}")
        print(f"\n Credit Score = {score}")

        #Declines loan if credit score is too low
        if score < self.LOW_THRESHOLD:
            print("Credit score is unacceptable. Cease loan agreement.")
        #Accepts loan request if credit score is high enough. 
        elif score > self.GOOD_THRESHOLD:
            print("Credit score is acceptable. Proceed with loan agreement forms.")
        # """Creates condition where income must be considered to determin if the loan will be accepted or not. Agent requesting more information on environment.
        else:
            print("Credit score near acceptable range, however, income must be considered.")
            #Elevated resilience when requesting the customer income
            while True:
                try:
                    income = int(input("\n Enter the users yearly income (in thousands) to determine their acceptance: "))
                    break
                except ValueError:
                    print("Invalid Input! Please enter a number.")
            #income = int(x)
            if income >= self.INCOME_PASSING:
                print("This customer meets the loan qualifications. Proceed with loan agreement forms.")
            else:
                time.sleep(self.delay_seconds)
                print("This customer does not meet the loan qualifications. Cease loan agreement.")
            time.sleep(self.delay_seconds)




#----------------------------Class Driver --------------------------------------    
agent = SimpleReflexAgent()

# Agent designed as semi-autonomous 
print("SIMPLE REFLEX AGENT - PERCEIVING & ACTING ON CUSTOMER CREDIT SCORE")
while True:    
    agent.environment()

    #Allowing the user to generate more values. This will delete previous values permanently
    n = input("\n Press Enter-key to continue or enter 'q' to Quit: ")
    if n.strip().lower() == 'q':
        print("Please be safe in the environment...")
        break