Survey System
=============

This is a survey system that runs on Google App Engine. To get up and running, do the following (OS X specific):

1. Clone the repo
2. Install Node (`brew install node` works nicely)
3. `npm install -g bower`
4. `bower install`
5. `gem install compass` (I'm going to remove this dependency soon)
6. `compass watch` or `compass compile` (watch will keep watching for changes to scss, helpful if you plan to do that kind of thing)
7. Add the project to your GoogleAppEngineLauncher and run!

If you aren't on OS X... this is more difficult. You could probably get up and running using Bower and Compass through other means. I think they have Windows executables. Once you're there though, you're set.

### Bootstrapping

Once you have the app running, go to the Interactive Console and run the `import_questions()` script that lives in `app/migrations/question_migration.py` to get the 180 quiz questions installed in your datastore.
