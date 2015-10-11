jest
  .dontMock('../SurveyQuestion.js')
  .dontMock('../SurveyAnswerGroup.js');

describe('SurveyQuestion', function () {
  var React = require('react')
  var TestUtils = require('react-addons-test-utils');
  var SurveyQuestion = require('../SurveyQuestion.js');

  it('should call it\'s prop function when handleChange is called', function () {
    var dummyFunction = jest.genMockFunction();

    var surveyQuestion = TestUtils.renderIntoDocument(
      <SurveyQuestion
        passUpAnswer={dummyFunction}
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
    expect(dummyFunction).toBeCalledWith({
      'question_number': 1,
      'category': 'adm',
      'answer': 5
    });
  });
});
