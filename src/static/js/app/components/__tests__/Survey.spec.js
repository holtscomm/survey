// Setup the body with what Survey is looking to get.
document.body.innerHTML =
    '<div>' +
    '  <span id="user-id">1234</span>' +
    '</div>';

import React from 'react';
import { mount } from 'enzyme';
import Survey from '../Survey.js';
import SurveyApi from '../../api/SurveyApi.js';
import expect from 'expect';

describe('Survey', function () {
  beforeEach(() => {
    expect.spyOn(SurveyApi, 'getFirstPageForUserId');
  });

  describe('componentDidMount', function () {
    it('should get a userId from the DOM', function () {
      var survey = mount(<Survey quizType="trial" />);
      console.log(document.getElementById('user-id'));
      expect(survey.userId).toBe('1234');
    });
  });

  describe('getNextPageOrSubmit', function () {
    it('should not call the getQuestion API if not all 15 questions are answered', function () {
      var survey = mount(<Survey quizType="trial" />);
      survey.submitAnswers = expect.createSpy();

      var nextButton = survey.find('button').click();

      expect(survey.submitAnswers).not.toHaveBeenCalled();
    });
  });
});
