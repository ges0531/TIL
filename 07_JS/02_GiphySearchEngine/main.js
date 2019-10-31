// 1. input 태그 안의 값(value)을 잡는다.
// 2-1. button 에 'click' 이 일어났을 때, input 에 ENTER키를 쳤을 때 

// [무엇].addEventListener([언제], [어떻게: function])
const button = document.querySelector('#js-go');
const inputArea = document.querySelector('#js-userinput');
const resultArea = document.querySelector('#js-result-area');


button.addEventListener('click', function () {
    const inputValue = inputArea.value;
    searchAndPush(inputValue);
});

inputArea.addEventListener('keypress', (event) => {
    if (event.which === 13) {
        const inputValue = inputArea.value
        searchAndPush(inputValue);
    }
});

// 3. Giphy API 에서 넘겨준 Data 를 index.html 에서 보여준다.
const searchAndPush = (keyword) => {
    const imageCount = 10;
    const API_KEY = 'uDfYqhoUpJoC6lrKusI65HV1iE68ZdMc';
    const url = `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${keyword}&limit=${imageCount}&offset=10&rating=G&lang=en`;
    
    const AJAX = new XMLHttpRequest();  // 요청 준비
    AJAX.open('GET', url);  // 요청 세팅
    AJAX.send();  // 요청 보내기

    AJAX.addEventListener('load', (answer) => {
        const res = answer.target.response;
        const giphyData = JSON.parse(res);
        const dataSet = giphyData.data;
        // 기존 검색결과 날리기
        resultArea.innerHTML = null;
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

};

