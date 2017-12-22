# PADx-Skill-Scraper
This program helps organize the hunt for skillups for monsters in Puzzle and
Dragons.



<h2>Capabilities</h2>

This program helps organize the hunt for skillups for monsters in Puzzle and
Dragons. It has two main capabilities:

1. listMySkillInfo <inputFile> <outputFile> [-dteS]

    Takes a file <inputFile> with lines beginning with monsternums, and
    possibly other things after the monsternum. Lists skillup monsters and 
    skillup dungeons for that monster in <outputFile> (may be same file. 
    Will also preserve lines beginning with #.), by scraping PADX. 
    If dteS is included, does not include dungeons with names that contain any
	of the words listed in the dungeonsToExclude setting under 
    PADskillGetterSettings.txt.  Example usage:
       listMySkillInfo monsters.txt monsters.txt -dteS
	   
2. checkForTempSkillups <skillInfoInputFile> <outputFile> [-cteS]

    Takes a file <skillInfoInputFile> that was generated by listMySkillInfo.
    Scrapes PADX to see if any of the dungeons listed as non-normal and 
	non-technical skillup dungeons in that file are currently available 
	in the 'special' or the 'coin' sections, and saves its findings to 
	<outputFile>. If -cteS is included, does not report dungeons in 
	the 'coin' section that are listed in the alwaysInCoin setting in 
    PADskillGetterSettings.txt. Example usage:
       checkForTempSkillups monsters.txt availableToday.txt -cteS

	   
<h2>Requirements</h2>

PADx-Skill-Scraper is written in Python 2.7. It requires the following non-standard
library packages: 
* [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [requests](https://pypi.python.org/pypi/requests)

If you have pip, these are installable with py -2 -m pip install <packagename>.

<h2>Usage</h2>

Typically, the programs menu system should be sufficient. The two main functions
are listMySkillInfo(cardNumList, dungeonsToExclude) and
checkForAvailableSkillups(normallyExcluded, alwaysInCoin, fullCardReportStr),
which the menus will set up calls to. More information on these below.

<h3> listMySkillInfo(cardNumList, dungeonsToExclude) </h3>

cardNumList = Python list of numbers of the monsters you're interested in
skilling up. E.g. [1, 2, 3, 3000].

dungeonsToExclude = Python list of words. It will ignore any dungeon that has
one of these words in its name.  
    Suggested: dToE, which is ["Challenge", "Tournament"]  
This function will output a tab-delimited list of information. I
usually view it in microsoft excel.

Example use:

```\>\> listMySkillInfo([1330, 1336], dToE)```

(Program runs, outputting some debugging info so you know it's doing
something...) Eventual output:

```Number	Name	farmableSkillUps	Normal or Technical dungeons	Other dungeons  
1330	Krishna	Flame Insect Dragon, Flammesickle	.	Herme Descended!, Fire Insect Dragon, Wood Guardian Dragon  
1336	Ganesha	Entrepreneur, Lex Luthor && Genius Scientist, Lex Luthor	.	Batman vs Superman Collab  
```

Saving that to a string in Python and typing print myString.replace("\t", "\n") will split each thing up onto lines. E.g.:

```
\>\> myString = """Number	Name	farmableSkillUps	Normal or Technical dungeons	Other dungeons  

1330	Krishna	Flame Insect Dragon, Flammesickle	.	Herme Descended!, Fire Insect Dragon, Wood Guardian Dragon  
1336	Ganesha	Entrepreneur, Lex Luthor && Genius Scientist, Lex Luthor	.	Batman vs Superman Collab"""  

\>\> print myString.replace("\n", '\n-----\n').replace("\t", "\n")

Number
Name  
farmableSkillUps  
Normal or Technical dungeons  
Other dungeons  
-----  
1330  
Krishna  
Flame Insect Dragon, Flammesickle  
.  
Herme Descended!, Fire Insect Dragon, Wood Guardian Dragon  
-----  
1336  
Ganesha  
Entrepreneur, Lex Luthor && Genius Scientist, Lex Luthor  
.  
Batman vs Superman Collab  ```

<h3>checkForAvailableSkillups(normallyExcluded, alwaysInCoin, fullCardReportStr)</h3>

normallyExcluded = what you put on dungeonsToExclude when making the cardReport.
Not relevant yet, but eventually may check if any of those kinds of dungeons are
available.  

alwaysInCoin = list of coin dungeons that you don't want to be told
about (presumably because they're always there.). A global variable named
"alwaysInCoin" lists the level-up mechanics dungeons. 

fullCardReportString =
Python string containing the cardReport you got as output of listMySkillInfo.
Will ignore all lines that don't begin with a number, so feel free to annotate
it. This function reports what cards in your cardReport have farmable skillups
from the current "special" or "coin" dungeons, again tab-delimited.

Example use: (remember "myString" from above?):

'''\>\> checkForAvailableSkillups(dToE, alwaysInCoin, myString)

CardNum CardName DungeonsAvailable 1330 Krishna Fire Insect Dragon'''

[This was run 10/3/2017. Your results will vary with what dungeons are currently
available!]



<h2>Disclaimers</h2>

IMPORTANT NOTES

1. the file PADskillGetterSettings.txt MUST be in the same directory as the
program if you want to use the optional dungeon-excludes form the menu. 

2. If you do not have python, Windows users can run the program using
padxSkillGetter.exe under the dist folder. You will need all of the build and
dist folders to do so.

3. I typically view the results by pasting into excel.

DISCLAIMERS:

big disclaimer: 

This program is only as smart as the website it scrapes from,
PADx. If PADx doesn't know, or formats it really weirdly, the program doesn't
know. For example, if PADx starts categorizing technical dungeons as
'multiplayer dungeons', that is where they will show up.

Smaller disclaimers:

* Does not handle Japanese characters well yet.
* Right now does not check if your monster changes skill on evolution. Assumes
you want skillups for that skill.
*Only reports the name of the dungeon the monster drops from, not which
specific level(s) of the dungeon it drops from.
*Only considers monsters "farmable" if they drop from a dungeon. Gungho collab
PEM is not considered farmable here.
* Does NOT document monsters that evolve into monsters that skill up your
monsters. (This was problematic with padx, and you usually don't want to do that
anyway, because it's miserably time-consuming.).
* Because of how padx uses template pages, program needs to know what page
numbers are too high to be real: If pad ever gets over 100,000 monsters, the
templateNumber variable needs to be made higher.


