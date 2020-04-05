def solution(dataSource, tags):
    answer = []
    ans = []
    doc_dict = {}
    for i in dataSource:
        result = 0
        for j in tags:
            if j in i:
                result += 1
        doc_dict[i[0]] = result
    for k in doc_dict:
        ans.append([doc_dict[k], k])
    ans.sort(key=lambda x: x[1])
    ans.sort(key=lambda x: x[0], reverse=True)
    for ii in ans:
        if ii[0]:
            answer.append(ii[1])
    return answer

solution([
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
], ["t1", "t2", "t3"])