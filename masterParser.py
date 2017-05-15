import	os
import	glob
import	re
import	json

#Add your new personalities here, make sure you also add the text file with the same name to the directory
filePrefixes	=	["imam",	"priest",	"Rabbi",	"sufi",	"blackreverend",	"zenmonk"]

for	fi	in	filePrefixes:
    #fi is the name of each personality, as listed in the array above
	output	=	os.popen('node	twitterbot.js	'	+	fi).read()
	fileName=fi+'_wordList.json'
    #Pass argument personality into the JS file for talking to twitter, loop through each personality
	if(glob.glob(fileName)):
					wordSet	=	set(json.loads(open(fileName).read()))
	else:
					wordSet=set()

	wordList=	re.sub("(@[A-Za-z0-9']+)|([^0-9A-Za-z	\t])|(\w+:\/\/\S+)","	",output)
	for	word	in	wordList.split("	"):
								wordSet.add(word)
	f	=	open(fileName,	'w')
	f.write(json.dumps(list(wordSet)))
	f.close()
