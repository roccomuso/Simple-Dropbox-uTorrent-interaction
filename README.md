# Simple-Dropbox-uTorrent-interaction
Simple Interaction between Dropbox and uTorrent, built with Python.


The python script accepts some parameters, used to edit a txt file inside our Dropbox folder.

Before starting working with this project, make sure to read 'Getting started with Dropbox in Python': https://www.dropbox.com/developers/core/start/python

In fact to make it work you have to create a new app on the Dropbox's website and install the dropbox module for python:
- python -m pip install dropbox

In the Tracker.py file paste your API KEY and APP SECRET codes.

Finally you have to set up uTorrent to execute the python script with specific parameters every time a download was completed:
Just go on Options > Settings > Advanced > Execute program , and insert the path to the python script with this parameter: %N ##

More details can be found on:
- http://www.hackerstribe.com/2014/python-e-dropbox-tener-traccia-dei-download-su-utorrent/

Now every time a new downoload is completed on uTorrent, you'll be noticed with the download's name inside a text file on your dropbox folder (automatically synchronized with all your devices).

