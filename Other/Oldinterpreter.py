# Replace sample directory with game file directory
file = open(
    "Interpreter/sample.txt", "r")
# file.write("\n\n\nPGN:\n")
print("File opened\n")

pgn = ""
i = 0
moveNum = 1
board = [
    2, 3, 4, 5, 6, 4, 3, 2,
    1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1, 1,
    2, 3, 4, 5, 6, 4, 3, 2
]
# Board indices
# board = [
#     0, 1, 2, 3, 4, 5, 6, 7,
#     8, 9, 10, 11, 12, 13, 14, 15,
#     16, 17, 18, 19, 20, 21, 22, 23,
#     24, 25, 26, 27, 28, 29, 30, 31,
#     32, 33, 34, 35, 36, 37, 38, 39,
#     40, 41, 42, 43, 44, 45, 46, 47,
#     48, 49, 50, 51, 52, 53, 54, 55,
#     56, 57, 58, 59, 60, 61, 62, 63
# ]
rawmoves = file.read().split(",")
rawmoves.pop(len(rawmoves)-1)  # Removes last empty element

print(rawmoves)
print()
while i < (len(rawmoves)-1):
    take = False
    pawnCheck = False

    if(moveNum % 1 == 0):
        pgn += (str(int(moveNum)) + ". ")

    if(rawmoves[i] == '100'):
        pgn += "O-O "
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
        moveNum += 0.5
    elif(rawmoves[i] == "1000"):
        pgn += "O-O-O "
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
        if (board[int(rawmoves[i+1])] != 0):
            take = True

        #pawn or piece
        # if pawn, need to decide which one it is (File designation)
        if(board[int(rawmoves[i])] == 1):
            pawnCheck = True
            if(rawmoves[i] == '0' or rawmoves[i] == '8' or rawmoves[i] == '16' or rawmoves[i] == '24' or rawmoves[i] == '32' or rawmoves[i] == '40' or rawmoves[i] == '48' or rawmoves[i] == '56'):
                pgn += "a"
            elif(rawmoves[i] == '1' or rawmoves[i] == '9' or rawmoves[i] == '17' or rawmoves[i] == '25' or rawmoves[i] == '33' or rawmoves[i] == '41' or rawmoves[i] == '49' or rawmoves[i] == '57'):
                pgn += "b"
            elif(rawmoves[i] == '2' or rawmoves[i] == '10' or rawmoves[i] == '18' or rawmoves[i] == '26' or rawmoves[i] == '34' or rawmoves[i] == '42' or rawmoves[i] == '50' or rawmoves[i] == '58'):
                pgn += "c"
            elif(rawmoves[i] == '3' or rawmoves[i] == '11' or rawmoves[i] == '19' or rawmoves[i] == '27' or rawmoves[i] == '35' or rawmoves[i] == '43' or rawmoves[i] == '51' or rawmoves[i] == '59'):
                pgn += "d"
            elif(rawmoves[i] == '4' or rawmoves[i] == '12' or rawmoves[i] == '20' or rawmoves[i] == '28' or rawmoves[i] == '36' or rawmoves[i] == '44' or rawmoves[i] == '52' or rawmoves[i] == '60'):
                pgn += "e"
            elif(rawmoves[i] == '5' or rawmoves[i] == '13' or rawmoves[i] == '21' or rawmoves[i] == '29' or rawmoves[i] == '37' or rawmoves[i] == '45' or rawmoves[i] == '53' or rawmoves[i] == '61'):
                pgn += "f"
            elif(rawmoves[i] == '6' or rawmoves[i] == '14' or rawmoves[i] == '22' or rawmoves[i] == '30' or rawmoves[i] == '38' or rawmoves[i] == '46' or rawmoves[i] == '54' or rawmoves[i] == '62'):
                pgn += "g"
            elif(rawmoves[i] == '7' or rawmoves[i] == '15' or rawmoves[i] == '23' or rawmoves[i] == '31' or rawmoves[i] == '39' or rawmoves[i] == '47' or rawmoves[i] == '55' or rawmoves[i] == '63'):
                pgn += "h"
            else:
                pgn += "ERR101!"
            board[int(rawmoves[i])] = 0
            board[int(rawmoves[i+1])] = 1
        else:
            if(board[int(rawmoves[i])] == 2):
                pgn += "R"
                board[int(rawmoves[i])] = 0
                board[int(rawmoves[i+1])] = 2
            elif(board[int(rawmoves[i])] == 3):
                pgn += "N"
                board[int(rawmoves[i])] = 0
                board[int(rawmoves[i+1])] = 3
            elif(board[int(rawmoves[i])] == 4):
                pgn += "B"
                board[int(rawmoves[i])] = 0
                board[int(rawmoves[i+1])] = 4
            elif(board[int(rawmoves[i])] == 5):
                pgn += "Q"
                board[int(rawmoves[i])] = 0
                board[int(rawmoves[i+1])] = 5
            elif(board[int(rawmoves[i])] == 6):
                pgn += "K"
                board[int(rawmoves[i])] = 0
                board[int(rawmoves[i+1])] = 6
            else:
                pgn += "ERR126!"

        # specify piece file and rank for cases with >1 option (yes the pgn interpreter accepts this)
        if (pawnCheck == True):
            pass
        else:
            if(rawmoves[i] == '0' or rawmoves[i] == '8' or rawmoves[i] == '16' or rawmoves[i] == '24' or rawmoves[i] == '32' or rawmoves[i] == '40' or rawmoves[i] == '48' or rawmoves[i] == '56'):
                pgn += "a"
            elif(rawmoves[i] == '1' or rawmoves[i] == '9' or rawmoves[i] == '17' or rawmoves[i] == '25' or rawmoves[i] == '33' or rawmoves[i] == '41' or rawmoves[i] == '49' or rawmoves[i] == '57'):
                pgn += "b"
            elif(rawmoves[i] == '2' or rawmoves[i] == '10' or rawmoves[i] == '18' or rawmoves[i] == '26' or rawmoves[i] == '34' or rawmoves[i] == '42' or rawmoves[i] == '50' or rawmoves[i] == '58'):
                pgn += "c"
            elif(rawmoves[i] == '3' or rawmoves[i] == '11' or rawmoves[i] == '19' or rawmoves[i] == '27' or rawmoves[i] == '35' or rawmoves[i] == '43' or rawmoves[i] == '51' or rawmoves[i] == '59'):
                pgn += "d"
            elif(rawmoves[i] == '4' or rawmoves[i] == '12' or rawmoves[i] == '20' or rawmoves[i] == '28' or rawmoves[i] == '36' or rawmoves[i] == '44' or rawmoves[i] == '52' or rawmoves[i] == '60'):
                pgn += "e"
            elif(rawmoves[i] == '5' or rawmoves[i] == '13' or rawmoves[i] == '21' or rawmoves[i] == '29' or rawmoves[i] == '37' or rawmoves[i] == '45' or rawmoves[i] == '53' or rawmoves[i] == '61'):
                pgn += "f"
            elif(rawmoves[i] == '6' or rawmoves[i] == '14' or rawmoves[i] == '22' or rawmoves[i] == '30' or rawmoves[i] == '38' or rawmoves[i] == '46' or rawmoves[i] == '54' or rawmoves[i] == '62'):
                pgn += "g"
            elif(rawmoves[i] == '7' or rawmoves[i] == '15' or rawmoves[i] == '23' or rawmoves[i] == '31' or rawmoves[i] == '39' or rawmoves[i] == '47' or rawmoves[i] == '55' or rawmoves[i] == '63'):
                pgn += "h"
            else:
                pgn += "ERR149!"

            if(int(rawmoves[i]) >= 0 and int(rawmoves[i]) <= 7):
                pgn += "8"
            elif(int(rawmoves[i]) >= 8 and int(rawmoves[i]) <= 15):
                pgn += "7"
            elif(int(rawmoves[i]) >= 16 and int(rawmoves[i]) <= 23):
                pgn += "6"
            elif(int(rawmoves[i]) >= 24 and int(rawmoves[i]) <= 31):
                pgn += "5"
            elif(int(rawmoves[i]) >= 32 and int(rawmoves[i]) <= 39):
                pgn += "4"
            elif(int(rawmoves[i]) >= 40 and int(rawmoves[i]) <= 47):
                pgn += "3"
            elif(int(rawmoves[i]) >= 48 and int(rawmoves[i]) <= 55):
                pgn += "2"
            elif(int(rawmoves[i]) >= 56 and int(rawmoves[i]) <= 63):
                pgn += "1"
            else:
                pgn += "ERR198!"
        i += 1  # Now that we know what piece, move to coord2 to know where it's going

        # is taking? (check occurs at top of Else)
        if(take == True):
            pgn += "x"

        # destination
        # File designation
        if(pawnCheck == True and take == False):
            pass
        else:
            if(rawmoves[i] == '0' or rawmoves[i] == '8' or rawmoves[i] == '16' or rawmoves[i] == '24' or rawmoves[i] == '32' or rawmoves[i] == '40' or rawmoves[i] == '48' or rawmoves[i] == '56'):
                pgn += "a"
            elif(rawmoves[i] == '1' or rawmoves[i] == '9' or rawmoves[i] == '17' or rawmoves[i] == '25' or rawmoves[i] == '33' or rawmoves[i] == '41' or rawmoves[i] == '49' or rawmoves[i] == '57'):
                pgn += "b"
            elif(rawmoves[i] == '2' or rawmoves[i] == '10' or rawmoves[i] == '18' or rawmoves[i] == '26' or rawmoves[i] == '34' or rawmoves[i] == '42' or rawmoves[i] == '50' or rawmoves[i] == '58'):
                pgn += "c"
            elif(rawmoves[i] == '3' or rawmoves[i] == '11' or rawmoves[i] == '19' or rawmoves[i] == '27' or rawmoves[i] == '35' or rawmoves[i] == '43' or rawmoves[i] == '51' or rawmoves[i] == '59'):
                pgn += "d"
            elif(rawmoves[i] == '4' or rawmoves[i] == '12' or rawmoves[i] == '20' or rawmoves[i] == '28' or rawmoves[i] == '36' or rawmoves[i] == '44' or rawmoves[i] == '52' or rawmoves[i] == '60'):
                pgn += "e"
            elif(rawmoves[i] == '5' or rawmoves[i] == '13' or rawmoves[i] == '21' or rawmoves[i] == '29' or rawmoves[i] == '37' or rawmoves[i] == '45' or rawmoves[i] == '53' or rawmoves[i] == '61'):
                pgn += "f"
            elif(rawmoves[i] == '6' or rawmoves[i] == '14' or rawmoves[i] == '22' or rawmoves[i] == '30' or rawmoves[i] == '38' or rawmoves[i] == '46' or rawmoves[i] == '54' or rawmoves[i] == '62'):
                pgn += "g"
            elif(rawmoves[i] == '7' or rawmoves[i] == '15' or rawmoves[i] == '23' or rawmoves[i] == '31' or rawmoves[i] == '39' or rawmoves[i] == '47' or rawmoves[i] == '55' or rawmoves[i] == '63'):
                pgn += "h"
            else:
                pgn += "ERR178!"

            # Rank designation
        if(int(rawmoves[i]) >= 0 and int(rawmoves[i]) <= 7):
            pgn += "8 "
        elif(int(rawmoves[i]) >= 8 and int(rawmoves[i]) <= 15):
            pgn += "7 "
        elif(int(rawmoves[i]) >= 16 and int(rawmoves[i]) <= 23):
            pgn += "6 "
        elif(int(rawmoves[i]) >= 24 and int(rawmoves[i]) <= 31):
            pgn += "5 "
        elif(int(rawmoves[i]) >= 32 and int(rawmoves[i]) <= 39):
            pgn += "4 "
        elif(int(rawmoves[i]) >= 40 and int(rawmoves[i]) <= 47):
            pgn += "3 "
        elif(int(rawmoves[i]) >= 48 and int(rawmoves[i]) <= 55):
            pgn += "2 "
        elif(int(rawmoves[i]) >= 56 and int(rawmoves[i]) <= 63):
            pgn += "1 "
        else:
            pgn += "ERR198!"
        i += 1  # progress to next move
        moveNum += 0.5
print("pgn: " + pgn)
# file.write(pgn)
file.close()
