// key - value 에 같은 단어를 쓸때 축약할 수 있음
// ES5
var books = ['Learning JS', 'Eloquent JS'];
var comics = {
    DC: ['Joker', 'Batman'],
    marvel: ['Avengers', 'Spiderman'],

};
var magazine = {}

var bookshop = {
    books: books,
    comics: comics,
    magazine: magazine,
};

// ES6+
const books = ['Learning JS', 'Eloquent JS'];
const comics = {
    DC: ['Joker', 'Batman'],
    marvel: ['Avengers', 'Spiderman'],

};
const magazine = {}

const bookshop = {
    books,  // books: books, 를 줄여서 한 번만 작성가능
    comics,
    magazine,
};

// Method(객체 안의 함수)
// 절대 arrow function () => {} 쓰지 말자.
const me = {
    name: 'kim',
    // 메서드 정의
    greet: function () {
        return `Hi, I'm ${this.name}`
    },
    walk: () => {
        return `${this.name} is walking..`
    },
};