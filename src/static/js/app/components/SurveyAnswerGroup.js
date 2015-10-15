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
            <label htmlFor={answerName + 'always'}>
              <input
                type='radio'
                id={answerName + 'always'}
                name={answerName}
                className='survey-page__question-choice--always'
                ref='always'
                value='5'
                onChange={this.handleOnChange}
                required />
              <span>Always</span>
            </label>
        </span>
        <span className='survey-page__question-choice'>
            <label htmlFor={answerName + 'sometimes'}>
              <input
                type='radio'
                id={answerName + 'sometimes'}
                name={answerName}
                className='survey-page__question-choice--sometimes'
                ref='sometimes'
                value='2'
                onChange={this.handleOnChange}
                required />
              <span>Sometimes</span>
            </label>
        </span>
        <span className='survey-page__question-choice'>
            <label htmlFor={answerName + 'rarely'}>
              <input
                type='radio'
                id={answerName + 'rarely'}
                name={answerName}
                className='survey-page__question-choice--rarely'
                ref='rarely'
                value='0'
                onChange={this.handleOnChange}
                required />
              <span>Rarely</span>
            </label>
        </span>
      </span>
    );
  }
}
