import heapq
def mix(smallest,sndsmallest,cnt):
    cnt = cnt+1
    new = smallest+2*sndsmallest
    return new,cnt
    
def solution(scoville, K):
    flag = False
    cnt = 0
    heapq.heapify(scoville)
    
    while(len(scoville)>0):
        minimum = heapq.heappop(scoville)
        if minimum >= K: # 굳이 섞지 않아도 되는 경우
            flag = True
            break
        if len(scoville)>0: # 섞을 두개 이상의 음식이 있을 때
            smallest = minimum # minimum
            sndsmallest = heapq.heappop(scoville) # second smallest
            new,cnt = mix(smallest, sndsmallest, cnt)
            heapq.heappush(scoville, new)
            # scoville.append(new)
            # heapq.heapify(scoville)
        else:
            break
        
    if flag:
        return cnt
    else:
        return -1
