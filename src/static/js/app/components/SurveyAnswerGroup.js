import React from 'react';
import { RadioButton } from './RadioButton';

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
    const answerName = 'choice' + this.props.questionNumber;
    const errorClass = this.props.hasErrors ? ' survey-page--errors' : '';
    return (
      <span
        ref='choices'
        className={'survey-page__question-choices' + errorClass}>
        <span className='survey-page__question-choice survey-page--first-question-choice'>
          <RadioButton
            inputId={answerName + 'strongly-disagree'}
            inputName={answerName}
            inputValue="1"
            handleOnChange={this.handleOnChange}
            desktopText="Strongly Disagree"
            mobileText="SD"
            ref="stronglyDisagree"
            >
          </RadioButton>
        </span>
        <span className='survey-page__question-choice'>
          <RadioButton
            inputId={answerName + 'disagree'}
            inputName={answerName}
            inputValue="2"
            handleOnChange={this.handleOnChange}
            desktopText="Disagree"
            mobileText="D"
            ref="disagree"
            >
          </RadioButton>
        </span>
        <span className='survey-page__question-choice'>
          <RadioButton
            inputId={answerName + 'neutral'}
            inputName={answerName}
            inputValue="3"
            handleOnChange={this.handleOnChange}
            desktopText="Neutral"
            mobileText="N"
            ref="neutral"
            >
          </RadioButton>
        </span>
        <span className='survey-page__question-choice'>
          <RadioButton
            inputId={answerName + 'agree'}
            inputName={answerName}
            inputValue="4"
            handleOnChange={this.handleOnChange}
            desktopText="Agree"
            mobileText="A"
            ref="agree"
            >
          </RadioButton>
        </span>
        <span className='survey-page__question-choice'>
          <RadioButton
            inputId={answerName + 'strongly-agree'}
            inputName={answerName}
            inputValue="5"
            handleOnChange={this.handleOnChange}
            desktopText="Strongly Agree"
            mobileText="SA"
            ref="stronglyAgree"
            >
          </RadioButton>
        </span>
        <span className='survey-page__question-choice'>
          <RadioButton
            inputId={answerName + 'not-applicable'}
            inputName={answerName}
            inputValue="0"
            handleOnChange={this.handleOnChange}
            desktopText="Not Applicable"
            mobileText="NA"
            ref="notApplicable"
            >
          </RadioButton>
        </span>
      </span>
    );
  }
}
