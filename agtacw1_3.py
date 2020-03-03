import numpy as np


# start value fro both player
def start():
    return 1,0

# tie-breaking pure strategy for both player
def tie_breaking():
    return 0,0

def play(round):
    i = 0
    # records for both player
    record_1 = [start()[0]]
    record_2 = [start()[1]]
    #game start with fixed round
    while (i <= round):
        #P1 dramasitc strategy
        #respone with the same possibility of P2's ratio of zeors and ones
        #both return 1 for bind breaking
        if record_2.count(0)/float(len(record_2)) == 0.5:
            play_this_turn_1 = tie_breaking()[0]
        if 0.5 < record_2.count(0)/float(len(record_2)):
            play_this_turn_1 = 0
        else:
            play_this_turn_1 = 1
        #P1 dramasitc strategy
        #respone with the opposity possibility of P2's ratio of zeors and ones

        if record_1.count(0)/float(len(record_1)) == 0.5:
            play_this_turn_2 = tie_breaking()[1]
        if 0.5 < record_1.count(0)/float(len(record_1)):
            play_this_turn_2 = 1
        else:
            play_this_turn_2 = 0
        record_1.append(play_this_turn_1)
        record_2.append(play_this_turn_2)
        i += 1
    #return the next time mixed strategy
    return record_1.count(0)/float(len(record_1)),record_2.count(0)/float(len(record_2))




print(play(10000))
