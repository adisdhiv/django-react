import React from 'react'
import './Candidates.css'
import CandidatesTable from './CandidatesTable'
import Button from '@material-ui/core/Button';
import { Link } from 'react-router-dom';
import PersonAddIcon from '@material-ui/icons/PersonAdd';

function Candidates() {

    return (
        <div className = 'candidates'>
            <div className = 'candidates__container'>
				<Link to ='/candidate-create/' style={{ textDecoration: 'none' }}>
                <Button variant="contained" color="primary" startIcon={<PersonAddIcon />}>Add Candidate</Button></Link>
            </div>
			<CandidatesTable />
        </div>
    )
}

export default Candidates

