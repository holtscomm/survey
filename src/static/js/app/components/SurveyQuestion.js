import React from 'react';

import SurveyAnswerGroup from './SurveyAnswerGroup';

export default class SurveyQuestion extends React.Component {
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
