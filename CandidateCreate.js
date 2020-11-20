import React, { useState } from "react";
import CandidateDataService from "./CandidateService";
import { useHistory } from 'react-router-dom'
import './CandidateCreate.css'
import { Button } from "@material-ui/core";

function CandidateCreate() {
    const initialCandidateState = {
        id: null,
        name: "",
        phone: "",
        email: "",
        previouscompany: "",
        noticeperiod: "",
      };

    const [candidate, setCandidate] = useState(initialCandidateState);
    const [submitted, setSubmitted] = useState(false);

    const handleInputChange = event => {
    const { name, value } = event.target;
    setCandidate({ ...candidate, [name]: value });
    };
    
    const history = useHistory()
    const cancel = () => {
      history.push('/candidates')
    }

    const saveCandidate = () => {
    var data = {
        name: candidate.name,
        phone: candidate.phone,
        email: candidate.email,
        previouscompany: candidate.previouscompany,
        noticeperiod: candidate.noticeperiod,
    };

    CandidateDataService.create(data)
        .then(response => {
        setCandidate({
            id: response.data.id,
            name: response.data.name,
            phone: response.data.phone,
            email: response.data.email,
            previouscompany: response.data.previouscompany,
            noticeperiod: response.data.noticeperiod,
        });
        setSubmitted(true);
        console.log(response.data);
        })
        .catch(e => {
        console.log(e);
        });
    };

    const newCandidate = () => {
    setCandidate(initialCandidateState);
    setSubmitted(false);
    };

    return (
        <div className = 'candidatecreate'>
            {submitted ? (
        <div className = 'candidatecreate__container'>
          <h4>You have added the candidate successfully!</h4>
          <div className = 'candidatecreate__buttons'>
            <Button variant="contained" color="primary" onClick={newCandidate}>
            Add Another
          </Button>
          <Button variant="contained" color="secondary" onClick={cancel}>
            Cancel
          </Button>
        </div>
        </div>
      ) : (
        <div className = 'candidatecreate__container'>
          <h1>Add Candidate</h1>
          <div className="form-group">
            <label htmlFor="name">Name</label>
            <input
              type="text"
              className="form-control"
              id="name"
              required
              value={candidate.name}
              onChange={handleInputChange}
              name="name"
            />
          </div>

          <div className="form-group">
            <label htmlFor="phone">Phone Number</label>
            <input
              type="text"
              className="form-control"
              id="phone"
              required
              value={candidate.phone}
              onChange={handleInputChange}
              name="phone"
            />
          </div>

          <div className="form-group">
            <label htmlFor="phone">Email id</label>
            <input
              type="text"
              className="form-control"
              id="email"
              required
              value={candidate.email}
              onChange={handleInputChange}
              name="email"
            />
          </div>

          <div className="form-group">
            <label htmlFor="previouscompany">Previous Company</label>
            <input
              type="text"
              className="form-control"
              id="previouscompany"
              required
              value={candidate.previouscompany}
              onChange={handleInputChange}
              name="previouscompany"
            />
          </div>

          <div className="form-group">
            <label htmlFor="noticeperiod">Notice Period</label>
            <input
              type="text"
              className="form-control"
              id="noticeperiod"
              required
              value={candidate.noticeperiod}
              onChange={handleInputChange}
              name="noticeperiod"
            />
          </div>

          <div className = 'candidatecreate__buttons'><Button variant="contained" color="primary" onClick={saveCandidate}>
            Submit
          </Button>
          <Button variant="contained" color="secondary" onClick={cancel}>
            Cancel
          </Button>
          </div>
        </div>
      )}
        </div>
    )
}

export default CandidateCreate
