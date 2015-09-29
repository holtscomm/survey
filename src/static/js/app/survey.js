import fetch from 'fetch';
import React from 'react';

class SurveyQuestion extends React.Component {
  render() {
    console.log(this.props);
    let questionClassName = 'question-number-' + this.props.questionNumber;
    return (<div className={questionClassName}>
        {this.props.questionNumber} {this.props.questionText} {this.props.questionAnswer} {this.props.questionCategory}
      </div>);
  }
}

class SurveyPage extends React.Component {
  render() {
    let questions = this.props.questions.map((question) => {
      return <SurveyQuestion key={question.question_number} questionText={question.text}
                             questionNumber={question.question_number}
                             questionAnswer={question.answer} questionCategory={question.category}/>;
    });
    return (
      <div className='survey-page'>
        {questions}
      </div>
    )
  }
}

class Survey extends React.Component {
  render() {
    let questions = [
      {
      category: "adm",
      question_number: 21,
      text: "I am able to discern when to delegate important responsibilities, and to whom.",
      answer: 0
      }
    ];
    return (<div className='survey'>
        <SurveyPage questions={questions} />
      </div>);
  }
}

React.render(<Survey />, document.getElementById('world-ender'));
