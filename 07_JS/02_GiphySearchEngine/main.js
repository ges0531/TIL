// 1. input 태그 안의 값(value)을 잡는다.

// const input = document.querySelector('#js-userinput').value;

// 2-1. button 에 'click;이 일어났을 때, input 에 ENTER키를 쳤을 때 
// [무엇].addEventListener([언제], [어떻게: function])
const button = document.querySelector('#js-go');
const inputArea = document.querySelector('#js-userinput');
const resultArea = document.querySelector('#js-result-area');


button.addEventListener('click', () => {
    const inputValue = inputArea.value
    searchAndPush(inputValue)
});

inputArea.addEventListener('keypress', (event) => {
    if (event.which === 13) {
        const inputValue = inputArea.value
        searchAndPush(inputValue)
    }
    
});


// 3. Giphy API 에서 넘겨준 Data 를 index.html 에서 보여준다.
const searchAndPush = (keyword) => {
    const inputCount = document.querySelector('#js-image-count').value;
    const API_KEY = 'CqgTEwLKXfNeA5pOiXK1Zpwsjab9gBqZ';
    const url = `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${keyword}&limit=${inputCount}&offset=0&rating=G&lang=ko`

    const AJAX = new XMLHttpRequest();  // 요청 준비
    AJAX.open('GET', url);  // 요청 세팅
    AJAX.send();  // 요청 보내기

    AJAX.addEventListener('load', (answer) => {
        const res = answer.target.response;
        const giphyData = JSON.parse(res);
        const dataSet = giphyData.data;
        resultArea.innerHTML = null
        for (const data of dataSet) {
            pushToDOM(data.images.fixed_height.url);
        }
    });

    const pushToDOM = (imageUrl) => {
        const imageTag = document.createElement('img');
        imageTag.src = imageUrl;
        imageTag.alt = 'giphy-image';
        imageTag.classList.add('container-image');

        resultArea.appendChild(imageTag);
    }
}
