"""

Author : Yassine LAFKIH
Email: yassine.lf.99@gmail.com
Program Name: SudokuSolver

"""
import flask
from flask import request,jsonify
from flask_cors import CORS
app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


# SUDOKO BOARD
board = [
    [7, 8, None, 4, None, None, 1, 2, None],
    [6, None, None, None, 7, 5, None, None, 9],
    [None, None, None, 6, None, 1, None, 7, 8],
    [None, None, 7, None, 4, None, 2, 6, None],
    [None, None, 1, None, 5, None, 9, 3, None],
    [9, None, 4, None, 6, None, None, None, 5],
    [None, 7, None, 3, None, None, None, 1, 2],
    [1, 2, None, None, None, 7, 4, None, None],
    [None, 4, 9, 2, None, 6, None, None, 7]
]
# SOLUTION
def solve(board) -> bool:
    find = findEmpytSquares(board) # tuple vs array  a = (3,2) , a[0] = 3
    if not find:
        return True
    else:
        row,col = find # (i,j)
        for i in range(1,10):
            if valid(board,i,(row,col)):
                board[row][col] = i
                if solve(board):
                    return True
                board[row][col] = None
        return False

#CHECK IF THE NUM ITS VALID
def valid(board: list, num: int, pos: tuple) -> bool:
    # CHECK RCURRENT ROW IF ITS VALID
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # CHECK CURRNET CULUMN IF ITS VALID
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # CHECK CURRENT BOX IF ITS VALID
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


# PRINT BOARD
def printBoard(board: list):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("_ _ _ _ _ _ _ _ _ _ _ _ ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# FIND EMPTY SQUARES POSITION
def findEmpytSquares(board: list) -> bool or tuple:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == None:
                return (i, j)
    return False


printBoard(board)
print("____________________________________________")
solve(board)
@app.route('/api/solve', methods=['GET'])
def api_all():
    print(jsonify(board))
    return jsonify(board)
printBoard(board)
app.run()