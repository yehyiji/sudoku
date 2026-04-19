const Babel = require('babel-standalone');
const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf-8');
const match = html.match(/<script type=\"text\/babel\">([\s\S]*?)<\/script>/);

let code = match[1];

// Babel standalone actually pads the script if it extracts from DOM, but here we just transpile manually
try {
  Babel.transform(Array(484).join('\n') + code, { presets: ['react'] });
  console.log("Success");
} catch(e) {
  console.log(e.message);
}
