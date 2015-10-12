import 'fetch';
import React from 'react';

import SurveyPage from './SurveyPage';

export default class Survey extends React.Component {
  state = {
    done: false,
    pageHasErrors: false,
    questions: [],
    nextPage: 2,
    userId: 0
  }

  componentDidMount() {
    let userId = document.getElementById('user-id').innerHTML;
    this.getFirstPageForUser(userId);
  }

  getFirstPageForUser(userId) {
    fetch(`/api/v1/survey/getFirstPage/?userId=${userId}`)
      .then((response) => response.json())
      .then((jsonData) => {
        this.setState({
          userId: jsonData.userId
        });
        this.updateQuestionsInState(jsonData);
      });
  }

  getNextPageOrSubmit = (e) => {
    if (Object.keys(this._surveyPage.getQuestions()).length !== 20) {
      this.setState({
        pageHasErrors: true
      });
      return;
    } else {
      this.setState({
        pageHasErrors: false
      });
    }
    this.submitAnswers(this.state.userId);
    if (this.state.nextPage !== false) {
      this.getSurveyPage(this.state.userId, this.state.nextPage);
    } else {
      // window.location.href = '/results/' + this.state.userId
    }
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
      body: JSON.stringify(this._surveyPage.giveQuestionData())
    })
  }

  updateQuestionsInState(questionJson) {
    this.setState({
      questions: questionJson.data,
      nextPage: questionJson.nextPage,
      done: questionJson.done
    });
  }

  render() {
    return (<div className='survey'>
      <SurveyPage
        questions={this.state.questions}
        ref={(c) => this._surveyPage = c}
        hasErrors={this.state.pageHasErrors}
      />
      <div className='alert alert-danger' style={{display: this.state.pageHasErrors ? 'block' : 'none'}}>
        You need to fill out all of the questions before continuing.
      </div>
      <button
        className='btn btn-primary'
        onClick={this.getNextPageOrSubmit}>
          {this.state.lastPage ? 'Submit' : 'Next'}
      </button>
    </div>);
  }
}
