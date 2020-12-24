/* eslint-disable jsx-a11y/img-redundant-alt */
import React, { useState, useEffect } from "react";
import Axios from "axios";

const Appointment = ({user}) => {

  console.log(user);

	return (
		<div className="Profile">
			<div className="container">
				<div>
					<h1>Your Profile</h1>
				</div>
				<div className="main">
					{/*  APPOINTMENT  */}
					<div className="appointment-info">
						<h3>Your Profile card</h3>
						<div className="cards">
							<div className="card">
								<div className="image">
									<img
										src={require("../assets/icons/profile.png")}
										alt="Image"
									/>
								</div>
								<div className="content">
									<div className="name">{user.name}</div>
									<div className="email">{user.email}</div>
									<div className="box">
										<div className="box1"></div>
										<div className="box2"></div>
										<div className="box3"></div>
									</div>
									<div className="more-details">
										<div className="age">
											<strong>Age</strong> : {user.age}
										</div>
										<div className="bg">
											<strong>Blood Group</strong> :{" "}
											{user.blood_group}
										</div>
										<div className="address">
											<strong>Addres </strong> :{" "}
											{user.address}
										</div>
										<div className="phone">
											<strong>Contact </strong>:{" "}
											{user.phone}
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	);
};

export default Appointment;
