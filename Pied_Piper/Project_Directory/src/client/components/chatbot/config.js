import { createChatBotMessage } from "react-chatbot-kit";
import React from "react";
import LinkComp from "./LinkComp";

const config = {
  botName: 'Piperbot',
  initialMessages: [createChatBotMessage(`Greetings! Let's have a quick session of some basic questions. Type 'start' to continue`)],
  state: {
    patientData: [],
  },
  widgets: [
    {
      widgetName: "link",
      widgetFunc: (props) => <LinkComp {...props} />,
      mapStateToProps: ["patientData"]
    }
  ]
}

export default config;
