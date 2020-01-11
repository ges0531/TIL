import React from 'react';

function Food({name}) {
  return <h1>I like {name}</h1>
}

const foodILike = [{
  id:1,
  name: "Kimchi"
},
{
  id:2,
  name: "Kimbap"
},
{
  id:3,
  name: "bibimbap"
}]

function App() {
  return (
    <div>
      {foodILike.map((dish) => (
        <Food key={dish.id} name={dish.name} />
      ))}
    </div>
  );

}

export default App;
