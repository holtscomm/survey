import 'fetch';

export default class SurveyApi {
  static getFirstPageForUserId(userId, callback) {
    fetch(`/api/v1/survey/getFirstPage/?userId=${userId}`)
      .then((response) => response.json())
      .then((jsonData) => callback(jsonData));
  }

  static getSurveyPage(userId, pageNum, callback) {
    fetch(`/api/v1/survey/${userId}/${pageNum}/`)
      .then((response) => response.json())
      .then((jsonData) => callback(jsonData));
  }

  static submitAnswers(userId, questionData) {
    fetch(`/api/v1/survey/post/${userId}/`, {
      method: 'post',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(questionData)
    })
  }
}
