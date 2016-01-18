var gulp = require('gulp');
var sass = require('gulp-sass');


gulp.task('sass', function () {
  gulp.src('./css/3.9-overerving-van-selectors/style.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./css/3.9-overerving-van-selectors'));
});

gulp.task('sass:watch', function () {
  gulp.watch('./css/**/*.scss', ['sass']);
});
