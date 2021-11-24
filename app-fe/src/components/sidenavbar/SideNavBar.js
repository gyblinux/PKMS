import React from 'react';
import { Nav, NavItem, NavLink } from 'reactstrap';
import { useState, useEffect } from 'react';
import { BLOG_SIDE_NAVS } from '../../constants/index.js';
import { WIKI_SIDE_NAVS} from '../../constants/index.js';
import './SideBar.css'

export const SideNavBar = (props) => {

    const [items, setItems] = useState([]);

    useEffect(() => {
        if (props.type === "wikisidebar") {
            setItems([...WIKI_SIDE_NAVS]);
        } else if (props.type === "blogsidebar") {
            setItems([...BLOG_SIDE_NAVS]);
        }
    }, []);

    return (
        <div className="sidebar">
            <Nav vertical>
                {items.map((item, index) => <NavItem key={index}><NavLink href="#">{item}</NavLink></NavItem>)}
            </Nav>
        </div>
    )
}
