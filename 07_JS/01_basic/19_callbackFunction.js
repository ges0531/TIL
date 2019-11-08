nfunction a(x, y) {
    return x + y;
}

function b(n) {
    return n ++;
}

function c(f1, f2) {
    return f1(10,10) + f2(99)
}

console.log(
    c(a, b)
)