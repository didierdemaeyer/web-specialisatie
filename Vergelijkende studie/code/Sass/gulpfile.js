var gulp = require('gulp');
var sass = require('gulp-sass');


gulp.task('sass', function () {
  gulp.src('./3.13-media-queries/style.scss')     // replace with file you want to compile
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./3.13-media-queries'));     // replace with folder where the compiled file should go
});

// gulp.task('sass:watch', function () {
//   gulp.watch('./css/**/*.scss', ['sass']);
// });
