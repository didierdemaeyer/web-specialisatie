var gulp = require('gulp');
var less = require('gulp-less');
var path = require('path');
var minifyCSS = require('gulp-minify-css');

gulp.task('less', function () {
  return gulp.src('./3.15-opmaak-van-de-output/style.less')    // replace with file you want to compile
    .pipe(less())
    // .pipe(minifyCSS())
    .pipe(gulp.dest('./3.15-opmaak-van-de-output'));           // replace with folder where the compiled file should go
});
