"# PADx-Skill-Scraper" 

NOTE: README is much more legible in RAW form...

Right now, needs to be run in a python interpreter so you can call the two main functions:

listMySkillInfo(cardNumList, dungeonsToExclude)
and 
checkForAvailableSkillups(normallyExcluded, alwaysInCoin, fullCardReportStr)

------------------------------------------ listMySkillInfo(cardNumList, dungeonsToExclude):

cardNumList = Python list of numbers of the mosnters you're interested in skilling up. E.g. [[1, 2, 3, 3000].

dungeonsToExclude = Python list of words. It will ignore any dungeon that has one of these words in its name.
	Suggested: dToE, which is ["Challenge", "Tournament"]
	
This function will output a tab-delimited list of information. I usually view it in microsoft excel. 

Example use:

>> listMySkillInfo([1330, 1336], dToE)

(Program runs, outputting some debugging info so you know it's doing something...)
Eventual output: 

Number	Name	farmableSkillUps	Normal or Technical dungeons	Other dungeons
1330	Krishna	Flame Insect Dragon, Flammesickle	.	Herme Descended!, Fire Insect Dragon, Wood Guardian Dragon
1336	Ganesha	Entrepreneur, Lex Luthor && Genius Scientist, Lex Luthor	.	Batman vs Superman Collab

Saving that to a string in Python and typing print myString.replace("\t", "\n") will split each thing up onto lines. E.g.:

>>> myString = myString = """Number	Name	farmableSkillUps	Normal or Technical dungeons	Other dungeons
1330	Krishna	Flame Insect Dragon, Flammesickle	.	Herme Descended!, Fire Insect Dragon, Wood Guardian Dragon
1336	Ganesha	Entrepreneur, Lex Luthor && Genius Scientist, Lex Luthor	.	Batman vs Superman Collab"""

>>> print myString.replace("\n", '\n-----\n').replace("\t", "\n")
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
Batman vs Superman Collab


------------------------------------------ checkForAvailableSkillups(normallyExcluded, alwaysInCoin, fullCardReportStr)

normallyExcluded = what you put on dungeonsToExclude when making the cardReport. 
	Not relevant yet, but eventually may check if any of those kinds of dungeons are available.
	
alwaysInCoin = list of coin dungeons that you don't want to be told about (presumably because they're always there.).
	A global variable named "alwaysInCoin" lists the level-up mechanics dungeons.
	
fullCardReportString = Python string containing the cardReport you got as output of listMySkillInfo. 
	Will ignore all lines that don't begin with a number, so feel free to annotate it.
	
This function reports what cards in your cardReport have farmable skillups from the current "special" or "coin"
dungeons, again tab-delimited.

Example use: (remember "myString" from above?):

>>> checkForAvailableSkillups(dToE, alwaysInCoin, myString) 

CardNum	CardName	DungeonsAvailable
1330	Krishna	Fire Insect Dragon

[This was run 10/3/2017. Your results will vary with what dungeons are currently available!]




------------------------------------------ checkForAvailableSkillups(normallyExcluded, alwaysInCoin, fullCardReportStr)

DISCLAIMERS:

big disclaimer:
This program is only as smart as the website it scrapes from, PADx. 
If PADx doesn't know, or formats it really weirdly, the program doesn't know.

--Does not handle Japanese characters well yet. 
--Right now does not check if your monster changes skill on evolution. Assumes you want skillups for that skill.
--Only reports the name of the dungeon the monster drops from, not which specific level(s) of the dungeon it drops from.
--Only considers monsters "farmable" if they drop from a dungeon. Gungho collab PEM is not considered farmable here.
--Does NOT document monsters that evolve into monsters that skill up your monsters. 
   (This was problematic with padx, and you usually don't want to do that anyway, because it's miserably time-consuming.).
   
   
NOTE:
   Because of how padx uses template pages, program needs to know what page numbers are too high to be real:
   If pad ever gets over 100,000 monsters, the templateNumber variable below needs to be made higher.
