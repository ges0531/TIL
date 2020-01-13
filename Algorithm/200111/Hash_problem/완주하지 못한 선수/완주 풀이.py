import collections


def solution(participant, completion):
    print(collections.Counter(participant), 11)
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer)[0])
    return list(answer.keys())[0]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))