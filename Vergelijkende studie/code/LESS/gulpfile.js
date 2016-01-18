var gulp = require('gulp');
var less = require('gulp-less');
var path = require('path');

gulp.task('less', function () {
  return gulp.src('./css/3.6-geneste-css-regels/style.less')
    .pipe(less({
      paths: [ path.join(__dirname, 'css', 'includes') ]
    }))
    .pipe(gulp.dest('./css/3.6-geneste-css-regels'));
});
