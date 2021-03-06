Survey System
=============

This is a survey system that runs on Google App Engine. To get up and running, do the following (OS X specific):

To get things up and running, here's "all" you have to do:

1. Clone the repository
2. In your cloned directory, run the following commands in sequential order:
  1. `npm install -g bower` (if you don't have it)
  2. `bower install` (for static assets)
  3. `yarn` (for Javascript-related things and some command-line tools)
  4. `yarn build-js` (to compile the Javascript app)
  5. `yarn build-css` (to compile the styles for the app)
3. Start up the virtualenv for python development: `source venv/bin/activate`
4. Do a pip install if you haven't already `pip3 install -r src/requirements.txt`
5. Run the app `yarn start`
6. Navigate to `http://localhost:8080` (your port may vary)!

### Bootstrapping

Note: Now that we're using google-cloud-ndb this step shouldn't be necessary. But if it is, do the following:

Once you have the app running, go to [superadmin](http://localhost:8080/superadmin/) and
click on the link that says Import questions.

## Developing the app

### JavaScript

Since this is a React app you'll need some form of transpiling in order for things to run. The survey uses jspm and babel for this. Use the following command to keep your JS up to date:

`npm run build-js` or `npm run watch-js` (if you're going to be making changes)
Alternatively, you can install and run webpack directly. `npm install -g webpack`, then `webpack` to compile once and `webpack --watch` to watch and recompile iteratively.

### CSS

We use SASS for compiling stylesheets, so use the following command to compile or watch the scss files respectively:

`npm run build-css` or `npm run watch-css`

The `build-css` command uses node-sass to compile so there aren't any Ruby dependencies.
