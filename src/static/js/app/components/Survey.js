import React from 'react';

import SurveyApi from '../api/SurveyApi';
import SurveyPage from './SurveyPage';

export default class Survey extends React.Component {
  state = {
    pageHasLoaded: false,
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
    this.setState({
      userId: userId
    });
    SurveyApi.getFirstPageForUserId(userId, this.updateQuestionsInState);
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
      window.location.href = '/results/' + this.state.userId;
    }
  }

  getSurveyPage(userId, pageNum) {
    SurveyApi.getSurveyPage(userId, pageNum, this.updateQuestionsInState);
  }

  submitAnswers(userId) {
    SurveyApi.submitAnswers(userId, this._surveyPage.giveQuestionData());
  }

  updateQuestionsInState = (questionJson) => {
    this.setState({
      questions: questionJson.data,
      nextPage: questionJson.nextPage,
      pageHasLoaded: true
    });
  }

  render() {
    return (<div>
      <SurveyPage
        questions={this.state.questions}
        ref={(c) => this._surveyPage = c}
        hasErrors={this.state.pageHasErrors}
      />
      <div className='survey__completed' style={{display: this.state.nextPage === false ? 'block' : 'none'}}>
        <p>You have already completed the survey. View your results <a href={'/results/?userId=' + this.state.userId}>here</a>.</p>
      </div>
      <div className='survey-page__next-area'>
        <div className='survey-page__info' style={{display: this.state.pageHasErrors ? 'block' : 'none'}}>
          You need to fill out all of the questions before continuing.
        </div>
        <button
          style={{display: this.state.pageHasLoaded && this.state.nextPage !== false ? 'block' : 'none'}}
          className='survey-page__next-btn'
          onClick={this.getNextPageOrSubmit}>
            {this.state.nextPage === false ? 'Submit' : 'Next'}
        </button>
      </div>
    </div>);
  }
}
