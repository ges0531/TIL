const numbers = [1, 2, 3]

numbers[0];  // 1
numbers[-1];  // undefined: index 는 양의 정수
numbers.length;  // 4

// 원본 파괴 methods
numbers.reverse();
numbers.reverse();

numbers.push('a');  // 4 -> [1, 2, 3, 'a']
numbers.pop();  // 'a'

numbers.unshift('a')  // 4 -> ['a', 1, 2, 3]


// 원본 그대로인 methods
numbers.includes('1')  // True
numbers.indexOf(1)  // 0
numbers.join()  // "1,2,3"
numbers.join('')  // "123"
