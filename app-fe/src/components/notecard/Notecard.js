import React from 'react'
import { Card, Button, Col } from 'react-bootstrap';
import { Link } from 'react-router-dom';

export const Notecard = (props) => {

    return (
        <Link to={`${props.details.post_id}`}>
            <Col>
            <Card style={{ width: '18rem' }}>  
                <Card.Body>
                    <Card.Title>{props.details.post_title} + {props.details.post_id}</Card.Title>
                    <Button>Check</Button>
                </Card.Body>
            </Card>
            </Col>
        </Link>
    )
}
