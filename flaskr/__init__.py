import os

from flask import Flask, flash, redirect, render_template, request, session


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    @app.route('/')
    def index():
        return render_template("blog/index.html")

    @app.route('/blog/articles.html')
    def articles():
        return render_template("blog/articles.html")

    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

    return app
