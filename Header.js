import React from 'react'
import { Link } from 'react-router-dom';
import './Header.css'

function Header() {
    return (
        <div className = 'header'>
            <div className='header__nav'>
                <Link to ='/candidates' className="link"><span className='header__optioneone'>Candidates</span></Link>
                <Link to ='/interviewers' className="link"><span className='header__optioneone'>Interviewers</span></Link>
            </div>
        </div>
    )
}

export default Header
