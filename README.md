# WikiTalker

## A Toolkit to parse and analyse Wikipedia talk pages.

Please use the [WikiTalker/sample.json] file to dump the dataset in MongoDB. Make sure you have MongoDB installed and running on your system.

Depending upon the values you used in the [WikiTalker/analyzer.py] file, the data extraction commands (to fetch the saved data from the MongoDB server) will be as follows.

This is your MongoDB shell:
```sh
> use <name_of_wiki_database>
> db.<name_of_wiki_collection>.find({"id": <wiki_article_id>});
> db.<name_of_wiki_collection>.find({"revision_id": <comment_revision_id>});
```

If you do not change the [WikiTalker/analyzer.py] file and run it, all database and collection names will be as mentioned in the code. You can then run these commands.

This is your MongoDB shell:
```sh
> use mywikidump
> db.sample.find({"id": 1});
> db.sample.find({"revision_id": "901589438"});
```

[Grawitas] is a lightweight, fast parser for Wikipedia talk pages that takes the raw Wikipedia-syntax and outputs the structured content in various formats.

[WikiTalker/sample.json]: <https://github.com/descentis/WikiTalker/blob/master/WikiTalker/sample.json>
[WikiTalker/analyzer.py]: <https://github.com/descentis/WikiTalker/blob/master/WikiTalker/analyzer.py>
[GraWitas]: <https://github.com/bencabrera/grawitas>
