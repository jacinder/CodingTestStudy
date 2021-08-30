# https://programmers.co.kr/learn/courses/30/lessons/42891
def solution(food_times, k):
    def add_turn(turn):
        turn += 1
        if turn == len(food_times):
            turn = 0
        return turn
    
    def find_next(food_times, turn):
        # print(f'[FIND NEXT] input turn:{turn}')
        turn = add_turn(turn)
        while True:
            if food_times[turn] != 0:
                break
            turn = add_turn(turn)
        # print(f'[FIND NEXT] output turn:{turn}')
        return turn

    # print(f'[INIT] k={k}, {food_times}')

    if sum(food_times) <= k:
        return -1
    
    turn = 0
    for time in range(k):
        food_times[turn] -= 1
        # print(f'[LOG] turn:{turn}, {food_times}')
        turn = find_next(food_times, turn)    

    return turn+1