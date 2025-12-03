"""
Expert System: AI Thinking humanly through financial advising

Created Aug 21, 2025

@author: V_Morgan
"""


class Finances_Expert_System:
    
    def user_interface(self):        
        intro = """
        Welcome to Investment Advisor Expert System.
        Our cutting edge technology will help you find the investment account that best fits you
        """
        print(intro)        
                
        main_menu = """
                    0. Quit
                    1. KNOWLEDGE ACQUISITION.
                    2. Investment Recommendation.
                    """
        
        while True:
            print("\n Advising Main Menu:")
            print(main_menu)
            
            try:
                num = int(input("Reply with the relevant option (1-2) to continue or 0 to Quit: "))   
                if num == 0:
                    print("Goodbye! Stay safe online")
                    break
                if num == 1:
                    self.acquire_knowledge()
                elif num == 2:
                    self.expert_system()      
                else:
                    print("Oops! Incorrect option, try again!")
            except ValueError:
                print("Please enter a number.")

    def acquire_knowledge(self):
        ack = """
        Investing is a good practice to start at any age.
        Different factors, like age and income, can help you decide which type of account is best for you.
        """
        print(ack)
        
    def expert_system(self):
        print("\n Welcome to EXPERT SYSTEM section")    
        
        print('\n W H A T    A R E    Y O U  R    F I N A N C I A L    C O N S I D E R A T I O N S:?')
        observations = """
        'Age 18-35', 'Income less than 146k', 'Income 146k-161k', 'More tax in retirement', 'Comfortable contributing after tax dollars',
        'Age 30-55', 'Income less than 77k', 'Income 77k-87k', 'Less tax in retirement', 'Prefer upfront tax savings',
        'Age 22-65', 'Income above 161k', 'Employer matching', 'No income limit', 'Prefer payroll deduction', 'Income less than 100k',
        'Lower taxes now', 'Lower taxes later', 'income less than 100k', 'Tax free growth'
        """
        print(observations)
        
        print("\n Enter your financial considerations (comma-separated):")
        patient_input = input().lower().split(',')
        factors = [factor.strip() for factor in patient_input]
                        
        self.factors = factors
        self.knowledge_base()
        self.diagnose_inference(factors)       
    
    def knowledge_base(self):
        knowledge_db = {
            'Roth IRA': [
                'age 18-35',
                'income less than 146k',
                'income 146k-161k',
                'income less than 100k',
                'more tax in retirement',
                'comfortable contributing after tax dollars',
                'lower taxes later',
                'tax free growth'
                ],
            'Traditional IRA': [
                'age 30-55',
                'income less than 77k',
                'income 77-87k',
                'income less than 100k',
                'less tax in retirement',
                'prefer upfront tax savings',
                'lower taxes now'
                ],
            '401(k)': [
                'age 22-65',
                'income above 161k',
                'employer matching',
                'no income limit',
                'prefer payroll deduction',
                'lower taxes now'
                ]
        }
        self.knowledge_db = knowledge_db
        
    def diagnose_inference(self, factors):
        knowledge_db = self.knowledge_db

        account_scores = {account: 0 for account in knowledge_db}
        
        # Ruled-based Inference
        possible_accounts = [] 
        for account, account_factors in self.knowledge_db.items():
            factors_lower = [f.lower() for f in account_factors]
            for user_input in factors:
                for factor in factors_lower:
                    if user_input in factor:
                        account_scores[account] +=1
                        break
        
        ranked_accounts = []
        remaining_accounts = account_scores.copy()


        
        while remaining_accounts:

            max_account = max(remaining_accounts, key = remaining_accounts.get)
            max_score = remaining_accounts[max_account]

            if max_score == 0:
                break

            ranked_accounts.append((max_account, max_score))
            del remaining_accounts[max_account]
        
        self.possible_accounts = ranked_accounts
        self.explanation()

    def explanation(self):        
        possible_accounts = self.possible_accounts 
        factors = self.factors            
        
        if possible_accounts:
            accounts_formatted = [f"{account} ({score} match(es))"
                                  for account, score in possible_accounts]
            print('\n D I A G N O S I S   R E S U L T S')
            print("Best fitting account(s):","," .join(accounts_formatted))
            print("Contact your bank for more information about opening your account")
        else:
            print("None of our accounts match what you're looking for. Please see a teller for more help.")
            
            
            
    
    
   
#----------------------------Class Driver --------------------------------------
handle = Finances_Expert_System()

handle.user_interface()
