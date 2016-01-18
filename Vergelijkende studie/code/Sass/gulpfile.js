var gulp = require('gulp');
var sass = require('gulp-sass');


gulp.task('sass', function () {
  gulp.src('./3.12-logica-en-loops/style.scss')     // replace with file you want to compile
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./3.12-logica-en-loops'));     // replace with folder where the compiled file should go
});

// gulp.task('sass:watch', function () {
//   gulp.watch('./css/**/*.scss', ['sass']);
// });
