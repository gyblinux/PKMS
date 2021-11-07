import React from 'react';
import { Nav, NavItem, NavLink } from 'reactstrap';
import { useState, useEffect } from 'react';
import { TOP_NAVS } from '../constants/topnavs.js';
import './styles/TopNavBar.css';

export const TopNavBar = () => {
    const [navs, setNavs] = useState([]);
    
    useEffect(() => {
        setNavs([...TOP_NAVS]);
    }, []);

    const handleNavTabClick = (event) => {
        console.log(event.target.value);
    }

    return (
        <div>
            <Nav tabs className="justify-content-end">
                {navs.map((nav, index) => {
                    return (
                        <NavItem id="navitem" key={index}>
                            <NavLink active href="#" onClick={handleNavTabClick}>{nav}</NavLink>
                        </NavItem>
                        )
                    })
                }
            </Nav>
        </div>
    )
}