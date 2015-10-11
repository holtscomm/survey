jest.dontMock('../components/SurveyQuestion.js');
jest.dontMock('../components/SurveyAnswerGroup.js');
jest.dontMock('../components/SurveyPage.js');
jest.dontMock('../survey.js');

describe('Survey', function () {
  var React = require('react')
  var TestUtils = require('react-addons-test-utils');
  var Survey = require('../survey.js');

  describe('getNextPageOrSubmit', function () {
    it('should not call the getQuestion API if not all 20 questions are answered', function () {
      var survey = TestUtils.renderIntoDocument(<Survey />);


    });
  });
});
