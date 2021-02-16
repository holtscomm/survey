import React from 'react';

import SurveyAnswerGroup from './SurveyAnswerGroup';

export default class SurveyQuestion extends React.Component {
  handleChange = (e) => {
    this.props.passUpAnswer({
      'question_number': this.props.questionNumber,
      'category': this.props.questionCategory,
      'answer': parseInt(e.target.value)
    });
  };

  render() {
    return (
      <div className='survey-page__question'>
        <span className={`survey-page__question-number${this.props.hasErrors ? ' has-errors' : ''}`}>
          { this.props.questionNumber }
        </span>
        <span className='survey-page__question-text'>{ this.props.questionText }</span>
        <SurveyAnswerGroup
          questionAnswer={this.props.questionAnswer}
          questionNumber={this.props.questionNumber}
          handleOnChangeCallback={this.handleChange}
          />
      </div>
    );
  }
}
