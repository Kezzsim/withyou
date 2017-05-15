import os
import re

filePrefixes = ["imam", "priest", "Rabbi", "sufi", "blackreverend", "zenmonk"]
for fi in filePrefixes:
 output = os.popen('node twitterbot.js ' + fi).read()

print ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",output).split()) 
