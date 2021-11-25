import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router';
import { Card } from 'react-bootstrap';

import { API_USER_BASE_URL } from '../../constants';

export const Editor = () => {
    const [post, setPost] = useState("")
    const [paras, setParas] = useState([])
    const params = useParams();
    const postid = params.id;

    useEffect(() => {
        fetch(API_USER_BASE_URL + `${localStorage.getItem('userid')}/posts/${postid}/`, {
            method: 'GET',
            headers: {
                'Authorization': 'JWT ' + localStorage.getItem('token')
            }
        }).then(resp => resp.json())
            .then(data => {
                console.log(data)
                setPost(data)
            })
    }, [])

    return (
        <div>

            <h1>{post.post_title}</h1>
            {post.paras && post.paras.map((para, index) => {
                return (
                    <Card key={index}>
                        <Card.Body>{para.content}</Card.Body>
                    </Card>
                )
            })}
            {/* post_id post_title paras */}
        </div>
    )
}
