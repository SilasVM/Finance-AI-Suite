"""
Created on Nov 13th 2025

@author: V_Morgan

Education: Financial Investement Information and

Modification Goals:
Race Cryptocurrency, Bonds, and Stocks, displaying the risk and reward comparisons of the three.
Modularize set of actions into for dynamic calling and code reduction.
Have each investement option race one at a time, from the same starting position, and display as a manual stock chart
"""

import turtle
import random
import time

screen = turtle.Screen()
screen.title("Investment Comparisons: Stocks, Bonds, and Crypto")
screen.bgcolor("black")

class InvestComparisonGame:
    def setup_race(self):
        
        #Create and hide template turtle
        turtle.Turtle().hideturtle()
        Template_turtle = turtle.Turtle()
        Template_turtle.hideturtle()
        Template_turtle.penup()

        
        #Create 3 turtles to represent 3 investment options
        Stock_rep = Template_turtle.clone()
        Bond_rep = Template_turtle.clone()
        Crypto_rep = Template_turtle.clone()

        #Create Graph Turtles to form graph
        X_marker = Template_turtle.clone()
        X_marker.speed(5)
        X_marker.color("white", "white")
        X_marker.shape("classic")
        X_marker.showturtle()
        X_marker.goto(-376,0)
        X_marker.pendown()
        X_marker.goto(372,0)
        X_marker.hideturtle()
        X_marker.penup()
        X_marker.goto(-480,-10)
        X_marker.write("Time / Investment Period", align="center", font=("Arial", 12, "bold"))
        

        Y_marker = Template_turtle.clone()
        Y_marker.speed(5)
        Y_marker.color("white", "white")
        Y_marker.shape("classic")
        Y_marker.showturtle()
        Y_marker.left(90)
        Y_marker.goto(372,-376)
        Y_marker.pendown()
        Y_marker.goto(372,376)
        Y_marker.write("Value (Returns/Loss)", align="center", font=("Arial", 12, "bold"))
        Y_marker.hideturtle()
        
        #Set up racer properties
        Stock_rep.speed(1)
        Stock_rep.color("green", "green")
        Stock_rep.shape("turtle")

        Bond_rep.speed(1)
        Bond_rep.color("red", "red")
        Bond_rep.shape("arrow")

        Crypto_rep.speed(1)
        Crypto_rep.color("yellow", "yellow")
        Crypto_rep.shape("classic")
        
        racers = [("Stock", Stock_rep, "Smart Investments, steady gains!"), ("Bond", Bond_rep, "Slow and Steady wins the race!"), ("Crypto", Crypto_rep, "High Risk! High Reward!!")]

        highest_y = -float('inf')
        highest_invest = None
        
        #Running Racers
        for name, racer, slogan in racers:
            self.start_race(name, racer)
            y = racer.ycor()
            if y > highest_y:
                highest_y = y
                highest_invest = name

        #printing winner
        for name, racer, slogan in racers:
            if name == highest_invest:
                racer.goto(0, 283)
                racer.write(f"{name} did the best!", align = "center", font=("Arial", 12, "bold"))
                racer.goto(0, 273)
                time.sleep(3)
                racer.goto(0, 243)
                racer.write(f"Remember: {slogan}", align = "center", font=("Arial", 12, "bold"))
                racer.goto(0, 233)


        X_marker.goto
        
        turtle.done()
        
    #Handling each racer and starting their race
    def start_race(self, investType, turtleRacer):
        
        turtleRacer.showturtle()
        turtleRacer.goto(-376, 0)
        turtleRacer.pendown()
        finish_line = 372

        #Dynamic Variables depending on investment type
        time_range = (10,50)
        angle_range = (30, -30)
       
        if investType == "Stock":
            time_range = (20,100)
            angle_range = (-30, 60)
        elif investType == "Bond":
            time_range = (10,20)
            angle_range = (-5, 15)
        elif investType == "Crypto":
            time_range = (20,50)
            angle_range = (-45, 45)

        #Beginning race for each investment type
        while turtleRacer.xcor() < finish_line:
            time_passed = random.randint(time_range[0], time_range[1])
            angle = random.randint(angle_range[0], angle_range[1])
            turtleRacer.setheading(angle)
            #making sure each marker doesn't go past x-372
            remaining = finish_line - turtleRacer.xcor() + 1
            step = min(time_passed, remaining)
            
            turtleRacer.forward(step)
            turtle.update()
            
        #Labelling each racer
        turtleRacer.penup()
        turtleRacer.goto(finish_line + 40, turtleRacer.ycor() + (turtleRacer.ycor()/15))
        turtleRacer.write(f"{investType}", align = "center", font=("Arial", 12, "bold"))
        turtleRacer.goto(turtleRacer.xcor(), turtleRacer.ycor()-10)


# -----------Driving the class -----------------------------------
handle = InvestComparisonGame()

handle.setup_race()
