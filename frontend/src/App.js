import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import './styles/App.css';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" component={HomePage} />
      </Switch>
    </Router>
  );
}

export default App;