dependencies = do require 'bower-files'
minify = require 'gulp-minify-css'
uglify = require 'gulp-uglify'
gulp = require 'gulp'
del = require 'del'


glob_deps = 'src/static/lib/*'
path_deps = 'src/static/lib'


gulp.task 'resolve dependencies', ->
  gulp.src dependencies.files
    .pipe gulp.dest path_deps


gulp.task 'deploy dependencies', ->
  gulp.src dependencies.ext('css').files
    .pipe minify keepSpecialComments: 0
    .pipe gulp.dest path_deps

  gulp.src dependencies.ext('js').files
    .pipe do uglify
    .pipe gulp.dest path_deps


gulp.task 'clean dependencies', ->
  del [glob_deps]
