var gulp = require('gulp');
var less = require('gulp-less');
var path = require('path');

gulp.task('less', function () {
  return gulp.src('./3.13-media-queries/style.less')    // replace with file you want to compile
    .pipe(less({
      paths: [ path.join(__dirname, './', 'includes') ]
    }))
    .pipe(gulp.dest('./3.13-media-queries'));           // replace with folder where the compiled file should go
});
