import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import UsernamePicker from './UsernamePicker';
import Room from './Room';
import Game1 from './Game1';
import Game2 from './Game2';
import Game3 from './Game3';
import Game4 from './Game4';
import Game5 from './Game5';
import NotFound from './NotFound';
import App from './App';


const Router = () => (
    <BrowserRouter>
        <Switch>
            <Route exact path="/" component={UsernamePicker} />
            <Route path="/room" component={Room} />
            <Route path="/app" component={App} />
            <Route path="/game1" component={Game1} />
            <Route path="/game2" component={Game2} />
            <Route path="/game3" component={Game3} />
            <Route path="/game4" component={Game4} />
            <Route path="/game5" component={Game5} />
            <Route path="/" component={NotFound} />
        </Switch>
    </BrowserRouter>    
);

export default Router;