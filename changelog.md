# Changelog:

## Discover Flask

06/02/2023

- Fixed error that appeared when loading the time/ page.

###### Old code: return flask.render_template('XXXX.html'
###### New code: return flask.render_template('time.html'

- Improved display of date and time on the time/ page.
###### Old code: date=None, hour=None
###### New code: date=date, hour=hour

- Added link between CSS and HTML of the application.
###### Old code (line 8 of the index.html file):  filename='css/XXXX.css') }}" />
###### New code (line 8 of the index.html file): filename='css/main.css') }}" />

## Add "Review" directory

06/02/2023

###### The "Review" directory is used to give opinion.
###### Added "Review" directory with templates folder containing base.html, index.html, submit.html and app.py file.
