import React from 'react';

import SurveyQuestion from './SurveyQuestion';

export default class SurveyPage extends React.Component {
  state = {
    questions: []
  }

  gatherQuestionData = (questionObj) => {
    let questions = this.state.questions;
    questions.push(questionObj);
    this.setState({
      questions: questions
    });
  }

  giveQuestionData() {
    return this.state.questions;
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
