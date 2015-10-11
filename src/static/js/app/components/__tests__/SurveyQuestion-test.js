jest.dontMock('../SurveyQuestion.js');
jest.dontMock('../SurveyAnswerGroup.js');

describe('SurveyQuestion', function () {
  it('should set state when handleChange is called', function () {
    var React = require('react')
    var TestUtils = require('react-addons-test-utils');
    var SurveyQuestion = require('../SurveyQuestion.js');

    var surveyQuestion = TestUtils.renderIntoDocument(
      <SurveyQuestion
        passUpAnswer={() => {}}
        key={1}
        questionText={'Some text'}
        questionNumber={1}
        questionAnswer={null}
        questionCategory={'adm'}
        />
    );

    var answerInputs = TestUtils.scryRenderedDOMComponentsWithTag(
      surveyQuestion,
      'input'
    );

    TestUtils.Simulate.change(answerInputs[0]);
    expect()
  })
});
