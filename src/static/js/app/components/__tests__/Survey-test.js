jest
  .dontMock('../SurveyQuestion.js')
  .dontMock('../SurveyAnswerGroup.js')
  .dontMock('../SurveyPage.js')
  .dontMock('../Survey.js');

describe('Survey', function () {
  var React = require('react');
  var TestUtils = require('react-addons-test-utils');
  var Survey = require('../Survey.js');

  // Setup the body with what Survey is looking to get.
  document.body.innerHTML =
      '<div>' +
      '  <span id="user-id">1234</span>' +
      '</div>';

  describe('componentDidMount', function () {
    it('should get a userId from the DOM', function () {
      var survey = TestUtils.renderIntoDocument(<Survey />);

      expect(survey.state.userId).toBe('1234');
    });
  });

  describe('getNextPageOrSubmit', function () {
    it('should not call the getQuestion API if not all 20 questions are answered', function () {
      var survey = TestUtils.renderIntoDocument(<Survey />);

      var nextButton = TestUtils.scryRenderedDOMComponentsWithTag(survey, 'button');
      TestUtils.Simulate.click(nextButton);

      expect(survey.state.pageHasErrors).toBe(true);
    });
  });
});
