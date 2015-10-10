Survey System
=============

This is a survey system that runs on Google App Engine. To get up and running, do the following (OS X specific):

1. Clone the repo
2. Install Node (`brew install node` works nicely)
3. `npm install -g bower`
4. `bower install`
5. `npm install`
6. `jspm install`
7. Add the project to your GoogleAppEngineLauncher and run!

If you aren't on OS X... this is more difficult. You could probably get up and running using Bower and Compass through other means. I think they have Windows executables. Once you're there though, you're set.

### Bootstrapping

Once you have the app running, go to the Interactive Console and copy-paste the following script to get the 180 quiz questions installed in your datastore:

```python
from app.migrations.question_migration import import_questions

import_questions()
```

## Developing the app

### JavaScript

Since this is a React app you'll need some form of transpiling in order for things to run. The survey uses jspm and babel for this. Use the following command to keep your JS up to date:

`npm run build-js` or `npm run watch-js` (if you're going to be making changes)

### CSS

We use SASS for compiling stylesheets, so use the following command to compile or watch the scss files respectively:

`npm run build-css` or `npm run watch-css`

The `build-css` command uses node-sass to compile so there aren't any Ruby dependencies anymore.
