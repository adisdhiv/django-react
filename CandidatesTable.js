import React, { useState, useEffect } from 'react'
import './CandidatesTable.css'
import Button from '@material-ui/core/Button';
import DeleteIcon from '@material-ui/icons/Delete';
import EditIcon from '@material-ui/icons/Edit';
import { Link } from 'react-router-dom';

function CandidatesTable() {
    const [data, setData] = useState([])
    
    useEffect(() => {
        fetch("http://localhost:8000/api/candidate-list/")
            .then(res => res.json())
            //.then(data => console.log(data))
            .then(data => setData(data))
    }, [])
      
    return (
        <div className = 'candidatestable'>
            <table className = 'candidatestable__container'>
                <thead className = 'candidatestable__header'>
                    <tr>
                    <th>Candidate Name</th>
                    <th>Phone Number</th>
                    <th>Email id</th>
                    <th>Previous Company</th>
                    <th>Notice Period</th>
                    {/* <th>Resume</th> */}
                    {/* <th>Date Created</th> */}
                    <th></th>
                    <th></th>
                    </tr>
                </thead>
                <tbody className = 'candidatestable__body'>
                    {data.map((item) => {
                        return (                   
                            <tr key = {item.id}>
                                <td>{item.name}</td>
                                <td>{item.phone}</td>
                                <td>{item.email}</td>
                                <td>{item.previouscompany}</td>
                                <td>{item.noticeperiod}</td>
                                {/* <td>{item.resume}</td> */}
                                {/* <td>{item.datecreated}</td> */}
                                <td><Link to={"/candidate-update/" + item.id} style={{ textDecoration: 'none' }}><Button variant="contained" color="primary" startIcon={<EditIcon />}>Edit</Button></Link></td>
                                <td><Link to={"/candidate-delete/" + item.id} style={{ textDecoration: 'none' }}><Button variant="contained" color="secondary" startIcon={<DeleteIcon />}>Delete</Button></Link></td>
                            </tr>
                        )
                    })}
                </tbody>
            </table>
        </div>
    )
}

export default CandidatesTable
