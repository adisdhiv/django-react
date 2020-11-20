import { Button } from "@material-ui/core";
import React, { useState, useEffect } from "react";
import { useHistory, useParams } from 'react-router-dom';
import CandidateDataService from "./CandidateService";
import './CandidateDelete.css'

function CandidateDelete() {

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

    const deleteCandidate = () => {
        CandidateDataService.remove(currentCandidate.id)
            .then(response => {
            console.log(response.data);
            setMessage("The Candidate was deleted successfully!");
            history.push("/candidates")
            })
            .catch(e => {
            console.log(e);
            });
        };
    
    return (
        <div className = 'candidatedelete'>
          <div className = 'candidatedelete__container'>
            <h2>Are you sure you want to delete "{currentCandidate.name}" ?</h2>
            <div className = 'candidatedelete__buttons'><Button variant="contained" color="secondary"  onClick={deleteCandidate}>
            Delete
          </Button>
          <Button variant="contained" color="primary" onClick={cancel}>
            Cancel
          </Button>
          </div>
          <p>{message}</p>
          </div>
        </div>
    )
}

export default CandidateDelete
