// React isn't used directly within jsx, but the transpiled code will use it.
import React from 'react';
import { render } from 'react-dom';

import { loadScript, browserSupportsAllFeatures } from './browser-helpers';
import Survey from './components/Survey';

function startRender(error) {
  if (error) {
    console.error(error);
  } else {
    render(<Survey quizType={window.quizType} />, document.getElementById('survey'));
  }
}

if (browserSupportsAllFeatures()) {
  startRender();
} else {
  // If it's not all supported, load some polyfills.
  loadScript('https://cdn.polyfill.io/v2/polyfill.min.js?features=Promise,fetch&rum=1', startRender);
}
