"""
Created November 20th

Chess Playing AI Agent

@author: V_Morgan
"""

#!pip install chess

import chess
import random
import time

state_space = chess.Board()
state_space
print(state_space)

#Checks Game Status and prints it. Returns value used to break loop if user ends game with their move
def check_game_status(board):
    if board.is_checkmate():
        print("Checkmate detected! Won!!")
        print("Game over:", board.result())
        return True
    elif board.is_stalemate():
        print("Stalemate detected! Draw!!")
        print("Results = ", board.result())
        return True
    elif board.is_insufficient_material():
        print("Draw! insufficient material.")
        print("Results = ", board.result())
        return True
    elif board.is_check():
        print("Check! The Agent's king is under attack!")
    elif board.is_game_over():
        print("Game over for a different reason.")
        print("Game over:", board.result())
        return True
    else:
        print("Game is still ongoing.")
        print("Results = ", board.result())
        return False

#Checks if a move results in checkmate before reporting it back to the agent as an option
def check_checkmate(board, move):
    copy = board.copy()
    copy.push(move)
    return copy.is_checkmate() 

#Checks for defensive moves and gives the agent a list of its options
def defence_moves(board, move):
    copy = board.copy()
    copy.push(move) 
    
    piece = copy.piece_at(move.to_square)
    if piece is None:
        return False 
        
    defenders = copy.attackers(copy.turn, move.to_square)
    return len(defenders) > 0

#Chooses from multiple sets of move options with priorities in the order they appear
def perform_ai_move(board):
    legal_moves = list(board.legal_moves)

    
    checkmate_moves = [m for m in legal_moves if check_checkmate(board, m)]
    if len(checkmate_moves) > 0:
        print("Agent has performed a Checkmate and won!")
        return random.choice(checkmate_moves)

    captures = [m for m in legal_moves if board.is_capture(m)]
    if len(captures) > 0:
        print("Agent performs a Capture")
        return random.choice(captures)
    
    checks = [m for m in legal_moves if board.gives_check(m)]    
    if len(checks) > 0:
        print("Agent performs Check!")
        return random.choice(checks)
    
    defending_moves = [m for m in legal_moves if defence_moves(board, m)]
    if len(defending_moves) > 0:
        print("Agent plays defence")
        return random.choice(defending_moves)
        
    promotions = [m for m in legal_moves if m.promotion in( chess.QUEEN, chess.KNIGHT)]
    if len(promotions) > 0:
        print("Agent promotes a pawn")
        return random.choice(promotions)

    return random.choice(legal_moves)

    
while not state_space.is_game_over():

    #Requesting the user, white, to make their move first
    while True:
        move = input("Enter Your Move: ")
        if chess.Move.from_uci(move) in list(state_space.legal_moves):
            break
        else:
            print("Invalid move. Try again.")    
    state_space.push(chess.Move.from_uci(move))
    print(state_space)

    if check_game_status(state_space):
        break
    
    #Selecting and carrying out the agents move
    move = perform_ai_move(state_space)
    state_space.push(move)
    print(state_space)
    
    time.sleep(2)

print("Final Result:", state_space.result())

print("\n Move History (in iternal UCI notation)")
print(state_space.move_stack)