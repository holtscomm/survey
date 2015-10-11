jest.dontMock('../SurveyAnswerGroup.js');

describe('SurveyAnswerGroup', function () {
  var React = require('react');
  var ReactDOM = require('react-dom');
  var TestUtils = require('react-addons-test-utils');
  var SurveyAnswerGroup = require('../SurveyAnswerGroup.js');

  it('should start with nothing selected when questionAnswer is null', function () {
    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={null} />
    );

    var inputs = TestUtils.scryRenderedDOMComponentsWithTag(
      answerGroup,
      'input'
    );

    inputs.forEach(function (input) {
      expect(ReactDOM.findDOMNode(input).checked).toEqual(false);
    })
  });

  it('should select the highest answer if questionAnswer is 5', function () {
    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={5} />
    );

    expect(answerGroup.refs.always.checked).toEqual(true);
  });

  it('should select the middle answer if questionAnswer is 2', function () {
    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={2} />
    );

    expect(answerGroup.refs.sometimes.checked).toEqual(true);
  });

  it('should select the lowest answer if questionAnswer is 0', function () {
    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={0} />
    );

    expect(answerGroup.refs.rarely.checked).toEqual(true);
  });

  it('should call a callback when an answer is selected with the answer provided', function () {
    var dummyCallback = jest.genMockFunction();

    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={null} handleChangeCallback={dummyCallback} />
    );

    var inputs = TestUtils.scryRenderedDOMComponentsWithTag(
      answerGroup,
      'input'
    );

    TestUtils.Simulate.change(inputs[0])

    expect(dummyCallback).toBeCalled();
  })
});
