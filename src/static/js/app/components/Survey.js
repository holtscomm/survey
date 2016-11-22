import React from 'react';

import SurveyApi from '../api/SurveyApi';
import SurveyPage from './SurveyPage';

export default class Survey extends React.Component {
  static propTypes = {
    quizType: React.PropTypes.string
  };
  static defaultProps = {
    quizType: ''
  };
  userId = 0;
  state = {
    pageHasLoaded: false,
    pageHasErrors: false,
    questions: [],
    nextPage: 2
  };

  constructor() {
    super();
    this.surveyApi = new SurveyApi();
  }

  componentDidMount() {
    this.userId = document.getElementById('user-id').innerHTML;
    this.getFirstPageForUser(this.userId);
  }

  componentDidUpdate() {
    if (!this.state.pageHasErrors && this.state.nextPage !== 2) {
      window.scrollTo(0, this.surveyTop.offsetTop);
    }
  }

  getFirstPageForUser(userId) {
    SurveyApi.getFirstPageForUserId(userId, this.props.quizType, this.updateQuestionsInState);
  }

  getNextPageOrSubmit = (e) => {
    if (Object.keys(this._surveyPage.getQuestions()).length !== 15) {
      this.setState({
        pageHasErrors: true
      });
      return;
    } else {
      this.setState({
        pageHasErrors: false
      });
    }
    this.submitAnswers(this.userId);
    if (this.state.nextPage !== false) {
      this.getSurveyPage(this.userId, this.state.nextPage);
    } else {
      if (this.props.quizType === 'trial') {
        window.location.href = 'https://gifts.holtscomm.ca/';
      } else {
        window.location.href = `/results/?userId=${this.userId}`;
      }
    }
  };

  getSurveyPage(userId, pageNum) {
    SurveyApi.getSurveyPage(userId, pageNum, this.props.quizType, this.updateQuestionsInState);
  }

  submitAnswers(userId) {
    SurveyApi.submitAnswers(userId, this._surveyPage.giveQuestionData(), this.props.quizType);
  }

  updateQuestionsInState = ({data, nextPage}) => {
    this.setState({
      questions: data,
      nextPage: nextPage,
      pageHasLoaded: true
    });
  };

  render() {
    const completedStyles = {
      display: this.state.nextPage === false && this.state.questions.length === 0 ? 'block' : 'none'
    };
    const errorsStyles = {
      display: this.state.pageHasErrors ? 'block' : 'none'
    };
    const nextPageBtnStyles = {
      display: this.state.pageHasLoaded &&
        this.state.questions.length > 0 ? 'block' : 'none'
    };
    return (
      <div ref={(div) => this.surveyTop = div }>
        <SurveyPage
          questions={this.state.questions}
          ref={(c) => this._surveyPage = c}
          hasErrors={this.state.pageHasErrors}
        />
        <div className='survey__completed' style={completedStyles}>
          <p>You have already completed the survey. View your results <a href={'/results/?userId=' + this.userId}>here</a>.</p>
        </div>
        <div className='survey-page__next-area'>
          <div className='survey-page__info' style={errorsStyles}>
            You need to fill out all of the questions before continuing.
          </div>
          <button
            style={nextPageBtnStyles}
            className='survey-page__next-btn'
            onClick={this.getNextPageOrSubmit}>
            { this.state.nextPage === false ? 'Submit' : 'Next →'}
          </button>
        </div>
      </div>
    );
  }
}
