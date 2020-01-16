def solution(answers):
    il=[1, 2, 3, 4, 5]
    i=[2, 1, 2, 3, 2, 4, 2, 5]
    sam=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer=[0,0,0]
    for x in range(0,len(answers)):
        if il[x%5]==answers[x]:answer[0]+=1
        if i[x%8]==answers[x]:answer[1]+=1
        if sam[x%10]==answers[x]:answer[2]+=1
    mx=max(answer)
    for x in range(3):
        if answer[x]== mx:
            answer.append(x+1)
    return answer[3:]