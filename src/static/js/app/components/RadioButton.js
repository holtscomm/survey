import React from 'react';

export const RadioButton = ({inputId, inputName, inputValue, handleOnChange, desktopText, mobileText}) => {
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
