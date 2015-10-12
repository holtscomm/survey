import React from 'react';

export default class SurveyAnswerGroup extends React.Component {
  static propTypes = {
    questionNumber: React.PropTypes.number.isRequired,
    questionAnswer: React.PropTypes.number,
    hasErrors: React.PropTypes.bool
  }

  componentDidMount() {
    if (this.props.questionAnswer == 5) {
      this.refs.always.checked = true;
    } else if (this.props.questionAnswer == 2) {
      this.refs.sometimes.checked = true;
    } else if (this.props.questionAnswer == 0) {
      this.refs.rarely.checked = true;
    }
  }

  handleOnChange = (e) => {
    this.refs.choices.classList.remove('has-error');
    this.props.handleOnChangeCallback(e);
  }

  render() {
    let answerName = 'choice' + this.props.questionNumber;
    let errorClass = this.props.hasErrors ? ' survey-page--errors' : '';
    return (
      <span
        ref='choices'
        className={'survey-page__question-choices' + errorClass}>
        <span className='survey-page__question-choice'>
            <span>Always</span>
            <input
              type='radio'
              name={answerName}
              ref='always'
              value='5'
              onChange={this.handleOnChange}
              required />
        </span>
        <span className='survey-page__question-choice'>
            <span>Sometimes</span>
            <input
              type='radio'
              name={answerName}
              ref='sometimes'
              value='2'
              onChange={this.handleOnChange}
              required />
        </span>
        <span className='survey-page__question-choice'>
            <span>Rarely</span>
            <input
              type='radio'
              name={answerName}
              ref='rarely'
              value='0'
              onChange={this.handleOnChange}
              required />
        </span>
      </span>
    );
  }
}
