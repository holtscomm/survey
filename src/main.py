from flask import Flask, render_template

from app.views import render_survey_template, results, survey, superadmin
from app.views.api.v1 import survey as survey_api

app = Flask(__name__)

# now = datetime.datetime.now()
# context['year'] = now.year

@app.route('/')
def main():
    return render_survey_template('index.html')

app.register_blueprint(results.bp)
app.register_blueprint(survey.bp)
app.register_blueprint(survey_api.bp)
app.register_blueprint(superadmin.bp)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
