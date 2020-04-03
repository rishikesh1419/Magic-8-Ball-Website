# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def index() :
# 	return render_template("index.html")

# if __name__ == "__main__" :
# 	app.run()

# print("Hello world!")
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def index() :
# 	return render_template("index.html")

# if __name__ == "__main__" :
# 	app.run()

# print("Hello world!")

import webapp2
import wsgiref.handlers
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(template.render("templates/index.html",{}))


application = webapp2.WSGIApplication([('/', MainPage)])

