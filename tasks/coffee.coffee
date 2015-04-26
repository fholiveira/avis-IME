sourcemaps = require 'gulp-sourcemaps'
coffeelint = require 'gulp-coffeelint'
filesize = require 'gulp-filesize'
plumber = require 'gulp-plumber'
changed = require 'gulp-changed'
coffee = require 'gulp-coffee'
uglify = require 'gulp-uglify'
watch = require 'gulp-watch'
gulp = require 'gulp'
del = require 'del'


glob_coffee = 'src/coffee/*.coffee'
glob_js = 'src/js/*'
path_js = 'src/js/'


gulp.task 'compile coffee', ->
  gulp.src glob_coffee
    .pipe changed path_js
    .pipe do plumber
    .pipe do coffeelint
    .pipe do coffeelint.reporter
    .pipe do sourcemaps.init
    .pipe coffee { bare: true }
    .pipe do sourcemaps.write
    .pipe gulp.dest path_js


gulp.task 'deploy coffee', ->
  gulp.src glob_coffee
    .pipe do plumber
    .pipe do coffeelint
    .pipe do coffeelint.reporter
    .pipe coffee { bare: true }
    .pipe do uglify
    .pipe gulp.dest path_js

  gulp.src glob_js
    .pipe do filesize


gulp.task 'watch coffee', ->
  watch glob_coffee
    .pipe do plumber
    .pipe changed path_js
    .pipe do coffeelint
    .pipe do coffeelint.reporter
    .pipe do sourcemaps.init
    .pipe coffee { bare: true }
    .pipe do sourcemaps.write
    .pipe gulp.dest path_js


gulp.task 'clean coffee', ->
  del [glob_js]
