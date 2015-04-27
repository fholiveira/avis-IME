require('require-dir') 'tasks/'
gulp = require 'gulp'


gulp.task 'compile', ['resolve dependencies', 'compile coffee', 'compile less']
gulp.task 'deploy', ['deploy dependencies', 'deploy coffee', 'deploy less']
gulp.task 'clean', ['clean dependencies', 'clean coffee', 'clean less']
gulp.task 'watch', ['watch coffee', 'watch less']


gulp.task 'default', ['compile', 'watch']
