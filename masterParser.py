import os

filePrefixes = ["imam", "priest", "Rabbi", "sufi", "blackreverend", "zenmonk"]
for fi in filePrefixes:
 output = os.popen('node twitterbot.js ' + fi).read()
print output
