jest.dontMock('../SurveyQuestion.js');
jest.dontMock('../SurveyAnswerGroup.js');

describe('SurveyQuestion', function () {
  it('should set state when handleChange is called', function () {
    var React = require('react/addons');
    var SurveyQuestion = require('../SurveyQuestion.js');
    var TestUtils = React.addons.TestUtils;

    var surveyQuestion = TestUtils.renderIntoDocument(
      <SurveyQuestion
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
