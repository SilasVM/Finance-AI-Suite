"""
Created on November 25th, 2025

Stochastic Investment Game

Stock Market Navigation in Certain and Stochastic Market State

@author: V_Morgan
"""

import random
import time

class InvestmentGame:
    marketStates = ["Bullish", "Bearish", "Volatile"]
    principalInvestment = 150
    desired_increase = 1.75
    
    def CertainMarket_Investment(self):
        principal = self.principalInvestment
        balance = principal
        target = principal * self.desired_increase
        rounds = 0

        print("\n Welcome to the Stochastic Investment Game!")
        print("Before you begin your role as financial advisor you must display your competency by completing this game")
        print("Your task: Double your 'Principal Investment'.")
        print("Your investment choice each round reflects your strategy and the risk you're taking.")
        print(f"Your principal investment is $", principal, f", your target is $", target)

        while balance < target:
            print("\nThe market is in a stable state of growth. Choose where to invest wisely.")
            choice = input("1 = Bonds(low risk), 2 = Index Fund(medium risk), 3 = Tech Stock(high risk)")
            while choice not in ["1", "2", "3"]:
                choice = input("Invalid choice. Enter 1, 2, or 3: ")
                
            if choice == "1":
                rate = random.uniform(0.03, 0.06)
            elif choice == "2":
                rate = random.uniform(0.08, 0.15)
            elif choice == "3":
                rate = random.uniform(0.15, 0.25)

        
            gain = balance * rate
            balance += gain

            print(f"Your investment options have given you an increase of {rate*100:.2f}% for a gain of ${gain:.2f}")
            print(f"Your new balance is ${balance:.2f}")
            
            rounds += 1

        print(f"You've reached your target in", rounds, "rounds!")
        print(f"Your final balance was ${balance:.2f}. Congratulations!")

    def UncertainMarket_Investment(self):
        print("\n Advanced Level: The market state changes unpredictably every rounds!")
        print("In this level the stock market state changes, and the way the different stock categories grow changes.")
        print("This represents real-world volatility, like economic shocks or new policies.\n")
        
        principal = self.principalInvestment
        balance = principal
        target = principal * 1.5
        rounds = 0
        marketStates = self.marketStates

        while balance < target:
            print(f"Your current balance is ${balance:.2f}.")

            state = random.choice(marketStates)
            print("The Market state may have changed. Invest Wisely\n")
            choice = input("1 = Bonds(low risk), 2 = Index Fund(medium risk), 3 = Tech Stock(high risk)") 
            
            while choice not in ["1", "2", "3"]:
                choice = input("Invalid choice. Enter 1, 2, or 3: ")

            if choice == "1":
                baseRate = random.uniform(0.03, 0.06)
            elif choice == "2":
                baseRate = random.uniform(0.08, 0.15)
            elif choice == "3":
                baseRate = random.uniform(0.15, 0.25)
                
            if state == "Bullish":
                rate = baseRate * 1.2
            elif state == "Bearish":
                rate = -random.uniform(0.03, baseRate)
            elif state == "Volatile":
                rate = random.uniform(-.5*baseRate, 1.5*baseRate)
                
            gain = balance * rate
            balance += gain
            rounds += 1
            
            print(f"The Market was in a {state} state this round.\n")
            print(f"Your investment options have given you an increase of {rate*100:.2f}% for a gain of ${gain:.2f}")
            print(f"Your new balance is ${balance:.2f}")    
            
        print(f"You've reached your target in", rounds, "rounds!")
        print(f"Your final balance was ${balance:.2f}. Congratulations!")          

# -------------------------- Drive the game --------------------------
handle = InvestmentGame()

print("Stochastic Game for Decision Making Under Uncertainty\n")
t1 = time.time()

print(" BASIC GAME: Relatively Stable Environment ")
handle.CertainMarket_Investment()

print("\n ADVANCED GAME: Dynamic and Uncertain Society ")
handle.UncertainMarket_Investment()