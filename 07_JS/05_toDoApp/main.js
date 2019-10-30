// Card 만들기

const button = document.querySelector('#js-todo-button');
const inputTag = document.querySelector('#js-todo-input');
const reverseBtn = document.querySelector('#js-reverse-button')

reverseBtn.addEventListener('click', () => {
    // const todoArea = document.querySelector('#js-todo-area');
    const todos = document.querySelectorAll('.js-card');


});

button.addEventListener('click', () => {
    const inputArea = document.querySelector('#js-todo-input');
    createTodoCard(inputArea.value);
    inputArea.value = null;
});

inputTag.addEventListener('keydown', (e) => {
    if (e.whice === 13) {
        const inputArea = document.querySelector('#js-todo-input');
        createTodoCard(inputArea.value);
        inputArea.value = null;
    }
});

const createTodoCard = (content, completed=false) => {
    const todoArea = document.querySelector('#js-todo-area');
    const todos = document.querySelectorAll('.js-card');
    while (todoArea.firstChild) {
        todoArea.removeChild(todoArea.firstChild);
    }
    
    const todo = document.createElement('div');
    todo.className = 'ui segment js-card';

    const wrapper = document.createElement('div');
    wrapper.className = 'ui checkbox';

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.addEventListener('click', () => {
        if(checkbox.checked) {
            todo.classList.remove('secondary');
            lable.classList.remove('done');
        }
        else {
            todo.classList.add('secondary');
            lable.classList.add('done');
        }
    })

    const lable = document.createElement('lable');
    lable.innerHTML = content;

    const deleteIcon = document.createElement('i');
    deleteIcon.className = 'icon close custom-icon';

    deleteIcon.addEventListener('click', () => {
        cardArea.removeChild(todo);
    })

    wrapper.appendChild(checkbox);
    wrapper.appendChild(lable);
    todo.appendChild(wrapper);
    todo.appendChild(deleteIcon);
    cardArea.appendChild(todo);
}