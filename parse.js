const fs = require('fs');

const babelCode = fs.readFileSync('babel.min.js', 'utf-8');
const htmlCode = fs.readFileSync('index.html', 'utf-8');
const match = htmlCode.match(/<script type=\"text\/babel\">([\s\S]*?)<\/script>/);
let scriptContent = match && match[1];

let result = undefined;
try {
  // Mock window and document to evaluate babel
  const window = {};
  const navigator = {};
  const process = { env: {} };
  eval(babelCode);
  
  result = Babel.transform(Array(484).join('\n') + scriptContent, { presets: ['react'] });
  console.log("Success!");
} catch (e) {
  console.log("ERROR:\n", e.message);
}
