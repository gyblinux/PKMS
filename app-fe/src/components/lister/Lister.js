import React from 'react'
import { useState, useEffect } from 'react';

import { API_USER_BASE_URL } from '../../constants';
import { Row } from 'react-bootstrap';
import { Notecard } from '../notecard/Notecard.js';
import { Loader } from '../loader/Loader.js';

export const Lister = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [posts, setPosts] = useState([])
    useEffect(() => {
        setIsLoading(true)
        fetch(API_USER_BASE_URL + `${localStorage.getItem('userid')}/posts/`, {
            method: 'GET',
            headers: {
                'Authorization': 'JWT ' + localStorage.getItem('token')
            }
        })
            .then(resp => resp.json())
            .then(data => setPosts([...data]))
            .catch(error => console.error(error))
            .finally(() => setIsLoading(false))
    }, [])

    return (
        <Row xs={1} md={3} className="g-3">
            {isLoading && <Loader />}
            {posts && posts.map(post => <Notecard key={post.post_id} details={post} />)}
        </Row>
    )
}
