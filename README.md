################
Coding Interview
################


Required Software
=================

- `Python >= 3.10 <https://www.python.org/downloads/>`_
- A text editor of your choice, e.g. `Visual Studio Code <https://code.visualstudio.com>`_


Getting Started
===============

Setup the python environment on Unix::

    # python3 -m venv venv
    # . venv/bin/activate
    (venv) # python -m pip install --upgrade pip
    (venv) # pip install -r requirements.txt

or on Windows::

    > python -m venv venv
    > venv\Scripts\activate.bat
    (venv) > python -m pip install --upgrade pip
    (venv) > pip install -r requirements.txt

Start the development server::

    (venv) # python app.py

Go to http://localhost:5000/


Development
===========

Hot Reload is turned on in Flask using Debug.


Tasks
===========
* Create models for Author and Book
* Authors have a name and rank
* Books have a name, number of pages and a connection to an author
* Authors write books, so Author needs to have a connection to Book and for convenience a property "books"
* Create the actual DB objects using migrations with Flask migrate
* Add some authors and their books
* Under the API endpoint "/api/authors/books" expose all authors with their corresponding books

Optional
----------
* Fetch data from endpoint /api/products/ in Jinja Template
* Render List of Product names in Frontend Content component