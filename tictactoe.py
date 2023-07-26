places=("A1","A2","A3","B1","B2","B3","C1","C2","C3")
board = {"A1": " ", "A2": " ", "A3": " ",
         "B1": " ", "B2": " ", "B3": " ",
         "C1": " ", "C2": " ", "C3": " "}

def printboard():
    print(f" {board['A1']}   | {board['A2']}   | {board['A3']}")
    print("_____|_____|_____")
    print(f" {board['B1']}   | {board['B2']}   | {board['B3']}")
    print("_____|_____|_____")
    print(f" {board['C1']}   | {board['C2']}   | {board['C3']}")
    print("     |     |     ")

def check_win(player):
    return ((board['A1'] == board['A2'] == board['A3'] == player) or
            (board['B1'] == board['B2'] == board['B3'] == player) or
            (board['C1'] == board['C2'] == board['C3'] == player) or
            (board['A1'] == board['B1'] == board['C1'] == player) or
            (board['A2'] == board['B2'] == board['C2'] == player) or
            (board['A3'] == board['B3'] == board['C3'] == player) or
            (board['A1'] == board['B2'] == board['C3'] == player) or
            (board['A3'] == board['B2'] == board['C1'] == player))

while True:
    printboard()
    choice=input("Make your choice (A-C), (1-3)")
    

