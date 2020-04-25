def solution(registered_list, new_id):
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    string_list = []
    number_list = []
    for i in range(len(new_id)):
        if new_id[i] in num_list:
            string_list = new_id[:i]
            number_list = new_id[i:]
            break
    else:
        string_list = list(new_id)
        number_list = ['0']
    print(string_list, number_list)
    for j in range(len(registered_list)):
        if new_id in registered_list:
            number_list = list(str(int(''.join(number_list))+1))
            new_id = ''.join(list(string_list)+number_list)
        else:
            break
    answer = new_id
    return answer

solution(["bird99", "bird98", "bird101", "gotoxy"], "bird98")