import React, { Component, Fragment } from 'react';
import { Link } from 'react-router-dom';

const Home = ({history, message}) => {

  const cta = (user) => {
		history.push("/signup");
	};

  return (
    <React.Fragment>
      <div className="Home">
  			<div className="container">
  				{/* TOP SECTION  */}
  				<div className="top">
  					<div className="left">
  						<h3 className="welcome">
  							Welcome to{" "}
  							<div className="logo">
  								<h1>Pied Piper</h1>
  							</div>
  						</h3>
  						<p>
  							A service to connect patients and doctors.
  							<br />Patients can book appointments
  							and can get themeselves checked online.
  						</p>
  						<button className="primary cta" onClick={() => cta()}>
  							"Get Started"
  						</button>
  					</div>
  					<div className="right">
  						<img src={require("../assets/svg/doc3.svg")} alt="" />
  					</div>
  				</div>

  				<div className="middle">
  					<h2>Features</h2>
  					<div className="cards">
  						<div className="card">
  							<img
  								src={require("../assets/icons/heart.png")}
  								alt="Heart Icon"
  							/>
  							<div className="content">
  								<h4>Disease Predicition</h4>
  								<p>
  									Predicition of any disease based on your symptoms with the help of a chatbot.
  								</p>
  							</div>
  						</div>
  						<div className="card">
  							<img
  								src={require("../assets/icons/medicine.png")}
  								alt="Heart Icon"
  							/>
  							<div className="content">
  								<h4>Personal Health Assistant</h4>
  								<p>
  								Store your health records using voice based personal health assistant.
  								</p>
  							</div>
  						</div>
  						<div className="card">
  							<img
  								src={require("../assets/icons/doctor.png")}
  								alt="Heart Icon"
  							/>
  							<div className="content">
  								<h4>Book Appointment</h4>
  								<p>
  								Patients can book online appointments with a specific doctor.
  								</p>
  							</div>
  						</div>
  					</div>
  				</div>
  			</div>
  		</div>
    </React.Fragment>
  )

}

export default Home;
