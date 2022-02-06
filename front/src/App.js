import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./views/Home";
import Weather from "./views/Weather";
import Crowd from "./views/Crowd";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<Home/>} />
        <Route path="/weather" element={<Weather/>} />
        <Route path="/crowd" element={<Crowd/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
