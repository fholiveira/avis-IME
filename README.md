# wowbagger
a infinitely prolonged RESTful API

[![Build Status](https://snap-ci.com/contasdoape/wowbagger/branch/master/build_image)](https://snap-ci.com/contasdoape/wowbagger/branch/master)
[![Heroku Staging](https://heroku-badge.herokuapp.com/?app=wowbagger)](http://wowbagger.herokuapp.com/)

### Development system-wide dependencies
 - [GNU Make](http://www.gnu.org/software/make/) >= 4.1 
 - [Python](https://www.python.org/) >= 3.4

### Setup environment
```bash
git clone https://github.com/contasdoape/wowbagger.git
cd wowbagger
make configure
```

### Test application
```bash
make test
```

### Run application
```bash
make serve
```

### Built on top of
 - [Flask](http://flask.pocoo.org/)
 - [Pony ORM](http://ponyorm.com/)
 - [Gunicorn](http://gunicorn.org/)
 - [nose](http://nose.readthedocs.org/)
