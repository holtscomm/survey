import 'fetch';
import React from 'react';

// Use `jspm bundle-sfx ./src/static/js/app/survey ./src/static/js/out.js` to build this bad boy up into
// a lightning-fast executable. Run from the base of the project!

class SurveyAnswerGroup extends React.Component {
  render() {
    let answerName = "choice" + this.props.questionNumber;
    let alwaysSelected = this.props.questionAnswer == 5 ? 'checked' : '';
    return (
      <span className="col-md-3 col-xs-12">
        <span className="col-xs-4 question-choice">
            <span>Always</span>
            <input
              type="radio"
              name={answerName}
              value="2"
              required />
        </span>
        <span className="col-xs-4 question-choice">
            <span>Sometimes</span>
            <input
              type="radio"
              name={answerName}
              value="1"
              required />
        </span>
        <span className="col-xs-4 question-choice">
            <span>Rarely</span>
            <input
              type="radio"
              name={answerName}
              value="0"
              required />
        </span>
      </span>
    );
  }
}

class SurveyQuestion extends React.Component {
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

class SurveyPage extends React.Component {
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

class Survey extends React.Component {
  state = {
    questions: [],
    done: false,
    nextPage: 2,
    prevPage: 1
  }

  componentDidMount() {
    this.getSurveyPage(1, this.state.prevPage);
  }

  getNextPageOrSubmit = (e) => {
    this.getSurveyPage(1, this.state.nextPage);
  }

  getPreviousPage = (e) => {
    this.getSurveyPage(1, this.state.prevPage);
  }

  getSurveyPage(userId, pageNum) {
    fetch(`/api/v1/survey/${userId}/${pageNum}/`)
      .then((response) => response.json())
      .then((jsonData) => this.updateQuestionsInState(jsonData));
  }

  updateQuestionsInState(questionJson) {
    this.setState({
      questions: questionJson.data,
      prevPage: questionJson.prevPage,
      nextPage: questionJson.nextPage,
      done: questionJson.done
    });
  }

  render() {
    return (<div className='survey'>
        <SurveyPage questions={this.state.questions} />
        <button onClick={this.getPreviousPage}>Previous</button>
        <button onClick={this.getNextPageOrSubmit}>{this.state.lastPage ? 'Submit' : 'Next'}</button>
      </div>);
  }
}

React.render(<Survey />, document.getElementById('world-ender'));
