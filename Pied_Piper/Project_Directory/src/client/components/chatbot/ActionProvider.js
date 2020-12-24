class ActionProvider {
  constructor(createChatBotMessage, setStateFunc, createClientMessage) {
    this.createChatBotMessage = createChatBotMessage;
    this.setState = setStateFunc;
    this.createClientMessage = createClientMessage;
  }

  greet() {
    const greetingMessage = this.createChatBotMessage("Good! Please submit the answers in the text box.");
    this.updateChatbotState(greetingMessage);
    this.initBot();
    this.questionOne();
  }

  dataUpdater(data) {
    this.setState(prevState => ({
     	...prevState, patientData: [...prevState.patientData, data]
     }))
  }

  initBot() {
    this.setState(prevState => ({
     	...prevState, init: true, quesNo: 1
     }))
  }

  finishBot() {
    this.setState(prevState => ({
     	...prevState, init: false, finished: true
     }))
  }

  updateQuestion(num) {
    this.setState(prevState => ({
     	...prevState, quesNo: num
     }))
  }

  updateChatbotState(message) {

   this.setState(prevState => ({
    	...prevState, messages: [...prevState.messages, message]
    }));
  }

  thanks() {
    const endMessage = this.createChatBotMessage(
      "Thank you! Here's a link to Doctor Chat.",
      {
        widget: "link"
      }
    );
    this.updateChatbotState(endMessage);
  }

  questionOne() {
    const questionMessage = this.createChatBotMessage(`How are you feeling today?`);
    this.updateChatbotState(questionMessage);
    this.updateQuestion(2);
  }

  questionTwo() {
    const questionMessage = this.createChatBotMessage(`Did you took your medication?`);
    this.updateChatbotState(questionMessage);
    this.updateQuestion(3);
  }

  questionThree() {
    const questionMessage = this.createChatBotMessage(`Your weight (in kg)`);
    this.updateChatbotState(questionMessage);
    this.updateQuestion(4);
  }

  questionFour() {
    const questionMessage = this.createChatBotMessage(`For how many hours did you slept last time?`);
    this.updateChatbotState(questionMessage);
    this.updateQuestion(5);
  }

  questionFive() {
    const questionMessage = this.createChatBotMessage(`Your blood sugar level (in mg/dL)`);
    this.updateChatbotState(questionMessage);
    this.updateQuestion(6);
  }

  questionSix() {
    const questionMessage = this.createChatBotMessage(`Are you feeling sick?`);
    this.updateChatbotState(questionMessage);
    this.finishBot();
  }
}

export default ActionProvider;
