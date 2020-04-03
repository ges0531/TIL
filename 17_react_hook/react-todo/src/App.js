import React, { useState, useEffect, useRef } from "react";
import "./App.css";

////////////////////////////////////////// useInput

// const useInput = (initialValue, validator) => {
//   const [value, setValue] = useState(initialValue);
//   const onChange = event => {
//     const {
//       target: { value }
//     } = event;
//     let willUpdate = true;
//     if (typeof validator === "function") {
//       willUpdate = validator(value);
//     }
//     if (willUpdate) {
//       setValue(value);
//     }

//   };
//   return { value, onChange };
// };

// const App = () => {
//   const maxLen = value => value.length <= 10;
//   const name = useInput("Mr.", maxLen);

//   return (
//     <div className="App">
//       <h1>Hello</h1>
//     </div>
//   );
// }

// export default App;



///////////////////////////////////////////// useTabs

// const content = [
//   {
//     tab: "Section 1",
//     content: "I'm the content of the Section 1"
//   },
//   {
//     tab: "Section 2",
//     content: "I'm the content of the Section 2"
//   }
// ];

// const useTabs = (initialTab, allTabs) => {
//   const [currentIndex, setCurrentIndex] = useState(initialTab);
//   return {
//     currentItem: allTabs[currentIndex],
//     changeItem: setCurrentIndex
//   };
// };

// const App = () => {
//   const { currentItem, changeItem } = useTabs(0, content);
//   return (
//     <div className="App">
//       <h1>Hello</h1>
//       {content.map((section, index) => (
//         <button onClick={() => changeItem(index)}>{section.tab}</button>
//       ))}
//       <div>{currentItem.content}</div>
//     </div>
//   );
// };

// export default App;

//////////////////////////////////////////// useTitle

// const useTitle = (initialTitle) => {
//   const [title, setTitle] = useState(initialTitle)
//   const updateTitle = () => {
//     const htmlTitle = document.querySelector("title")
//     htmlTitle.innerHTML = title
//   }
//   useEffect(updateTitle, [title])
//   return setTitle
// }

// const App = () => {
//   const titleUpdater = useTitle("Loading...")
//   setTimeout(() => titleUpdater("Home"), 5000)
//   return (
//     <div className="App">
//       <h1>Hello</h1>
//     </div>
//   );
// };

// export default App;


/////////////////////////////////// useRef

// const App = () => {
//   const potato = useRef(); // document.getElementByID() 와 같음
//   setTimeout(() => console.log(potato.current), 5000)
//   return (
//     <div className="App">
//       <h1>Hello</h1>
//       <input ref={potato} placeholder="la" />
//     </div>
//   );
// };

// export default App;

////////////////////////////////////// useClick


const useClick = (onClick) => {
  // if(typeof onClick !== "function") {
  //   return ;
  // }
  const element = useRef()
  useEffect(() => {
    if (element.current) {
      element.current.addEventListener("click", onClick)
    }
    return () => element.current.removeEventListener("click", onClick)
  }, [])
  return element
}

const App = () => {
  const sayHello = () => console.log("say hello")
  const title = useClick(sayHello)
  return (
    <div className="App">
      <h1 ref={title}>Hello</h1>
    </div>
  );
};

export default App;