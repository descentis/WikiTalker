import pywikibot as pw
import os
import subprocess


pageName = 'India'
name = 'Talk:'+pageName

# fetch the given page using pywikibot
page = pw.Page(pw.Site('en', 'wikipedia'), name)
text = page.get()
fileName = 'talk_page_file'+'.wikimd'
f=open(fileName, "w")
f.write(text)
f.close()


# Run the parser to generate the json file 
s=subprocess.check_call("./grawitas_cli_core --input-talk-page-file talk_page_file.wikimd --comment-list-json comment_list_file.json",shell = True)
jsonFilename = pageName+'.json'
os.rename('comment_list_file.json', jsonFilename)

