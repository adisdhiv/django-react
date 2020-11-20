import React from 'react';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'
import './App.css';
import Candidate from './Candidate';
import CandidateCreate from './CandidateCreate';
import CandidateDelete from './CandidateDelete';
import Candidates from './Candidates';
import Header from './Header';
import Interviewers from './Interviewers';

function App() {
  return (
    <Router>
      <div className="app">
        <Switch>
          <Route path="/candidates">
            <Header />
            <Candidates />
          </Route>
          <Route path="/candidate-create">
          <Header />
            <CandidateCreate />  
          </Route>
          <Route path="/candidate-update/:id">
          <Header />
            <Candidate />
          </Route>
          <Route path="/candidate-delete/:id">
          <Header />
            <CandidateDelete />
          </Route>
          <Route path = '/interviewers'>
          <Header />
            <Interviewers />
          </Route>
          <Route path = '/'>
          <Header />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
