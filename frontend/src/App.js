import React from "react";
import FileUpload from "./components/FileUpload";
import "./styles.css";

function App() {
  return (
    <div className="App">
      <h1>PDF to JSON Converter</h1>
      <FileUpload />
    </div>
  );
}

export default App;
