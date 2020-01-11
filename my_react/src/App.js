import React from 'react';
import PropTypes from "prop-types";

function Food({name, rating}) {
  return (
    <div>
      <h1>I like {name}</h1>
      <h4>{rating}/5.0</h4>
    </div>
  );
}

Food.propTypes = {
  name: PropTypes.string.isRequired,
  rating: PropTypes.number.isRequired
};

const foodILike = [{
  id:1,
  name: "Kimchi",
  rating: 3.0
},
{
  id:2,
  name: "Kimbap",
  rating: 4.0
},
{
  id:3,
  name: "bibimbap",
  rating: 5.0
}]

function App() {
  return (
    <div>
      {foodILike.map((dish) => (
        <Food key={dish.id} name={dish.name} rating={dish.rating} />
      ))}
    </div>
  );

}

export default App;
