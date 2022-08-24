from flask_app import app  # Needed for @app.route() among other things
from flask_app.models import strategy  # Import models
# Import methods from Flask
from flask import render_template, redirect, request, session


@app.route('/process_form_data')
return render_template('/dashboard')
