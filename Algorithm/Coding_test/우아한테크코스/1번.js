function solution(arr) {
    var result = 0
    
    var flag = 0
    console.log(1)
    while (arr[0] !== 1 || arr.length !== 1) {
        var my_list = []
        for (var i=0; i < arr.length; i += 1) {
            if (i === 0) {
                flag = arr[i]
            } else {
                if (flag === arr[i]) {
                    result += 1
                } else {
                    flag = arr[i]
                    my_list.push(result+1)
                    result = 0
                }
            }
        }
        if (result === 0) {
            my_list.push(1)
        } else {
            my_list.push(result+1)
            result = 0
        }
        arr = my_list.slice()
        console.log(arr, 'Hello')
        
    }
    
}

solution([2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2])