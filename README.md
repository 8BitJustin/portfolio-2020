# Flask Portfolio 2020

Git repo of my portfolio website.

## About

Although I already had a portfolio website in place, I created this due to
my focus on Python and Flask. Basically, I wanted a website built using the
tools I'm currently focused on, and this was the result.

## Details

This website is mainly built for viewable purposes for any visitors. For
them, the main page will have a simple greeting, show the latest blog entry
(which will have a 'show more' link if the character limit reaches 300
+), completed projects with Github links, contact information, and blog
page to show blog entries.
   
On the 'user' end, is a login page accessed via the blog page, which
provides access to all entries, delete/edit buttons for each, and a form
to create new blog posts.
     
Each blog entry requires a title and body. When a post is created, it is
provided a unique ID number, and timestamp of when it was created. The
timestamp is altered within the blog.html file using strftime("%A, %b %d
%Y @ %I:%M %p") which gives the Thursday, Sep 17 2020 @ 01:14 PM format.
   
These posts are stored in the Heroku database for the app, and the user
login for the restricted area are stored within the app database. SQLAlchemy
and postgres is used for the databases. 

## Built With

- [Python](https://www.python.org/) - Core programming language used
- [Flask](https://maven.apache.org/) - Web application framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit
- [Bootstrap](https://getbootstrap.com/) - CSS framework used to
develop responsive and mobile-first websites
- [Python-Login](https://flask-login.readthedocs.io/en/latest/) - User
session management for Flask
- [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - Templating library for Python
- [jQuery](https://jquery.com/) - Lightweight JS library
- [JavaScript](https://www.javascript.com/) - Programming language for
websites
- [CSS](https://en.wikipedia.org/wiki/CSS) - Provides style to html
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - Provides
structure of website


## Authors

- **Justin Olson** - _Initial work_ - [JODPortfolio](https://jodportfolio.herokuapp.com/)

