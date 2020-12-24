import React, { Component, Fragment } from 'react';
import { Link } from 'react-router-dom';

class SignUp extends Component {

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
    if(this.state.username.length === 0) {
      this.setState({error: true});
    }
    else {
      this.setState({error: false});
      this.props.signup({email: this.state.email, password: this.state.password});
    }
  }

  render() {
    return (
      <React.Fragment>
      <div className="SignUp">
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
            src={require("../assets/svg/doc1.svg")}
            alt="Doctor"
          />
        </div>
        <div className="main-signup">
          <h1>Sign Up</h1>
          <div className="signup-form">
            <label htmlFor="email">Email</label>
            <input
              type="text"
              id="email"
              value={this.state.email}
              onChange={this.handleChange}
            />

            <label htmlFor="fullname">Full Name</label>
            <input
              type="text"
              id="fullname"
            />

            <label htmlFor="phone_number">Phone Number</label>
            <input
              type="number"
              id="phone_number"
            />

            <label htmlFor="age">Age</label>
            <input
              type="number"
              id="age"
            />

            <label htmlFor="blood_group">Blood group</label>
            <select
              name="blood_grp">
              <option value="AB+">AB+</option>
              <option value="AB-">AB-</option>
              <option value="A+">A+</option>
              <option value="A-">A-</option>
              <option value="B+">B+</option>
              <option value="B-">B-</option>
              <option value="O+">O+</option>
              <option value="O-">O-</option>
            </select>

            <label htmlFor="address">Address</label>
            <input
              type="text"
              id="address"
            />

            <label htmlFor="pass">Password</label>
            <input
              type="password"
              id="password"
              name="password"
              value={this.state.password}
              onChange={this.handleChange}
            />
            <button className="primary" onClick={this.handleSubmit}>
              Sign Up
            </button>
          </div>
        </div>
      </div>
      </React.Fragment>
    )
  }
}

export default SignUp;
