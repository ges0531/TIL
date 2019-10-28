typeof(1)  // number
typeof(Infinity)  // number
typeof(NaN)  // Not A Number : number
// number 연산이 이상할 경우
// 에러가 아니라 NaN 이라는 값을 return

Infinity - Infinity  // NaN
'asdf' + 1  // 덧셈이 아니라 string concat: 'asdf1'
'asdf' - 1  // NaN
'asdf' * 1  // NaN