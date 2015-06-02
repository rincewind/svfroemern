
var fs = require('fs');
var path = require('path');
var cssnext = require('cssnext');
  var postcss = require('postcss');
//var Cleancss = require('clean-css');

var removeComments = postcss.plugin('remove-comments', function(opts) {
  opts = opts || {};
  return function(root) {
    root.eachComment(function(comment) {
      comment.removeSelf();
    });
  }
});

var dir = path.join(__dirname, './css_src/');
var dest = path.join(__dirname, './css/');

var src = fs.readFileSync(dir + 'base.css', 'utf8');

  var css = cssnext(src, {
    features: {
      customProperties: {
        strict: false, // disable variable fallbacks from being redundantly added
      },
      rem: false,
      pseudoElements: false,
      colorRgba: false,

    }
  });
  //css = meta + '\n\n' + postcss().use(removeComments()).process(css).css;
  //var minified = new Cleancss({
  //    advanced: false,
  //  }).minify(css).styles;

  css = postcss().use(removeComments()).process(css).css;

  fs.writeFileSync(dest + 'svfroemern.css', css);

