import React from 'react';
import ReactDOM from 'react-dom';

function Counter(props) {
    return (
        <button className="counter" onClick={props.onClick}>
            +
        </button>
    )
}

class Number extends React.Component {
    constructor(props) {
        super(props)
    }
}



ReactDOM.render(<Counter />, document.getElementById('root'));
