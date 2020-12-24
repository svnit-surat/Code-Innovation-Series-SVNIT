import React, { Component, Fragment } from 'react';
import { Link } from 'react-router-dom';
import DoctorCard from '../../components/doctorchat/DoctorCard';

class Dashboard extends Component {

  componentDidMount() {

  }

  render() {

    const services = [
    	{
    		title: "Dr. Erlich Bachman",
    		image: require("../../assets/icons/doctor.png"),
    		imageAlt: "Heart Icon",
    		desc:
    			"Answer simple questions and get to know which disease you might have based on the symptoms",
    		link: "/dashboard/doctorchat",
    	},
    	{
    		title: "Dr. Richard Hendricks",
    		image: require("../../assets/icons/doctor.png"),
    		imageAlt: "Face Icon",
    		desc:
    			"Communicate with a doctor online through video call and sharing your medical history",
    		link: "/dashboard/doctorchat",
    	},
    	{
    		title: "Dr. Dinesh Chugtai",
    		image: require("../../assets/icons/doctor.png"),
    		imageAlt: "Medicine Icon",
    		desc:
    			"Share your medical history online so that it's easier for doctors to access it and diagnose you accordingly",
    		link: "/dashboard/doctorchat",
    	}
    ];

    return (
      <React.Fragment>
        <div className="Dashboard">
    			<div className="container">
    				<h1>Available Doctors:</h1>
    				<div className="cards">
    					{services.map(({ imageAlt, title, image, desc, link }) => (
    						<DoctorCard
    							key={title}
    							title={title}
    							image={image}
    							imageAlt={imageAlt}
    							desc={desc}
    							link={link}
    						/>
    					))}
    				</div>
    			</div>
    		</div>
      </React.Fragment>
    )
  }
}

export default Dashboard;
