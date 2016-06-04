jest.dontMock('../SurveyAnswerGroup.js');

describe('SurveyAnswerGroup', function () {
  var React = require('react');
  var ReactDOM = require('react-dom');
  var TestUtils = require('react-addons-test-utils');
  var SurveyAnswerGroup = require('../SurveyAnswerGroup.js');

  it('should start with nothing selected when questionAnswer is null', function () {
    var handleOnChangeCallbackMock = jest.genMockFn();
    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={null} handleOnChangeCallback={handleOnChangeCallbackMock} />
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
    var handleOnChangeCallbackMock = jest.genMockFn();
    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={5} handleOnChangeCallback={handleOnChangeCallbackMock} />
    );

    expect(answerGroup.refs.stronglyAgree.checked).toEqual(true);
  });

  it('should select the second highest answer if questionAnswer is 4', function () {
    var handleOnChangeCallbackMock = jest.genMockFn();
    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={4} handleOnChangeCallback={handleOnChangeCallbackMock} />
    );

    expect(answerGroup.refs.agree.checked).toEqual(true);
  });

  it('should select the middle answer if questionAnswer is 3', function () {
    var handleOnChangeCallbackMock = jest.genMockFn();
    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={3} handleOnChangeCallback={handleOnChangeCallbackMock} />
    );

    expect(answerGroup.refs.neutral.checked).toEqual(true);
  });

  it('should select the second lowest answer if questionAnswer is 2', function () {
    var handleOnChangeCallbackMock = jest.genMockFn();
    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={2} handleOnChangeCallback={handleOnChangeCallbackMock} />
    );

    expect(answerGroup.refs.disagree.checked).toEqual(true);
  });

  it('should select the highest answer if questionAnswer is 1', function () {
    var handleOnChangeCallbackMock = jest.genMockFn();
    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={1} handleOnChangeCallback={handleOnChangeCallbackMock} />
    );

    expect(answerGroup.refs.stronglyDisagree.checked).toEqual(true);
  });

  it('should call a callback when an answer is selected with the answer provided', function () {
    var dummyCallback = jest.genMockFunction();

    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={null} handleOnChangeCallback={dummyCallback} />
    );

    var inputs = TestUtils.scryRenderedDOMComponentsWithTag(
      answerGroup,
      'input'
    );

    TestUtils.Simulate.change(inputs[0])

    expect(dummyCallback).toBeCalled();
  })
});
