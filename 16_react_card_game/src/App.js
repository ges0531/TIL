import React, { useState } from 'react'
import './App.css'
import TinderCard from './react-tinder-card/index'

const db = [
  {
    name: '강석진',
    url: 'http://watch.peoplepower21.org/files/attach/images/461/886/79d4e9058cb84f214310aa59364f1f85.jpg'
  },
  {
    name: '강병원',
    url: 'http://watch.peoplepower21.org/files/attach/images/461/816/f164c361398baab0fb4e05dbfb30b137.jpg'
  },
  {
    name: '강길부',
    url: 'http://watch.peoplepower21.org/images/member/318.jpg'
  },
  {
    name: '권은희',
    url: 'http://watch.peoplepower21.org/images/member/864.jpg'
  },
  {
    name: '나경원',
    url: 'http://watch.peoplepower21.org/images/member/363.jpg'
  },
  {
    name: '권칠승',
    url: 'http://watch.peoplepower21.org/files/attach/images/461/853/b8d89e4258aa9fb95f8d5a599cd5ab01.jpg'
  },
  {
    name: '권칠승',
    url: 'http://watch.peoplepower21.org/files/attach/images/461/853/b8d89e4258aa9fb95f8d5a599cd5ab01.jpg'
  }
]

var a = [];

function App () {
  const characters = db
  const [lastDirection, setLastDirection] = useState()

  const swiped = (direction, nameToDelete) => {
    if (direction === '좋아합니다') {
      a.push(nameToDelete)   
    }
    console.log('removing: ' + nameToDelete)
    setLastDirection(direction)
    console.log(a)
  }

  const outOfFrame = (name) => {
    console.log(name + ' left the screen!')
  }

  return (
    <div>
      <link href='https://fonts.googleapis.com/css?family=Damion&display=swap' rel='stylesheet' />
      <link href='https://fonts.googleapis.com/css?family=Alatsi&display=swap' rel='stylesheet' />
      <h1>공약</h1>
      <div className='cardContainer'>
        {characters.map((character) =>
          <TinderCard className='swipe' key={character.name} onSwipe={(dir) => swiped(dir, character.name)} onCardLeftScreen={() => outOfFrame(character.name)}>
            <div style={{ backgroundImage: 'url(' + character.url + ')' }} className='card'>
              <h3>{character.name}</h3>
            </div>
          </TinderCard>
        )}
      </div>
      {lastDirection ? <h2 className='infoText'>이 사람을 {lastDirection}</h2> : <h2 className='infoText' />}
    </div>
  )
}
console.log(a)

export default App
