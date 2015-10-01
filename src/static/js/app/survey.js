import 'fetch';
import React from 'react';

class SurveyAnswerGroup extends React.Component {
  render() {
    let answerName = "choice" + this.props.questionNumber;
    let alwaysSelected = this.props.questionAnswer == 5 ? 'checked' : '';
    return (
      <span className="col-md-3 col-xs-12">
        <span className="col-xs-4 question-choice">
            <span>Always</span>
            <input
              type="radio"
              name={answerName}
              value="2"
              required />
        </span>
        <span className="col-xs-4 question-choice">
            <span>Sometimes</span>
            <input
              type="radio"
              name={answerName}
              value="1"
              required />
        </span>
        <span className="col-xs-4 question-choice">
            <span>Rarely</span>
            <input
              type="radio"
              name={answerName}
              value="0"
              required />
        </span>
      </span>
    );
  }
}

class SurveyQuestion extends React.Component {
  render() {
    let questionClassName = 'row question-item question-number-' + this.props.questionNumber;
    return (
      <div className={questionClassName}>
        <span className="col-md-1 col-xs-1 question-number">{ this.props.questionNumber }.</span>
        <span className="col-md-8 col-xs-11 question-text">{ this.props.questionText }</span>
        <SurveyAnswerGroup
          questionAnswer={this.props.questionAnswer}
          questionNumber={this.props.questionNumber}
          />
      </div>
    );
  }
}

class SurveyPage extends React.Component {
  render() {
    let questions = this.props.questions.map((question) => {
      return (
        <SurveyQuestion
          key={question.question_number}
          questionText={question.text}
          questionNumber={question.question_number}
          questionAnswer={question.answer}
          questionCategory={question.category}/>
      );
    });
    return (
      <div className='survey-page'>
        {questions}
      </div>
    )
  }
}

class Survey extends React.Component {
  state = {
    questions: []
  }

  componentDidMount() {
    this.getSurveyPage(1, 1);
  }

  getSurveyPage(userId, pageNum) {
    let saved = fetch('/api/v1/survey/1/1')
      .then((response) => response.json())
      .then((jsonData) => this.updateQuestionsInState(jsonData));
    // return fetch('/api/v1/survey/1/1')
    //   .then((response) => response.json());
  }

  updateQuestionsInState(questionJson) {
    this.setState({
      questions: questionJson.data
    });
  }

  render() {
    return (<div className='survey'>
        <SurveyPage questions={this.state.questions} />
        
      </div>);
  }
}

React.render(<Survey />, document.getElementById('world-ender'));
