"""
Learning Agent using KNN Regressor

Created on 13th Oct 2025

@author: V_Morgan
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

label_encoder = LabelEncoder()

class LearningAgent_kNNregressor:
    
    #Creating multiple encoder labels for the handful of variables that need encoding. Makes for easier expansion
    encoders = {}
    categorical_cols = ['Manufacturer', 'Model', 'Category', 'LeatherInterior', 'FuelType', 'EngineVolume', 'GearBoxType', 'DriveWheels', 'Wheel', 'Color']
    
    def load_data(self, file_path):
        
        df = pd.read_csv(file_path)
        self.df = df
        
        print(df.head().to_string(index=True))
        
        print('\n Data Size = ', df.shape)
        
        print(df.describe())
        
        
    def visualizeData_bef_modeling(self):   
        print('\n VISUALIZE DATA PATTERNS BEFORE MODELING')
        df = self.df                
        x = df['Mileage']
        y = df['Price']

        # Create a scatter plot
        plt.figure(figsize=(8, 6))
        plt.scatter(x, y, marker='o', color='red', alpha=0.5)
        plt.xlabel('Mileage')
        plt.ylabel('Price')
        plt.title('Scatter Plot: Mileage vs. Price')
        plt.show()        
        
    def data_preprocessing(self):
        df = self.df
        
        print('\n DATA ENCODING')
        for col in self.categorical_cols:
            self.encoders[col] = LabelEncoder()
            df[f'{col}_enc'] = self.encoders[col].fit_transform(df[col])         
                
        print(df.head().to_string(index=True))
        
        features = df[['Levy', 'Manufacturer_enc', 'Model_enc', 'ProdYear', 'Category_enc', 'LeatherInterior_enc', 'FuelType_enc', 'EngineVolume_enc', 'Mileage', 'Cylinders', 'GearBoxType_enc', 'DriveWheels_enc', 'Doors', 'Wheel_enc', 'Color_enc', 'Airbags']]
        target = df['Price']
        
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.1, random_state=42)
        
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        self.scaler = scaler
        
        self.df = df
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test    
        
        
    def train_agent_predict_test(self):   
        X_train = self.X_train
        y_train = self.y_train
        X_test = self.X_test
        
        kNN_learner = KNeighborsRegressor(n_neighbors=2)
        kNN_learner.fit(X_train, y_train)
                
        self.pred = kNN_learner.predict(X_test)                
        self.kNN_learner = kNN_learner
        
        
    def evaluate_KNN_agent(self):     
        print('\n PERFORMANCE EVALUATIONS')
        X_test = self.X_test
        y_test = self.y_test  
        pred_y = self.pred
        
        r2 = r2_score(y_test, pred_y)
        print("R-squared = ", r2)
        
        mse = mean_squared_error(y_test, pred_y)
        print("MSE = ", mse)                     
        
        # Visualize the predictions        
        plt.figure(figsize=(8, 6))
        plt.scatter(y_test, pred_y, alpha=0.6, color='green', label='Predictions')
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', label='Perfect Fit Line')
        plt.xlabel("True Price")
        plt.ylabel("Predicted Price")
        plt.title("True vs Predicted Car Price")
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.show()

    def predict_new_percept(self, Levy, Manufacturer, Model, ProdYear, Category, LeatherInterior, FuelType, EngineVolume, Mileage, Cylinders, GearBoxType, DriveWheels, Doors, Wheel, Color, Airbags): 
        Manufacturer_enc = self.encoders['Manufacturer'].transform([Manufacturer])[0]
        Model_enc = self.encoders['Model'].transform([Model])[0]
        Category_enc = self.encoders['Category'].transform([Category])[0]
        LeatherInterior_enc = self.encoders['LeatherInterior'].transform([LeatherInterior])[0]
        FuelType_enc = self.encoders['FuelType'].transform([FuelType])[0]
        EngineVolume_enc = self.encoders['EngineVolume'].transform([EngineVolume])[0]
        GearBoxType_enc = self.encoders['GearBoxType'].transform([GearBoxType])[0]
        DriveWheels_enc = self.encoders['DriveWheels'].transform([DriveWheels])[0]
        Wheel_enc = self.encoders['Wheel'].transform([Wheel])[0]
        Color_enc = self.encoders['Color'].transform([Color])[0]             

        input_data = {'Levy': Levy,
                      'Manufacturer_enc': Manufacturer_enc,
                      'Model_enc': Model_enc,
                      'ProdYear': ProdYear,
                      'Category_enc': Category_enc,
                      'LeatherInterior_enc': LeatherInterior_enc,
                      'FuelType_enc': FuelType_enc,
                      'EngineVolume_enc': EngineVolume_enc,
                      'Mileage': Mileage,
                      'Cylinders': Cylinders,
                      'GearBoxType_enc': GearBoxType_enc,
                      'DriveWheels_enc': DriveWheels_enc,
                      'Doors': Doors,
                      'Wheel_enc': Wheel_enc,
                      'Color_enc': Color_enc,
                      'Airbags': Airbags
        }

        new_input = pd.DataFrame([input_data])
        
        # Scale and predict
        new_scaled = self.scaler.transform(new_input)
        new_pred = self.kNN_learner.predict(new_scaled)                    
        
        print('\n Predicted Car Price = $', new_pred[0])

    #Function to take in and handle categorical inputs from the user
    def cat_input(self, prompt, column_name, transform=None):
        #creates a list of acceptable inputs from the user
        valid_values = list(self.df[column_name].unique())

        #Requests input from the user until they enter a valid input
        while True:
            value = input(prompt).strip().lower()
            #transforms the users input to match the data style. All caps, upper case, etc.
            if transform:
                value = transform(value)
            if value in valid_values:
                return value
            else:
                print(f"'{value}' not recognized. Valid options include: {valid_values[:2]} ...")
                    
def collect_int(prompt):
    while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please input an integer")
        
        
        
        
        
#----------------------------Class Driver --------------------------------------    
agent = LearningAgent_kNNregressor()

#Update from environment
file_path = 'apps/ASSN6/carPricePrediction.csv'

agent.load_data(file_path)

#agent.visualizeData_bef_modeling()

agent.data_preprocessing()

agent.train_agent_predict_test()

agent.evaluate_KNN_agent()

# Agent designed as semi-autonomous with promts or files 

print('PREDICT NEW INSTANCES')
while True:
    Levy = collect_int("Enter car Levy or 0: ")
    Mileage = collect_int("Enter the mileage: ")
    Cylinders = collect_int("Enter the cylinders: ")
    ProdYear = collect_int("Enter car production year: ")
    Airbags = collect_int("Enter number of airbags: ")
    Doors = collect_int("Enter the number of doors(2, 4, 5): ")
    
    Manufacturer = agent.cat_input("Enter car Manufacturer: ", 'Manufacturer', str.upper)
    Model = agent.cat_input("Enter car model: ", 'Model', str.capitalize)
    Category = agent.cat_input("Enter car category: ", 'Category', str.capitalize)
    LeatherInterior = agent.cat_input("Leather interior?('Yes' or 'No': ", 'LeatherInterior', str.capitalize)
    FuelType = agent.cat_input("Enter the fuel type: ", 'FuelType', str.capitalize)
    EngineVolume = agent.cat_input("Enter the engine volume: ", 'EngineVolume')
    GearBoxType = agent.cat_input("Enter the gear box type: ", 'GearBoxType', str.capitalize)
    DriveWheels = agent.cat_input("Enter car wheel drive type: ", 'DriveWheels', str.capitalize)
    Wheel = agent.cat_input("Enter wheel side(Left or Right): ", 'Wheel', str.capitalize)
    Color = agent.cat_input("Enter car color: ", 'Color', str.capitalize)

    agent.predict_new_percept(Levy, Manufacturer, Model, ProdYear, Category, LeatherInterior, FuelType, EngineVolume, Mileage, Cylinders, GearBoxType, DriveWheels, Doors, Wheel, Color, Airbags)  

    n = input("\n Please press Enter-key to continue or enter 'q' to Quit: ")
    if n.strip().lower() == 'q':
        break
