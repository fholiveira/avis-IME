sourcemaps = require 'gulp-sourcemaps'
coffeelint = require 'gulp-coffeelint'
plumber = require 'gulp-plumber'
coffee = require 'gulp-coffee'
uglify = require 'gulp-uglify'
watch = require 'gulp-watch'
size = require 'gulp-size'
gulp = require 'gulp'
del = require 'del'


path =
  coffee: 'src/static/coffee/*.coffee'
  js: 'src/static/js/'


gulp.task 'compile coffee', ->
  gulp.src path.coffee
    .pipe do plumber
    .pipe do coffeelint
    .pipe do coffeelint.reporter
    .pipe do sourcemaps.init
    .pipe do coffee
    .pipe do sourcemaps.write
    .pipe gulp.dest path.js


gulp.task 'deploy coffee', ->
  gulp.src path.coffee
    .pipe do plumber
    .pipe do coffeelint
    .pipe do coffeelint.reporter
    .pipe do coffee
    .pipe do uglify
    .pipe size showFiles: true
    .pipe gulp.dest path.js


gulp.task 'watch coffee', ->
  watch path.coffee
    .pipe do plumber
    .pipe do coffeelint
    .pipe do coffeelint.reporter
    .pipe do sourcemaps.init
    .pipe do coffee
    .pipe do sourcemaps.write
    .pipe gulp.dest path.js


gulp.task 'clean coffee', ->
  del [path.js]
