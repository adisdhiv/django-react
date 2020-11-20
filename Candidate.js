import React, { useState, useEffect } from "react";
import { useHistory, useParams } from 'react-router-dom';
import CandidateDataService from "./CandidateService";
import './Candidate.css'
import { Button } from "@material-ui/core";

function Candidate() {
    const initialCandidateState = {
        id: null,
        name: "",
        phone: "",
        email: "",
        previouscompany: "",
        noticeperiod: "",
      };

    const [currentCandidate, setCurrentCandidate] = useState(initialCandidateState);
    const [message, setMessage] = useState("");

    const getCandidate = id => {
        CandidateDataService.get(id)
          .then(response => {
            setCurrentCandidate(response.data);
            console.log(response.data);
          })
          .catch(e => {
            console.log(e);
          });
      };
    
    const { id } = useParams()

    useEffect(() => {
        getCandidate(id);
      }, [id]);

    const history = useHistory()
    const cancel = () => {
      history.push('/candidates')
    }
    
    const handleInputChange = event => {
        const { name, value } = event.target;
        setCurrentCandidate({ ...currentCandidate, [name]: value });
        };
    
    const updateCandidate = () => {
        CandidateDataService.update(currentCandidate.id, currentCandidate)
            .then(response => {
            console.log(response.data);
            setMessage("The Candidate was updated successfully!");
            history.push("/candidates")
            })
            .catch(e => {
            console.log(e);
            });
        };
    
    return (
        <div className = 'candidate'>
            <div className="candidate__container">
            <h1>Update Candidate</h1>
            <form>
            <div className="form-group">
            <label htmlFor="name">Name</label>
            <input
              type="text"
              className="form-control"
              id="name"
              required
              value={currentCandidate.name}
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
              value={currentCandidate.phone}
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
              value={currentCandidate.email}
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
              value={currentCandidate.previouscompany}
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
              value={currentCandidate.noticeperiod}
              onChange={handleInputChange}
              name="noticeperiod"
            />
          </div>
            </form>
          <div className = 'candidatecreate__buttons'>
            <Button variant="contained" color="primary" onClick={updateCandidate}>Update</Button>
            <Button variant="contained" color="secondary" onClick={cancel}>
            Cancel
          </Button>
          </div>
          <p>{message}</p>
        </div>
        </div>
    )
}

export default Candidate

      
