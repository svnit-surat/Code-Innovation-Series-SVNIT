import React, { Component, Fragment } from 'react';
import { Link } from 'react-router-dom';

class Login extends Component {

  constructor() {
    super();
    this.state = {
      email: '',
      password: '',
      error: false
    }
  }

  handleChange = (e) => {
    const {name, value} = e.target;
    this.setState({[name]: value});
  }

  handleSubmit = (e) => {
    e.preventDefault();
    if(this.state.email.length === 0) {
      this.setState({error: true});
    }
    else {
      this.setState({error: false});
      this.props.login({email: this.state.email, password: this.state.password});
    }
  }

  render() {
    return (
      <React.Fragment>
        <div className="Login">
    			<div className="left-bar">
    				<div className="top">
    					<Link to='/'>
    						<div className="logo">
    							<h1>Pied Piper</h1>
    						</div>
    					</Link>
    					<p>
    						Welcome to the Unified HealthCare Platform
    					</p>
    				</div>
    				<img
    					className="art"
    					src={require("../assets/svg/doc2.svg")}
    					alt=""
    				/>
    			</div>
    			<div className="main-login">
    				<h1>Login</h1>
    				<div className="login-form">
    					<label htmlFor="email">Email</label>
              <input
                 type="text"
                 onChange={this.handleChange}
                 name="email"
                 value={this.state.email}
                 id="email"
               />
    					<label htmlFor="pass">Password</label>
              <input
                 type="password"
                 onChange={this.handleChange}
                 name="password"
                 value={this.state.password}
                 id="password"
               />
    					<button
    						className="primary"
    						onClick={this.handleSubmit}>
    						Log In
    					</button>
    				</div>
            <div className="error-container">
    					{this.props.errors &&
    							<div className="error">
    								{this.props.errors}
    							</div>}
    				</div>
    			</div>
    		</div>
      </React.Fragment>
    )
  }
}

export default Login;
