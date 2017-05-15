var fs = require('fs');

// Requirements --------------------------------------
var twit = require('twit');
var config = require('./config.js');
var filePrefixes = ["imam", "priest", "Rabbi", "sufi", "black reverend", "zen monk"]
//Globals --------------------------------------------
//prevents reoccuring tweets, should be moved inside of the search function when scaled up
var timeLine = [];

//Program --------------------------------------------
//Import Twitter login settings
var Twitter = new twit(config);

//Finds hashtags in each text file and gets the latest ones
filePrefixes.forEach(function(val,index){
var hashtags = fs.readFileSync(val+'.txt', 'utf8').split(",");
var searchTweets = function(tag) {

  var params = {
    q: tag,
    result_type: 'recent',
    lang: 'en'
  }
Twitter.get('search/tweets', params, function(err, data) {
      // if there no errors

        if (!err) {
          var tweets = data.statuses;
          for (var i = 0; i < tweets.length; i++) {
            if (!timeLine.includes(tweets[i].text)){
              timeLine.push(tweets[i].text);
              console.log(tweets[i].text);
            }
          }
          //console.log(data);
        }
        // if unable to Search a tweet
        else {
          console.log('Could not Search...');
        }
    });
}

//Run Once, search through each hashtag
for (var i = 0; i < hashtags.length; i++) {
  searchTweets(hashtags[i]);

}
})
