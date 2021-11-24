import React from 'react';
import { Container, Navbar, Nav } from 'react-bootstrap';
import { useState, useEffect } from 'react';
import { TOP_NAVS } from '../../constants/index.js';

import './TopNavBar.css';

export const TopNavBar = () => {
    const [navs, setNavs] = useState([]);
    
    useEffect(() => {
        setNavs([...TOP_NAVS]);
    }, []);

    const handleNavTabClick = (event) => {
        console.log(event.target.value);
    }

    return (
        <div className="topnavbar">
        <Nav variant="tabs" className="justify-content-end" activeKey="#">
        {navs.map((nav, index) => {
                return (
                    <Nav.Item key={index}>
                    <Nav.Link active href={nav.link} onClick={handleNavTabClick}>
                        {nav.text}
                    </Nav.Link>
                    </Nav.Item>
                )
            })
        }
        </Nav>
        </div>
    )
}