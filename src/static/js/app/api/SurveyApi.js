export default class SurveyApi {
  constructor() {
    if (typeof window.fetch === 'function') {
      console.log('hey fetch');
      this.fetch = window.fetch.bind(window);
    } else {
      console.log('no fetch :(');
      System.import('fetch').then(fetch => {
        console.log(fetch);
        console.log('we gots da fetch');
        this.fetch = fetch.fetchUrl.bind(window)
      });
    }
  }

  getFirstPageForUserId = (userId, quizType, callback) => {
    this.fetch(`/api/v1/survey/getFirstPage/?userId=${userId}&quizType=${quizType}`)
      .then((response) => response.json())
      .then((jsonData) => callback(jsonData));
  }

  getSurveyPage = (userId, pageNum, quizType, callback) => {
    this.fetch(`/api/v1/survey/${userId}/${pageNum}/?quizType=${quizType}`)
      .then((response) => response.json())
      .then((jsonData) => callback(jsonData));
  }

  submitAnswers = (userId, questionData, quizType) => {
    this.fetch(`/api/v1/survey/post/${userId}/?quizType=${quizType}`, {
      method: 'post',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(questionData)
    });
  }
}
