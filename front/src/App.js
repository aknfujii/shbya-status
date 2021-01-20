import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Home from "./views/Home";
import Weather from "./views/Weather";
import Crowd from "./views/Crowd";

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/weather" component={Weather} />
        <Route path="/crowd" component={Crowd} />
      </Switch>
    </BrowserRouter>
  );
}

export default App;
