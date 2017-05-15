import os
import re

filePrefixes = ["imam", "priest", "Rabbi", "sufi", "blackreverend", "zenmonk"]
for fi in filePrefixes:
 output = os.popen('node twitterbot.js ' + fi).read()
 file = open(fi +"_output.txt","w")
 file.write(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",output).split()))
 file.close
#print ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",output).split())
