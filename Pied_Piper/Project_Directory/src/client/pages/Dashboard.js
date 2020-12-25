import React, { Component, Fragment } from 'react';
import { Link } from 'react-router-dom';
import Card from '../components/Card';

class Dashboard extends Component {

  componentDidMount() {

  }

  render() {

    const services = [
      {
    		title: "Book An Appointment with Chatbot",
    		image: require("../assets/icons/heart.png"),
    		imageAlt: "Doctor Icon",
    		desc:
    			"Patients can book online appointments with a specific doctor and can get prescription afterwards.",
    		link: "/dashboard/chatbot",
    	},
    	{
    		title: "Communicate with Doctors",
    		image: require("../assets/icons/face.png"),
    		imageAlt: "Face Icon",
    		desc:
    			"Communicate with a doctor online through video call and sharing your medical history",
    		link: "/dashboard/doctorlist",
    	},
      {
    		title: "Disease Predicition with Chatbot",
    		image: require("../assets/icons/doctor.png"),
    		imageAlt: "Medicine Icon",
    		desc:
    			"Predicition of any disease based on your symptoms with the help of a chatbot.",
    		link: "/dashboard/disease",
    	},
      {
    		title: "Covid Detection by Cough",
    		image: require("../assets/icons/covid.png"),
    		imageAlt: "Earth Icon",
    		desc: "Patients can know whether they have a probabilty of having Covid-19 by recording their coughing audio.",
    		link: "/dashboard/covid",
    	},
      {
    		title: "Save your medical history online",
    		image: require("../assets/icons/medicine.png"),
    		imageAlt: "Medicine Icon",
    		desc:
    			"Share your medical history online so that it's easier for doctors to access it and diagnose you accordingly",
    		link: "/dashboard/medical",
    	},
    ];

    return (
      <React.Fragment>
        <div className="Dashboard">
    			<div className="container">
    				<h1>Hi {this.props.user.name}</h1>
    				<div className="cards">
    					{services.map(({ imageAlt, title, image, desc, link }) => (
    						<Card
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
