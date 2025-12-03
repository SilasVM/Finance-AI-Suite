"""
Model-based recommender Agent

This agent recommends diverse stocks to purchase based on the users preferences. It reads in the stocks from a csv file and 
refines it to a list of stocks that fit the user's budget, industry, and risk preferences.

Created on 10/05/25

@author: V_Morgan
"""

import pandas as pd

class ModelBased_RecommenderAgent:
    
    total_Price = 0.0

    #load csv file
    def load_products(self, csv_file_path):
        print("Load Stock Listings \n")        

        #Building our dataframe and loading all of the stock data into it
        df = pd.read_csv(csv_file_path, encoding="ISO-8859-1")
        
        self.df = df
        
        print(df.head())

    #take in user preferences
    def add_preference(self):
        risks = ['low', 'medium', 'high']
        countries = ['USA', 'UK', 'Japan', 'Canada', 'Germany', 'India', 'China']
        
        print('\n Please enter your preferences to see your stock options \n')
        
        while True:
                pref_country = str(input("Country: USA, UK, Japan, Canada, Germany, India, China : ")).strip().lower()
                if pref_country in countries:
                    self.pref_country = pref_country
                    break
                else:
                    print("Invalid country. Please enter a listed country.")
        while True:
                try:
                    pref_budget = int(input("\n Budget: $ "))
                    break
                except ValueError:
                    print("Invalid Input! Please enter a number.")
        pref_industry = str(input("Industry: Automotive, Finance, Healthcare, Energy, Entertainment, Technology, Retail, Telecommunications : "))
        while True:
                pref_risk = str(input("Risk: Low, Medium, High : ")).strip().lower()
                if pref_risk in risks:
                    self.pref_risk = pref_risk
                    break
                else:
                    print("Invalid risk level. Please enter low, medium, or high.")
        #store preferences in global variables
        self.pref_budget = pref_budget
        self.pref_industry = pref_industry            
        
    def recommend_product(self):
        print("\n Product Recommendation Based on your Preferences")        

        #Bringing preferences into class function locally
        pref_country = self.pref_country
        pref_budget = self.pref_budget
        pref_industry = self.pref_industry
        pref_risk = self.pref_risk
        df = self.df       

        #Created a second dataframe with items that only match the user preference
        filtered_df = df[(df['Country'].str.lower() == pref_country.lower()) & (df['PricePerUnit'] < pref_budget) & (df['Industry'].str.lower() == pref_industry.lower()) & (df['RiskLevel'].str.lower() == pref_risk.lower())]

        
        cumulative_budget = 0.0
        displayed_rows = []

        #Reduces filtered_df and stores it in displayed_rows to ensure the rows displayed fit within the budget.
        for index, row in filtered_df.iterrows():
            cumulative_budget = cumulative_budget + row['PricePerUnit']
            if cumulative_budget <= pref_budget:
                displayed_rows.append(row)
                self.total_Price += row['PricePerUnit']
            else:
                break        
        
        recommended_prods = pd.DataFrame(displayed_rows)

        #Makes sure user results weren't null. Notifies users if so
        if not displayed_rows:
            print("No stocks found matching your preferences and budget. Please try another query\n")
            return
        else: 
            print(recommended_prods)
            print("The total price of this query is: ", recommended_prods['PricePerUnit'].sum())
            print("Your remaining budget for this query is: ", self.pref_budget - recommended_prods['PricePerUnit'].sum())
                            
            
                        
#----------------------------Class Driver --------------------------------------    
agent = ModelBased_RecommenderAgent()

# Agent designed as semi-autonomous 
print("MODEL-BASED AGENT: STOCK RECOMMENDER SYSTEM")
csv_file_path = 'apps/assn4/stock.csv'

agent.load_products(csv_file_path)
while True:
    agent.add_preference()
    
    agent.recommend_product()
    print(f"\nYour total price for all queries is: ${agent.total_Price:.2f}")
    #Allowing the user to generate more values. This will delete previous values permanently
    n = input("\n Press Enter-key to continue or enter 'q' to Quit: ")
    if n.strip().lower() == 'q':
        print("Please be safe in the environment...")
        break