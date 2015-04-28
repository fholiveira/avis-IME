dependencies = do require 'bower-files'
minify = require 'gulp-minify-css'
uglify = require 'gulp-uglify'
size = require 'gulp-size'
gulp = require 'gulp'
del = require 'del'


path = 'src/static/lib/'


gulp.task 'resolve dependencies', ->
  gulp.src dependencies.files
    .pipe gulp.dest path


gulp.task 'deploy dependencies', ->
  gulp.src dependencies.ext('css').files
    .pipe minify keepSpecialComments: 0
    .pipe size showFiles: true
    .pipe gulp.dest path

  gulp.src dependencies.ext('js').files
    .pipe do uglify
    .pipe size showFiles: true
    .pipe gulp.dest path


gulp.task 'clean dependencies', ->
  del [path]
