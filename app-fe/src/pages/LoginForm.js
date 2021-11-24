import React, { Component } from 'react';
import { useHistory } from "react-router-dom"
import axios from 'axios';

import { API_USER_BASE_URL } from '../constants/index';

export class LoginForm extends Component {
    
    handleFormSubmit = (event) => {
        event.preventDefault();

        const data = {
            username: this.username,
            password: this.password
        }

        axios.post(API_USER_BASE_URL + 'login/', data)
            .then(resp => {
                localStorage.setItem('token', resp.data.token);
                localStorage.setItem('userid', resp.data.id);
                console.log(resp.data.success);
                }
            )
    }

    render () {
        return (
            <form onSubmit={this.handleFormSubmit}>
                <h3>Login</h3>
                <div className="form-group">
                    <label htmlFor="username">Username: </label>
                    <input type="text" onChange={e => this.username = e.target.value} id="username" placeholder="Enter the username" className="textfield" />
                </div>

                <div className="form-group">
                <label htmlFor="password">Password: </label>
                <input type="text" onChange={e => this.password = e.target.value} id="password" placeholder="Enter the password" className="textfield" />
                </div>

                <div className="form-footer">
                <div className="validation-message"></div>
                <input type="submit" className="btn btn-primary" value="Login" />
            </div>
            </form>
        );
    }
}
