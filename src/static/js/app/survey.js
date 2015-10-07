import 'fetch';
import React from 'react';

import SurveyPage from './components/SurveyPage';

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
    this.submitAnswers();
    this.getSurveyPage(1, this.state.nextPage);
  }

  getPreviousPage = (e) => {
    this.calculatePageAnswers();
    this.getSurveyPage(1, this.state.prevPage);
  }

  getSurveyPage(userId, pageNum) {
    fetch(`/api/v1/survey/${userId}/${pageNum}/`)
      .then((response) => response.json())
      .then((jsonData) => this.updateQuestionsInState(jsonData));
  }

  submitAnswers(userId) {
    fetch(`/api/v1/survey/post/${userId}/`, {
      method: 'post',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(this.state.questions)
    })
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
        <SurveyPage questions={this.state.questions} ref={(c) => this._surveyPage = c} />
        <button onClick={this.getPreviousPage}>Previous</button>
        <button onClick={this.getNextPageOrSubmit}>{this.state.lastPage ? 'Submit' : 'Next'}</button>
      </div>);
  }
}

React.render(<Survey />, document.getElementById('world-ender'));
