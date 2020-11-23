import pywikibot as pw
import os
import subprocess
import json


# This function brings the whole talkpage with revisions of given name(line) 
#  in a revision object of pywikibot
def fetchTalkPage( line ):
    pageName = line
    name = 'Talk:' + line
    site = pw.Site('en', 'wikipedia')
    page = pw.Page(site, name)
    return page

# To convert a list of dictionary into json and dump
def convetTojson(name,Mypage):
    with open((name+".json"), "w") as outfile: 
        json.dump(Mypage, outfile) 


# reading the talk page as each revision and seperating out comments and return a list of {revision_id,comments}
def generateDump( page,name):
    fileName = 'talk_page_file' + '.wikimd'
    Mypage = []
    revs = page.revisions(content=True, reverse=True)
    for rev in revs:
        key=(rev['revid'])    
        with open(fileName, "w", encoding="utf-8") as f:
            f.write(rev['slots']['main']['*'])
            f.close()
        s=subprocess.check_call("./grawitas_cli_core --input-talk-page-file talk_page_file.wikimd --comment-list-json comment_list_file.json",shell = True)
        with open('comment_list_file.json', 'r') as openfile:
            json_object = json.load(openfile)
        for i  in range(len(Mypage)):
            dic=Mypage[i]
            if dic["revid"]==key:
                Mypage[i]["comments"].extend(json_object)
                continue
        curr = {"revid":key,"comments":json_object}
        Mypage.append(curr)
    return Mypage   
            

    

# read the given input file and generate dump
with open('talk_page_list.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        name = 'Talk:' + line
        page = fetchTalkPage(line)
        Allrevs=generateDump(page,name)
        convetTojson(name,Allrevs)
        print(line ,'-Done')
