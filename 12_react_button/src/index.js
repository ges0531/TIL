import React from 'react';
import ReactDOM from 'react-dom';

class CounterApp extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            count: 0
        };
    }

    Add() {
        this.setState({
            count: this.state.count + 1
        })
    }

    Minus() {
        this.setState({
            count: this.state.count - 1
        })
    }
    
    render() {
        return (
            <div>
                <div>{this.state.count}</div>
                <div>
                    <button onClick={() => this.Add()}>+</button>
                    <button onClick={() => this.Minus()}>-</button>
                </div>
            </div>
        );
    }
}

ReactDOM.render(
    <CounterApp />,
    document.querySelector('#root')
)