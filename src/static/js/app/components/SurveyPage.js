import React from 'react';

import SurveyQuestion from './SurveyQuestion';

export default class SurveyPage extends React.Component {
  static propTypes = {
    questions: React.PropTypes.array,
    hasErrors: React.PropTypes.bool
  };

  state = {
    questions: {}
  };

  getQuestions() {
    return this.state.questions;
  }

  gatherQuestionData = (questionObj) => {
    let questions = this.state.questions;
    questions[`${questionObj.question_number}`] = questionObj.category + ':' + questionObj.answer;
    this.setState({
      questions: questions
    });
  };

  giveQuestionData() {
    let questionData = this.getQuestions();
    this.setState({
      questions: {}
    });
    return questionData;
  }

  render() {
    let answeredQuestions = this.getQuestions();
    let allQuestions = [];
    this.props.questions.forEach((question) => {
      let shouldHighlight = false;
      if (this.props.hasErrors) {
        // Check if this question has already been answered.
        shouldHighlight = question.answer === null && answeredQuestions[question.question_number] === undefined;
      }
      if (question.answer !== null) {
        // If it has been answered, add it to the answered questions.
        // Any answer that was already there will be overwritten.
        answeredQuestions[`${question.question_number}`] = question.category + ':' + question.answer;
      }
      // Whether it is answered or not, add it to the list of questions to render.
      allQuestions.push(
        <SurveyQuestion
          key={question.question_number}
          passUpAnswer={this.gatherQuestionData}
          questionText={question.text}
          questionNumber={question.question_number}
          questionAnswer={question.answer}
          questionCategory={question.category}
          hasErrors={shouldHighlight}/>
      );
    });
    if (answeredQuestions.length > 0) {
      this.setState({
        questions: answeredQuestions
      });
    }
    return (
      <div className='survey-page'>
        {allQuestions}
      </div>
    )
  }
}
