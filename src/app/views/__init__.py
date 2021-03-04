"""
View code
"""
import datetime
from flask import render_template

def render_survey_template(template, **context):
    """ Pass a template (html) and a dictionary """
    if not context:
        context = {}
    now = datetime.datetime.now()
    context['year'] = now.year

    return render_template(template, **context)