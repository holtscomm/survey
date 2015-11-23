import React from 'react';

export default class SurveyAnswerGroup extends React.Component {
  static propTypes = {
    questionNumber: React.PropTypes.number.isRequired,
    questionAnswer: React.PropTypes.number,
    hasErrors: React.PropTypes.bool
  };

  componentDidMount() {
    if (this.props.questionAnswer == 5) {
      this.refs.stronglyAgree.checked = true;
    } else if (this.props.questionAnswer == 4) {
      this.refs.agree.checked = true;
    } else if (this.props.questionAnswer == 3) {
      this.refs.neutral.checked = true;
    } else if (this.props.questionAnswer == 2) {
      this.refs.disagree.checked = true;
    } else if (this.props.questionAnswer == 1) {
      this.refs.stronglyDisagree.checked = true;
    }
  }

  handleOnChange = (e) => {
    this.refs.choices.classList.remove('has-error');
    this.props.handleOnChangeCallback(e);
  };

  render() {
    let answerName = 'choice' + this.props.questionNumber;
    let errorClass = this.props.hasErrors ? ' survey-page--errors' : '';
    return (
      <span
        ref='choices'
        className={'survey-page__question-choices' + errorClass}>
        <span className='survey-page__question-choice survey-page--first-question-choice'>
          <label htmlFor={answerName + 'strongly-disagree'}>
            <input
              type='radio'
              id={answerName + 'strongly-disagree'}
              name={answerName}
              ref='stronglyDisagree'
              value='1'
              onChange={this.handleOnChange}
              required />
            <span>SD</span>
          </label>
        </span>
        <span className='survey-page__question-choice'>
          <label htmlFor={answerName + 'disagree'}>
            <input
              type='radio'
              id={answerName + 'disagree'}
              name={answerName}
              ref='disagree'
              value='2'
              onChange={this.handleOnChange}
              required />
            <span>D</span>
          </label>
        </span>
        <span className='survey-page__question-choice'>
          <label htmlFor={answerName + 'neutral'}>
            <input
              type='radio'
              id={answerName + 'neutral'}
              name={answerName}
              ref='neutral'
              value='3'
              onChange={this.handleOnChange}
              required />
            <span>N</span>
          </label>
        </span>
        <span className='survey-page__question-choice'>
          <label htmlFor={answerName + 'agree'}>
            <input
              type='radio'
              id={answerName + 'agree'}
              name={answerName}
              ref='agree'
              value='4'
              onChange={this.handleOnChange}
              required />
            <span>A</span>
          </label>
        </span>
        <span className='survey-page__question-choice'>
          <label htmlFor={answerName + 'strongly-agree'}>
            <input
              type='radio'
              id={answerName + 'strongly-agree'}
              name={answerName}
              ref='stronglyAgree'
              value='5'
              onChange={this.handleOnChange}
              required />
            <span>SA</span>
          </label>
        </span>
      </span>
    );
  }
}
