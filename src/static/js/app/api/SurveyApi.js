export default class SurveyApi {
  static getFirstPageForUserId = (userId, quizType, callback) => {
    window.fetch(`/api/v1/survey/getFirstPage/?userId=${userId}&quizType=${quizType}`)
      .then((response) => response.json())
      .then((jsonData) => callback(jsonData));
  }

  static getSurveyPage = (userId, pageNum, quizType, callback) => {
    window.fetch(`/api/v1/survey/${userId}/${pageNum}/?quizType=${quizType}`)
      .then((response) => response.json())
      .then((jsonData) => callback(jsonData));
  }

  static submitAnswers = (userId, questionData, quizType) => {
    window.fetch(`/api/v1/survey/post/${userId}/?quizType=${quizType}`, {
      method: 'post',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(questionData)
    });
  }
}
