class MessageParser {
  constructor(actionProvider, state) {
    this.actionProvider = actionProvider;
    this.state = state;
  }

  parse(message) {
    console.log(message);
    const lowerCaseMessage = message.toLowerCase()

    if(this.state.init) {
      if(this.state.quesNo === 1) {

      } else if(this.state.quesNo === 2) {
        this.actionProvider.dataUpdater(message);
        this.actionProvider.questionTwo();
      } else if(this.state.quesNo === 3) {
        this.actionProvider.dataUpdater(message);
        this.actionProvider.questionThree();
      } else if(this.state.quesNo === 4) {
        this.actionProvider.dataUpdater(message);
        this.actionProvider.questionFour();
      } else if(this.state.quesNo === 5) {
        this.actionProvider.dataUpdater(message);
        this.actionProvider.questionFive();
      } else if(this.state.quesNo === 6) {
        this.actionProvider.dataUpdater(message);
        this.actionProvider.questionSix();
      }
    }
    else if(this.state.finished) {
      this.actionProvider.dataUpdater(message);
      this.actionProvider.thanks();
    }
    else {
      if (lowerCaseMessage.includes("start")) {
        this.actionProvider.greet();
      }
    }
  }
}

export default MessageParser;
