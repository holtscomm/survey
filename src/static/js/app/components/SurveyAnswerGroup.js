import React from 'react';

export default class SurveyAnswerGroup extends React.Component {
  componentDidMount() {
    let id = 'choice' + this.props.questionNumber;
    if (this.props.questionAnswer == 5) {
      id += 'always';
    } else if (this.props.questionAnswer == 2) {
      id += 'sometimes';
    } else if (this.props.questionAnswer == 0) {
      id += 'rarely';
    } else {
      id = null;
    }

    if (id) {
      React.findDOMNode(this).querySelector('#' + id).checked = true;
    }
  }

  render() {
    let answerName = "choice" + this.props.questionNumber;

    return (
      <span className="col-md-3 col-xs-12">
        <span className="col-xs-4 question-choice">
            <span>Always</span>
            <input
              type="radio"
              name={answerName}
              id={answerName + 'always'}
              value="5"
              onChange={this.props.handleChangeCallback}
              required />
        </span>
        <span className="col-xs-4 question-choice">
            <span>Sometimes</span>
            <input
              type="radio"
              name={answerName}
              id={answerName + 'sometimes'}
              value="2"
              onChange={this.props.handleChangeCallback}
              required />
        </span>
        <span className="col-xs-4 question-choice">
            <span>Rarely</span>
            <input
              type="radio"
              name={answerName}
              id={answerName + 'rarely'}
              value="0"
              onChange={this.props.handleChangeCallback}
              required />
        </span>
      </span>
    );
  }
}

SurveyAnswerGroup.propTypes = {
  questionNumber: React.PropTypes.number.isRequired,
  questionAnswer: React.PropTypes.number
};
