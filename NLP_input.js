var fs = require('fs');

//Example to get all the text from one of the personalities for training an algorithm
var wordList=JSON.parse(fs.readFileSync("sufi_wordList.json", 'utf8'));
console.log(wordList.join(" "))
// paste wordList.join(" ") at the input for your Natural Language Parsing application
