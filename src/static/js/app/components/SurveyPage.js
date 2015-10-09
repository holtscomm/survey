import React from 'react';

import SurveyQuestion from './SurveyQuestion';

export default class SurveyPage extends React.Component {
  state = {
    questions: {}
  }

  checkQuestionData() {
    return this.state.questions;
  }

  gatherQuestionData = (questionObj) => {
    let questions = this.state.questions;
    questions[`${questionObj.question_number}`] = questionObj.category + ':' + questionObj.answer;
    this.setState({
      questions: questions
    });
  }

  giveQuestionData() {
    let questionData = this.checkQuestionData();
    this.setState({
      questions: {}
    });
    return questionData;
  }

  render() {
    let questions = this.props.questions.map((question) => {
      return (
        <SurveyQuestion
          key={question.question_number}
          passUpAnswer={this.gatherQuestionData}
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
