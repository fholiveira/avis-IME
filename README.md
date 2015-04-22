# avis-IME
app que avisa quando um professor do IME atualiza seu site

[![Build Status](https://snap-ci.com/fholiveira/avis-IME/branch/master/build_image)](https://snap-ci.com/fholiveira/avis-IME/branch/master)
[![Heroku](https://heroku-badge.herokuapp.com/?app=avis-ime)](http://wowbagger.herokuapp.com/)

### Development system-wide dependencies
 - [GNU Make](http://www.gnu.org/software/make/) >= 4.1 
 - [Python](https://www.python.org/) >= 3.4

### Setup environment
```bash
git clone https://github.com/contasdoape/avis-IME.git
cd avis-IME
make configure
```

### Run application
```bash
make serve
```

### Send notifications
```bash
make notify
```
