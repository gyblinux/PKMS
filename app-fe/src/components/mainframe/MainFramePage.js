import React from 'react';
import { Container, Breadcrumb } from 'react-bootstrap';
import { Route, Routes } from "react-router-dom";

import { TOP_NAVS, WIKI_SIDE_NAVS } from '../../constants/index.js';
import { Editor } from '../editor/Editor.js';
import { Lister } from '../lister/Lister.js'

import './MainFramePage.css';

export const MainFramePage = () => {

    return (
        <div className="main-frame">
        <Container fluid>
            <Breadcrumb>
                <Breadcrumb.Item href="/wiki/posts/list">{WIKI_SIDE_NAVS[1]}</Breadcrumb.Item>
            </Breadcrumb>

            <Routes>
                <Route path='list' element={<Lister />} />
                <Route path='list/:id' element={<Editor />} />
            </Routes>
        </Container>
        </div>
    )
}
