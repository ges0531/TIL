function solution(v) {
    var x_dict = {}
    var y_dict = {}
    for (var i = 0; i < v.length; i = i +1) {
        if (v[i][0] in x_dict) {
            delete x_dict[v[i][0]]
        } else {
            x_dict[v[i][0]] = 0
        }
        if (v[i][1] in y_dict) {
            delete y_dict[v[i][1]]
        } else {
            y_dict[v[i][1]] = 0
        } 
    }
    var answer = [
        parseInt(Object.keys(x_dict)[0]), parseInt(Object.keys(y_dict)[0])
    ];

    return answer;
}

console.log(solution([[1, 4], [3, 4], [3, 10]]))