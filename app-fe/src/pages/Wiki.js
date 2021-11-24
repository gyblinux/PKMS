import React from 'react';

import { Container, Row, Col } from 'react-bootstrap';
import { Route, Routes } from 'react-router';

import { SideNavBar } from '../components/sidenavbar/SideNavBar.js';
import { MainFramePage } from '../components/mainframe/MainFramePage.js';

import './Layout.css'
import { Link } from 'react-router-dom';

export const Wiki = () => {
    return (
        <Container fluid>
        <Row>
            <Col className="border sidebar" xs={3}>
                <SideNavBar type="wikisidebar"/>
            </Col>
            
            <Col className="border">
                <Routes>
                    <Route path="posts/*" element={<MainFramePage />} /> 
                    {/* the path is relative path */}
                </Routes>
            </Col>
        </Row>
        </Container>   
    )
}
