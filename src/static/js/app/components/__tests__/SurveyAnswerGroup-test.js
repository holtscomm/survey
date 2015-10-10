jest.dontMock('../SurveyAnswerGroup.js');

describe('SurveyAnswerGroup', function () {
  it('should start with nothing selected when questionAnswer is null', function () {
    // TODO: Figure out how to reduce this duplication in every test:
    var React = require('react/addons');
    var SurveyAnswerGroup = require('../SurveyAnswerGroup.js');
    var TestUtils = React.addons.TestUtils;

    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={null} />
    );

    var inputs = TestUtils.scryRenderedDOMComponentsWithTag(
      answerGroup,
      'input'
    );

    inputs.forEach(function (input) {
      expect(React.findDOMNode(input).checked).toEqual(false);
    })
  });

  it('should select the highest answer if questionAnswer is 5', function () {
    var React = require('react/addons');
    var SurveyAnswerGroup = require('../SurveyAnswerGroup.js');
    var TestUtils = React.addons.TestUtils;

    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={5} />
    );

    expect(React.findDOMNode(answerGroup).querySelector('#choice1always').checked).toEqual(true);
  });

  it('should select the middle answer if questionAnswer is 2', function () {
    var React = require('react/addons');
    var SurveyAnswerGroup = require('../SurveyAnswerGroup.js');
    var TestUtils = React.addons.TestUtils;

    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={2} />
    );

    expect(React.findDOMNode(answerGroup).querySelector('#choice1sometimes').checked).toEqual(true);
  });

  it('should select the lowest answer if questionAnswer is 0', function () {
    var React = require('react/addons');
    var SurveyAnswerGroup = require('../SurveyAnswerGroup.js');
    var TestUtils = React.addons.TestUtils;

    var answerGroup = TestUtils.renderIntoDocument(
      <SurveyAnswerGroup questionNumber={1} questionAnswer={0} />
    );

    expect(React.findDOMNode(answerGroup).querySelector('#choice1rarely').checked).toEqual(true);
  });

  it('should call a callback when an answer is selected with the answer provided', function () {
    var React = require('react/addons');
    var SurveyAnswerGroup = require('../SurveyAnswerGroup.js');
    var TestUtils = React.addons.TestUtils;

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
