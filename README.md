Survey System
=============

This is a survey system that runs on Google App Engine. To get up and running, do the following (OS X specific):

To get things up and running, here's "all" you have to do:

1. Clone the repository
2. In your cloned directory, run the following commands in sequential order:
  1. `npm install -g bower` (if you don't have it)
  2. `bower install` (for static assets)
  3. `npm install` (for Javascript-related things and some command-line tools)
  4. `npm run build-js` (to compile the Javascript app)
  5. `npm run build-css` (to compile the styles for the app)
3. Start a Google App Engine server from the `./src` directory of the repo.
4. Navigate to `http://localhost:8080` (your port may vary)!

Those steps will work best on \*nix. Here's what I found worked for me on Windows (10):

1. Download and install NodeJS from [here](https://nodejs.org/en/)
2. Open the `Node.js command prompt` that should have come with your installation.
3. Follow the steps above!

### Bootstrapping

Once you have the app running, go to the Interactive Console and copy-paste the following script to get the 180 quiz questions installed in your datastore:

```python
from app.migrations.question_migration import import_questions

import_questions()
```

Note: The Interactive Console is at http://localhost:9079/console for local instances, but often it's somewhere else on an actual application.

## Developing the app

### JavaScript

Since this is a React app you'll need some form of transpiling in order for things to run. The survey uses jspm and babel for this. Use the following command to keep your JS up to date:

`npm run build-js` or `npm run watch-js` (if you're going to be making changes)
Alternatively, you can install and run webpack directly. `npm install -g webpack`, then `webpack` to compile once and `webpack --watch` to watch and recompile iteratively.

### CSS

We use SASS for compiling stylesheets, so use the following command to compile or watch the scss files respectively:

`npm run build-css` or `npm run watch-css`

The `build-css` command uses node-sass to compile so there aren't any Ruby dependencies.
