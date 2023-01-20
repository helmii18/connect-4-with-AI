import numpy as np #the structure used for storing the board is an np array
import board as b
import math
from random import shuffle
from anytree import Node
AI = 1
PLAYER = 0
counter=0
leafs = 0
count=0
def min_max_Function(board,depth,maximizingPlayer,alpha,beta,root,algorithmChoice):

    global counter #counter to differentiate between nodes and each others
    global leafs
    global count
    is_terminal = b.is_terminal_node(board)
    if depth == 0 or is_terminal: #if the depth is zero or we have reached a full board then we must return the score of the board
                                #this is a leaf node
        return (None, b.hurestic(board, b.AI_PIECE)-b.hurestic(board,b.PLAYER_PIECE))#calculate the score wrt the AI (maximizing player)
                                                                            #and player score (minimizing player)
    shuffled_neigboors=b.get_Children(board)
    shuffle(shuffled_neigboors)
    column=shuffled_neigboors[0]
    if maximizingPlayer == AI:
        best=-math.inf
        for col in shuffled_neigboors:
            row=b.get_next_open_row(board,col)
            board_copy=board.copy()
            b.drop_piece(board_copy,row,col,b.AI_PIECE)
            child = Node(board_copy, parent=root)
            new_score = min_max_Function(board_copy, depth - 1, PLAYER, alpha, beta, child,algorithmChoice)[1]
            if depth == 1:#if it's a leaf node we print the board and it's score for tracing the minmax algorithm in the graph
                child.name=str(new_score) + "\n" + str(np.flip(board_copy, 0)) + "\n" + str(counter)
                leafs+=1
            else: #else it's a minimizing or a maximizing node then we should just add the score
                counter = counter + 1
                child.name =str(counter) + "\n" + str(new_score)


            if new_score > best:
                best = new_score
                column = col

            if algorithmChoice==0: #if we are using alpha beta pruning we assign the value of beta and alpha
                alpha=max(alpha,best)
                if beta <= alpha :
                    break
            count+=1
    else:
        best=math.inf
        for col in shuffled_neigboors:
            row=b.get_next_open_row(board,col)
            board_copy=board.copy()
            b.drop_piece(board_copy,row,col,b.PLAYER_PIECE)
            child = Node(board_copy, parent=root)
            new_score = min_max_Function(board_copy, depth - 1, AI, alpha, beta, child,algorithmChoice)[1]
            if depth == 1:
                leafs += 1
                child.name=str(new_score) + "\n" + str(np.flip(board_copy, 0)) + "\n" + str(counter)
            else:
                counter = counter + 1
                child.name =str(counter) + "\n" + str(new_score)

            if new_score < best:
                best = new_score
                column = col

            if algorithmChoice==0:
                beta = min(beta, best)
                if beta <= alpha :
                    break
            count+=1

    return column,best
