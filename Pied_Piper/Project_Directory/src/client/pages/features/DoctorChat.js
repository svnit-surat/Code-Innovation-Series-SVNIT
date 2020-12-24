import React, {useState}  from 'react'
import { log } from '../../components/doctorchat/utils'
import "./doctorchat.css";
import {startBasicCall, leaveCall} from '../../components/doctorchat/Agora_RTC';

export default function Home(props) {

  const [appid, setAppid] = useState('1f8602c1ee6b4b2aae034969f8b1e16c')
  const [channel, setChannel] = useState('piedpiper')
  const [token, setToken] = useState('0061f8602c1ee6b4b2aae034969f8b1e16cIAD8C1tCyZzYVRzyxZsDTKadIXdjeMA1Y3dnrVpoJyTAxwH9ad4AAAAAEADAccLp+ifmXwEAAQD6J+Zf')
  const [isjoin, setIsJoin] = useState(false)


  const bindInputAppid = (event) => {
    setAppid(event.target.value)
  }

  const bindInputToken = (event) => {
    setToken(event.target.value)
  }

  const bindInputChannel = (event) => {
    setChannel(event.target.value)
  }

  const handleClickJoin = () => {
    // if(!appid || !channel || !token) {
    //   if(!appid) {
    //     openNotification('appid')
    //   }
    //   if(!channel) {
    //     openNotification('channel')
    //   }
    //   if(!token) {
    //     openNotification('token')
    //   }
    //   return
    // }

    let options = {
      appId: appid,
      channel: channel,
      token: token,
    }
    startBasicCall(options)
    log('join channel success')
    setIsJoin(true)
  }

  const handleClickLeave = () => {
    leaveCall()
    log('client leaves channel success')
    setIsJoin(false)
  }

  // const openNotification = (placement) => {
  //   notification.open({
  //     message: 'Please enter complete information',
  //     description:
  //     `The ${placement} is empty`
  //   });
  // };

  const dataProp = props.location.dataProp;
  console.log(dataProp);

  return (
    <div className='home-box'>
      <div className='title-box'>
        <span id='title-agora'>Video Chat with Doctor</span>
      </div>
      <div className='message-box'>

        <div className='click-box'>
          <div className='joinButton'>
            <button type="primary" onClick={handleClickJoin} disabled={isjoin}>Join</button>
          </div>
          <div className='leaveButton'>
            <button onClick={handleClickLeave} disabled={!isjoin}>Leave</button>
          </div>
        </div>
      </div>
      {dataProp && <div className="databox">
            <p>The patient is feeling: {dataProp.data[0]}</p>
            <p>Did the patient take their medication: {dataProp.data[1]}</p>
            <p>Weight: {dataProp.data[2]} kg</p>
            <p>Sleep last night: {dataProp.data[3]} hours</p>
            <p>Blood Sugar: {dataProp.data[4]} mg/dL</p>
            <p>Is the patient sick: {dataProp.data[5]}</p>
      </div>}

      <div className='video-agora-box'>
        <div id='video-agora-local'></div>
      </div>
    </div>
  )
}
