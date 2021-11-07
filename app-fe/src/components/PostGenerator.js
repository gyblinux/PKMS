import React from 'react'
import { useState } from 'react'
import { useEffect } from 'react'
export const PostGenerator = () => {
    const [posts, setPosts] = useState([])

    useEffect(() => {
        getPosts();
    }, []);

    // fetching API endpoint
    const getPosts = async () => {
        const resp = await fetch("http://127.0.0.1:8000/api/app/posts/");
        const postsData = await resp.json();
        console.log(postsData);
        setPosts(postsData);
    }
    
    return (
        <div>
            <ul>
                {posts.map((post, index) => <li key={index}>{post.post_id}</li>)}
            </ul>
        </div>
    )
}
