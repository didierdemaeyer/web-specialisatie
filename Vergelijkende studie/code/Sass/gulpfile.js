var gulp = require('gulp');
var sass = require('gulp-sass');


gulp.task('sass', function () {
  gulp.src('./3.15-opmaak-van-de-output/style.scss')     // replace with file you want to compile
    .pipe(sass({outputStyle: 'expanded'}).on('error', sass.logError))     // default outputStyle = nested, others are: expanded, compact and compressed
    .pipe(gulp.dest('./3.15-opmaak-van-de-output'));     // replace with folder where the compiled file should go
});

// gulp.task('sass:watch', function () {
//   gulp.watch('./css/**/*.scss', ['sass']);
// });
