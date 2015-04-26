autoprefixer = require 'gulp-autoprefixer'
sourcemaps = require 'gulp-sourcemaps'
minify = require 'gulp-minify-css'
filesize = require 'gulp-filesize'
plumber = require 'gulp-plumber'
changed = require 'gulp-changed'
watch = require 'gulp-watch'
less = require 'gulp-less'
gulp = require 'gulp'
del = require 'del'


glob_less = 'src/static/less/*.less'
glob_css = 'src/static/css/*'
path_css = 'src/static/css/'


gulp.task 'compile less', ->
  gulp.src 'src/static/less/site.less'
    .pipe do plumber
    .pipe do sourcemaps.init
    .pipe do less
    .pipe do autoprefixer
    .pipe do sourcemaps.write
    .pipe gulp.dest path_css


gulp.task 'deploy less', ->
  gulp.src glob_less
    .pipe do plumber
    .pipe do less
    .pipe do autoprefixer
    .pipe minify keepSpecialComments: 0
    .pipe gulp.dest path_css

  gulp.src glob_css
    .pipe do filesize


gulp.task 'watch less', ->
  gulp.watch glob_less, ->
    gulp.src 'src/static/less/site.less'
      .pipe do plumber
      .pipe do sourcemaps.init
      .pipe do less
      .pipe do autoprefixer
      .pipe do sourcemaps.write
      .pipe gulp.dest path_css


gulp.task 'clean less', ->
  del [glob_css]
