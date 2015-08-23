Rapid Prototyping with Python
===
Demo files for my talk in @pyconmy #pyconmy2015. Slides are here, <http://www.slideshare.net/renyiace/rapid-prototyping-with-python-51970348>.


Setting up the environment
---
1. Install virtual environment

    ```
    $ pip install virtualenv virtualenvwrapper
    $ mkvirtualenv pyconmy2015-renyi
    $ workon pyconmy2015-renyi
    ```


2. Install django dependencies

    ```
    $ pip install -r requirements.txt
    ```


3. Install kivy dependencies

    ```
    $ pip install cython kivy
    ```

    Note: If you're using homebrew on Mac OS X, pip install will most likely fail. If you can't sort out the Cython version, just install the binary from here, <http://kivy.org/docs/installation/installation-macosx.html>.


4. To run the django app

    ```
    $ python manage.py runserver
    ```

    Note: If you're running this for the first time, you'll need to create the database and run schemamigration.

    ```
    $ python manage.py syncdb
    $ python manage.py migrate
    ```


5. To run the kivy app

    ```
    $ kivy main.py
    ```
