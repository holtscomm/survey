import React from 'react';

import SurveyQuestion from './SurveyQuestion';

export default class SurveyPage extends React.Component {
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
