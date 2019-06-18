# netcell - microblogging

![](media/screenshots.png)

[![forthebadge made-with-python](https://camo.githubusercontent.com/5392ad6fb7875a2520001270f08309896b6cb25d/687474703a2f2f466f7254686542616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667)](https://www.python.org/)


![Generic badge](https://img.shields.io/badge/release-1.0-RED.svg) ![Maintenance](https://img.shields.io/badge/Maintained%3F-no-green.svg) ![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg) ![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

**netcell** is a opensource microblogging platform, it respecs your privacy and gets the job done.



## Installation

```bash
$ git clone https://github.com/daehruoydeef/netcell-microblogging
$ cd netcell-microblogging
$ python manage.py runserver
```

## Usage

This will start itself on 
```
localhost:8000
```
if you want to host this on a real server and directly want to use your own Domain you will need to edit the settings.py to add your host to the allowed hosts array.
```
ALLOWED_HOSTS = ["myDomain.io"]
```

## Features

* Register and Login
* Update, Delete User
* Create, Update and Delete Posts
* Filter Posts by User
* Reset Password by Email
* Mobile Friendly
* upload Profile Picture
* resize Profile Pictures
* SQLite Database



## Who is this for?netcell is for everyone who wants to self-host a simple Microblogging Service, with no worries about Licensing, spying or unwanted third party behavior. Some of the use cases would be:

* used internally as an Update feed on upcoming Events
* Share Ideas or thoughts to a limited audience



## Requirements

* python 3.6 or higher
* django 2.2 or higher



## Technologies used

* Django 2.2
* Pillow
* bootstrap4



## Supporting netcell

netcell is an open source project. It's an independent project with its ongoing development made possible thanks to the support by our amazing backers. If you like this project and would like to see more time invested in this think about Donating.

![](media/liberapay.png)
