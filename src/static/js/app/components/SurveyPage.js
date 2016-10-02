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

  fillInQuestion(question, answeredQuestion, hasErrors) {
    const shouldHighlight = hasErrors && question.answer === null && answeredQuestion === undefined;

    return <SurveyQuestion
        key={question.question_number}
        passUpAnswer={this.gatherQuestionData}
        questionText={question.text}
        questionNumber={question.question_number}
        questionAnswer={question.answer}
        questionCategory={question.category}
        hasErrors={shouldHighlight}/>;
  }

  render() {
    let answeredQuestions = this.getQuestions();
    let allQuestions = [];
    console.log(this.props.hasErrors);
    this.props.questions.forEach((question) => {
      allQuestions.push(this.fillInQuestion(
        question,
        answeredQuestions[question.question_number],
        this.props.hasErrors
      ));
      allQuestions.push(<hr key={question.question_number + 'hr'}/>);
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
