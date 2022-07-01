# Python script for translating raw data from Board.cpp into PGN notation for chess analysis

import os
import time


def fileCheck(index, f2):
    if(index == '0' or index == '8' or index == '16' or index == '24' or index == '32' or index == '40' or index == '48' or index == '56'):
        f2.write("a")
    elif(index == '1' or index == '9' or index == '17' or index == '25' or index == '33' or index == '41' or index == '49' or index == '57'):
        f2.write("b")
    elif(index == '2' or index == '10' or index == '18' or index == '26' or index == '34' or index == '42' or index == '50' or index == '58'):
        f2.write("c")
    elif(index == '3' or index == '11' or index == '19' or index == '27' or index == '35' or index == '43' or index == '51' or index == '59'):
        f2.write("d")
    elif(index == '4' or index == '12' or index == '20' or index == '28' or index == '36' or index == '44' or index == '52' or index == '60'):
        f2.write("e")
    elif(index == '5' or index == '13' or index == '21' or index == '29' or index == '37' or index == '45' or index == '53' or index == '61'):
        f2.write("f")
    elif(index == '6' or index == '14' or index == '22' or index == '30' or index == '38' or index == '46' or index == '54' or index == '62'):
        f2.write("g")
    elif(index == '7' or index == '15' or index == '23' or index == '31' or index == '39' or index == '47' or index == '55' or index == '63'):
        f2.write("h")
    else:
        f2.write("ERR fileCheck")
        print("ERR fileCheck")


def rankCheck(index, f2):
    if(int(index) >= 0 and int(index) <= 7):
        f2.write("8")
    elif(int(index) >= 8 and int(index) <= 15):
        f2.write("7")
    elif(int(index) >= 16 and int(index) <= 23):
        f2.write("6")
    elif(int(index) >= 24 and int(index) <= 31):
        f2.write("5")
    elif(int(index) >= 32 and int(index) <= 39):
        f2.write("4")
    elif(int(index) >= 40 and int(index) <= 47):
        f2.write("3")
    elif(int(index) >= 48 and int(index) <= 55):
        f2.write("2")
    elif(int(index) >= 56 and int(index) <= 63):
        f2.write("1")
    else:
        f2.write("ERR rankCheck")
        print("ERR rankCheck")


def main():
    # file content
    # replace sample directory with game file directory
    file = open("Interpreter/sampleFiles/sample.txt", "r")
    print("File opened for reading\n")
    data = file.read()
    print("Data Collected:\n" + data + "\n")
    f2 = open("./Interpreter/Games/" +
              str(time.ctime(os.path.getctime(file.name)))+".pgn", "w")
    print("New file created:" + f2.name + "\n")
    file.close()

    f2.write("Game Timestamp: " +  # You can edit this section but leave the \n symbols for formatting purposes
             str(time.ctime(os.path.getctime(file.name))) + "\n")
    f2.write("White: \n")
    f2.write("Black: \n")
    f2.write("Special notes: \n\n\n")

    # init vars
    i = 0
    moveNum = 1
    board = [  # From white's perspective, edit this array to change initial board state
        2, 3, 4, 5, 6, 4, 3, 2,
        1, 1, 1, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 1,
        2, 3, 4, 5, 6, 4, 3, 2
    ]
    rawMoves = data.split(",")
    rawMoves.pop(len(rawMoves)-1)  # removes last empty element

    # main loop
    while i < (len(rawMoves)-1):
        take = False
        pawn = False
        enPassant = False

        if moveNum % 1 == 0:
            f2.write(str(int(moveNum))+". ")

        # Castling
        if(rawMoves[i] == '100'):
            f2.write("O-O ")
            if(moveNum % 1 == 0):
                board[60] = 0
                board[63] = 0
                board[62] = 3
                board[61] = 2
            else:
                board[4] = 0
                board[7] = 0
                board[6] = 3
                board[5] = 2
            i += 1
            moveNum += 0.5  # 0.5 increment differentiates between white/black for move printing
        elif(rawMoves[i] == "1000"):
            f2.write("O-O-O ")
            if(moveNum % 1 == 0):
                board[60] = 0
                board[56] = 0
                board[58] = 3
                board[59] = 2
            else:
                board[4] = 0
                board[0] = 0
                board[2] = 3
                board[3] = 2
            i += 1
            moveNum += 0.5
        else:
            # this check happens before increment to allow for inline board updates
            if (board[int(rawMoves[i+1])] != 0):
                take = True
            elif ((board[int(rawMoves[i])] == 1) and ((int(rawMoves[i])+8) != int(rawMoves[i+1])) and ((int(rawMoves[i])-8) != int(rawMoves[i+1])) and ((int(rawMoves[i])+16) != int(rawMoves[i+1])) and ((int(rawMoves[i])-16) != int(rawMoves[i+1])) and (board[int(rawMoves[i+1])] == 0)):
                enPassant = True
                take = True

            # Piece or Pawn
            if board[int(rawMoves[i])] == 1:
                pawn = True
                fileCheck(rawMoves[i], f2)
                board[int(rawMoves[i])] = 0
                board[int(rawMoves[i+1])] = 1
                if enPassant == True:
                    if int(rawMoves[i]) > int(rawMoves[i+1]):
                        board[int(rawMoves[i+1])+8] = 0
                    elif int(rawMoves[i]) < int(rawMoves[i+1]):
                        board[int(rawMoves[i+1])-8] = 0
            else:
                if(board[int(rawMoves[i])] == 2):
                    f2.write("R")
                    board[int(rawMoves[i])] = 0
                    board[int(rawMoves[i+1])] = 2
                elif(board[int(rawMoves[i])] == 3):
                    f2.write("N")
                    board[int(rawMoves[i])] = 0
                    board[int(rawMoves[i+1])] = 3
                elif(board[int(rawMoves[i])] == 4):
                    f2.write("B")
                    board[int(rawMoves[i])] = 0
                    board[int(rawMoves[i+1])] = 4
                elif(board[int(rawMoves[i])] == 5):
                    f2.write("Q")
                    board[int(rawMoves[i])] = 0
                    board[int(rawMoves[i+1])] = 5
                elif(board[int(rawMoves[i])] == 6):
                    f2.write("K")
                    board[int(rawMoves[i])] = 0
                    board[int(rawMoves[i+1])] = 6
                else:
                    f2.write("ERR pieceName")
                    print("ERR pieceName")

            # Extended PGN notation for cases with >1 same-name piece option
            if pawn == True:
                pass
            else:
                fileCheck(rawMoves[i], f2)
                rankCheck(rawMoves[i], f2)
            i += 1  # move to coord2 to find piece destination

            if take == True:
                f2.write("x")

            # destination
            if pawn == True and take == False:
                rankCheck(rawMoves[i], f2)
                f2.write(" ")
            else:
                fileCheck(rawMoves[i], f2)
                rankCheck(rawMoves[i], f2)
                f2.write(" ")
            i += 1  # progress to next move
            moveNum += 0.5
    f2.close()


main()
