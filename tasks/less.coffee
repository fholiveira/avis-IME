autoprefixer = require 'gulp-autoprefixer'
sourcemaps = require 'gulp-sourcemaps'
minify = require 'gulp-minify-css'
plumber = require 'gulp-plumber'
changed = require 'gulp-changed'
watch = require 'gulp-watch'
less = require 'gulp-less'
size = require 'gulp-size'
gulp = require 'gulp'
del = require 'del'


path =
  file: 'src/static/less/site.less'
  less: 'src/static/less/*.less'
  css: 'src/static/css/'


gulp.task 'compile less', ->
  gulp.src path.file
    .pipe do plumber
    .pipe do sourcemaps.init
    .pipe do less
    .pipe do autoprefixer
    .pipe do sourcemaps.write
    .pipe gulp.dest path.css


gulp.task 'deploy less', ->
  gulp.src path.less
    .pipe do plumber
    .pipe do less
    .pipe do autoprefixer
    .pipe minify keepSpecialComments: 0
    .pipe size showFiles: true
    .pipe gulp.dest path.css


gulp.task 'watch less', ->
  gulp.watch path.less, ['compile less']


gulp.task 'clean less', ->
  del [path.css]
