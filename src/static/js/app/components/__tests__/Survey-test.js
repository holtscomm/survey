jest
  .dontMock('../SurveyQuestion.js')
  .dontMock('../SurveyAnswerGroup.js')
  .dontMock('../SurveyPage.js')
  .dontMock('../Survey.js');

describe('Survey', function () {
  var React = require('react');
  var TestUtils = require('react-addons-test-utils');
  var Survey = require('../Survey.js');
  Survey.getFirstPageForUser = jest.genMockFunction();

  // Setup the body with what Survey is looking to get.
  document.body.innerHTML =
      '<div>' +
      '  <span id="user-id">1234</span>' +
      '</div>';

  describe.only('componentDidMount', function () {
    it('should get a userId from the DOM', function () {
      var survey = TestUtils.renderIntoDocument(<Survey />);

      expect(Survey.getFirstPageForUser).toBeCalledWith(1234);
    });
  });

  describe('getNextPageOrSubmit', function () {
    it('should not call the getQuestion API if not all 20 questions are answered', function () {
      var survey = TestUtils.renderIntoDocument(<Survey />);

      var nextButton = TestUtils.scryRenderedDOMComponentsWithTag(survey, 'button');
      console.log(nextButton);
      TestUtils.Simulate.click(nextButton);

      expect(Survey.updateQuestionsInState).toBeCalled();
    });
  });
});
