import React from "react";
import ReactDOM from "react-dom";
import { ButtonGroup, Divider, Button, Container } from "@material-ui/core";

function App() {
  return (
    <Container maxWidth="sm">
      <ButtonGroup>
        <Button>강남구</Button>
        <Button>서초구</Button>
        <Button>동작구</Button>
        <Button>관악구</Button>
        <Button>금천구</Button>
      </ButtonGroup>
      <ButtonGroup>
        <Button>수원시</Button>
        <Button>용인시</Button>
        <Button>화성시</Button>
        <Button>시흥시</Button>
        <Button>의정부시</Button>
      </ButtonGroup>
    </Container>
  );
}

ReactDOM.render(<App />, document.querySelector("#root"));
