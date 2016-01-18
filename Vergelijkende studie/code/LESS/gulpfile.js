var gulp = require('gulp');
var less = require('gulp-less');
var path = require('path');

gulp.task('less', function () {
  return gulp.src('./3.9-overerving-van-selectors/style.less')    // replace with file you want to compile
    .pipe(less({
      paths: [ path.join(__dirname, './', 'includes') ]
    }))
    .pipe(gulp.dest('./3.9-overerving-van-selectors'));           // replace with folder where the compiled file should go
});
