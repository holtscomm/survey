import React from 'react';

export class RadioButton extends React.Component {
  render() {
    const {inputId, inputName, inputValue, handleOnChange, desktopText, mobileText} = this.props;
    return (
      <label htmlFor={inputId}>
        <input
          type='radio'
          id={inputId}
          name={inputName}
          value={inputValue}
          onChange={handleOnChange}
          required/>
        <span>
          <span className="hidden-xs hidden-sm">{desktopText}</span>
          <span className="hidden-md hidden-lg">{mobileText}</span>
        </span>
      </label>
    );
  };
}
