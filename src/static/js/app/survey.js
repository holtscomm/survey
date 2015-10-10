import 'fetch';
import React from 'react';

import SurveyPage from './components/SurveyPage';

class Survey extends React.Component {
  state = {
    questions: [],
    done: false,
    nextPage: 2
  }

  componentDidMount() {
    // TODO: Make this load from the user id passed into the page
    this.getSurveyPage(1, 1);
  }

  getNextPageOrSubmit = (e) => {
    if (Object.keys(this._surveyPage.checkQuestionData()).length !== 20) {
      //alert('You must answer all the questions');
      //return;
    }
    this.submitAnswers(1);
    if (this.state.nextPage !== false) {
      this.getSurveyPage(1, this.state.nextPage);
    } else {

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
        <SurveyPage questions={this.state.questions} ref={(c) => this._surveyPage = c} />
        <button onClick={this.getNextPageOrSubmit}>{this.state.lastPage ? 'Submit' : 'Next'}</button>
      </div>);
  }
}

React.render(<Survey />, document.getElementById('world-ender'));
