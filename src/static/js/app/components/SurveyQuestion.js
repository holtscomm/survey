import React from 'react';

import SurveyAnswerGroup from './SurveyAnswerGroup';

export default class SurveyQuestion extends React.Component {
  static propTypes = {
    questionNumber: React.PropTypes.number.isRequired,
    questionText: React.PropTypes.string.isRequired,
    questionCategory: React.PropTypes.string.isRequired,
    questionAnswer: React.PropTypes.number
  }

  handleChange = (e) => {
    this.props.passUpAnswer({
      'num': this.props.questionNumber,
      'text': this.props.questionText,
      'category': this.props.questionCategory,
      'answer': parseInt(e.target.value)
    });
  }

  render() {
    return (
      <div className={'row question-item question-number-' + this.props.questionNumber}>
        <span className="col-md-1 col-xs-1 question-number">{ this.props.questionNumber }.</span>
        <span className="col-md-8 col-xs-11 question-text">{ this.props.questionText }</span>
        <SurveyAnswerGroup
          questionAnswer={this.props.questionAnswer}
          questionNumber={this.props.questionNumber}
          handleChangeCallback={this.handleChange}
          />
      </div>
    );
  }
}