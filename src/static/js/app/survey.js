// React isn't used directly within jsx, but the transpiled code will use it.
import React from 'react';
import { render } from 'react-dom';

import Survey from './components/Survey';

render(<Survey quizType={window.quizType} />, document.getElementById('survey'));
