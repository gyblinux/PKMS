import React from 'react';
import { Container, Row, Col } from 'reactstrap';
import { SideNavBar } from '../components/SideNavBar.js';
import { MainFramePage } from '../components/MainFramePage.js';

export const Wiki = () => {
    return (
        <div>
            {/* sidebar + main frame body*/}
            <Container className="bg-light border" fluid>
                <Row>
                    <Col className="bg-light border" xs="3">
                        <SideNavBar type="wikisidebar"/>
                    </Col>
                    <Col className="bg-light border">
                        <MainFramePage />
                    </Col>
                </Row>
            </Container>   
        </div>
    )
}
