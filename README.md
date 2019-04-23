# Dune
VM manager for MirageOS unikernels

#### Running Dune locally on mac
###### Install required packages from Ubuntu repositories

```sh
$ brew install opam redis python
```

###### Install and launch Redis Server

```sh
$ redis-server
```


###### Initialize OPAM and install MirageOS
```sh
$ opam init -a
$ eval `opam config env`
$ opam install mirage
```

###### Install Dune API requirements
```sh
$ git clone https://github.com/xingeT/Man
$ cd Man
$ pip install -r requirements.txt
```

###### Launch Dune API server
```sh
$ python runapiserver.py
```
The webserver should now be running at `http://localhost:5000` with the API root at `http://localhost:5000/api`

###### Launch Dune Client
```sh
$ cd client
$ sudo npm install
$ bower install
$ gulp build
$ gulp
```
The AngularJS dashboard is served at `http://localhost:8888`

#### Tech Stack
###### Man Core
- Python 3
- [OCaml](http://ocaml.org)
- [Mirage](http://mirage.io)
- [Redis](http://redis.io) for acting as a broker
- [Flask](http://flask.pocoo.org) for the web application and API
- [Redis Queue](http://python-rq.org) for asynchronous task queueing
- [Jinja2](http://jinja.pocoo.org) for templating with Flask
- [MongoDB](https://docs.mongodb.org/manual) for the backend database
- [PyMongo](https://api.mongodb.org/python/current) driver for MongoDB.
- Test bench with [nose](https://nose.readthedocs.org/en/latest)

###### Dune Client
- [AngularJS](https://angularjs.org)
- [Bower](http://bower.io)
- [Gulp](http://gulpjs.com)
