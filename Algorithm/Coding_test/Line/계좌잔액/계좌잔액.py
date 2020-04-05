def solution(snapshots, transactions):
    id_list = []
    account_dict = {}
    for j in snapshots:
        account_dict[j[0]] = int(j[1])
    for i in transactions:
        if i[0] not in id_list:
            id_list.append(i[0])
            if i[2] not in account_dict:
                account_dict[i[2]] = 0
            if i[1] == 'SAVE':
                account_dict[i[2]] += int(i[3])
            else:
                account_dict[i[2]] -= int(i[3])
    answer = []
    for k in account_dict:
        answer.append([k, "account_dict[k]"])
    answer.sort()
    return answer

solution([
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"]
], [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
])