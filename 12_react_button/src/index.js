import React from "react";
import ReactDOM from "react-dom";

class ImageUploadCard extends React.Component {
  handleUploadClick = event => {
    state = {
      mainState: "initial", // initial, search, gallery, uploaded
      imageUploaded: 0,
      selectedFile: null
    };
    console.log();
    var file = event.target.files[0];
    const reader = new FileReader();
    var url = reader.readAsDataURL(file);

    reader.onloadend = function(e) {
      this.setState({
        selectedFile: [reader.result]
      });
    }.bind(this);
    console.log(url); // Would see a path?

    this.setState({
      mainState: "uploaded",
      selectedFile: event.target.files[0],
      imageUploaded: 1
    });
  };

  return (
    <div>
      <input accept="image/*"
              type="file"
              onChange={handleUploadClick} />
    </div>
  );
}

ReactDOM.render(<App />, document.querySelector("#root"));
