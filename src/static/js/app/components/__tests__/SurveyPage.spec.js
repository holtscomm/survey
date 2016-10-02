import React from 'react';
import TestUtils from 'react-addons-test-utils';
import expect from 'expect';
import expectJSX from 'expect-jsx';
expect.extend(expectJSX);
import { shallow } from 'enzyme';

import SurveyPage from '../SurveyPage.js';

describe('SurveyPage', () => {
  it('should be a div', () => {
    const wrapper = shallow(<SurveyPage questions={[]} />);
    const expected = 'div';
    expect(wrapper.type()).toEqual(expected);
  });

  describe('fillInQuestion', () => {
    it('should highlight if the question has errors', () => {
      const question = {
        question_number: 1,
        answer: 'Test',
        category: 'adm'
      };
      const wrapper = shallow(SurveyPage.fillInQuestion(question, undefined, true));
      expect()
    })
  });
});
