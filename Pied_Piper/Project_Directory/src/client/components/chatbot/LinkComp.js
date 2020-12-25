
import React from "react";

import { Link } from 'react-router-dom';

const LinkComp = (props) => {
  return <Link to={{
    pathname:"/dashboard/doctorchat",
    dataProp:{
      data: props.patientData
    }
  }}>Doctor Chat</Link>;
};

export default LinkComp;
