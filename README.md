"# PADx-Skill-Scraper" 

Right now, needs to be run in a python interpreter so you can call the two main functions:

listMySkillInfo(cardNumList, dungeonsToExclude)
and 
checkForAvailableSkillups(normallyExcluded, alwaysInCoin, fullCardReportStr)

------------------------------------------ listMySkillInfo(cardNumList, dungeonsToExclude):
cardNumList = Python list of numbers of the mosnters you're interested in sklling up. E.g. [[1, 2, 3, 3000].
dungeonsToExclude = Python list of words. It will ignore any dungeon that has one of these words in its name.
	Suggested: dToE, which is ["Challenge", "Tournament"]

This function will output a tab-delimited list of information. I usually view it in microsoft excel. 

Example use:
>> listMySkillInfo([20, 200, 2000], dToE)
(Program runs, outputting some debugging info so you know it's doing something...)
Eventual output: 
Number	Name	farmableSkillUps	Normal or Technical dungeons	Other dungeons
20	Moondragon D'spinas	D'spinas && Moondragon Lunar D'spinas && Tiamat && Evil Dragon Helheim && Fog Chimera && Blazing Dark Tiamat && Flowing Dark Tiamat && Wooden Dark Tiamat && Lightning Dark Tiamat && Dark Twin Star Tiamat && Moondragon D'spinas && ├¿┬ú┬Å├ú┬â┬ò├ú┬é┬⌐├ú┬â┬â├ú┬é┬░├ú┬é┬¡├ú┬â┬₧├ú┬é┬ñ├ú┬â┬⌐ && Goggler	Others, Legendary Dragons' Footprints, Alt. Talos's Abyss, Mechdragons' Massive Fortress, Alt. Castle of Satan in Abyss, Forbidden Tower, Mystic Dragon Historic Site, Dragon Knight Sanctuary, Ancient Dragons' Mystic Realm, Talos's Abyss, Castle of Satan in the Abyss, Twilight Woods	Ultimate Dragon Rush!, Extreme Dragon Rush! 2, Extreme Dragon Rush!, Gift from Heaven, Ruins of the Star Vault, Santa Claus Descended!, Zeus Mercury Descended!, Rusted Mechdragon, Purple Flower Dragon, Noah Descended!, Light Insect Dragon, Dark Cat Dragon, Light Cat Dragon, October Quest Dungeon, Alt. Castle of Satan in Abyss, Alt. Talos's Abyss, Dark Insect Dragon, Legendary Evil Dragon, Legendary Dragon Rush!, Mephisto Descended!, Hera-Is Descended!, Ultimate Dragon Rush!, Princess Punt Collab
200	Blood Demon	Pyro Demon && Frost Devil && Frost Demon && Taur Devil && Taur Demon && Harpie Devil && Harpie Demon && Blood Devil && Blood Demon && Pyro Devil && ├¿┬ú┬Å├ú┬â┬æ├ú┬é┬ñ├ú┬â┬¡├ú┬â┬ç├ú┬â┬╝├ú┬â┬ó├ú┬â┬│ && Hellray Harpie Demon && ├¿┬ú┬Å├º┬ü┬½├º┬é┬Ä├º┬ì┬ä├ú┬â┬╗├ú┬â┬æ├ú┬é┬ñ├ú┬â┬¡├ú┬â┬ç├ú┬â┬╝├ú┬â┬ó├ú┬â┬│ && Hellice Frost Demon && Hellwind Taur Demon && Hellfire Pyro Demon && Helldark Blood Demon	Divine Queen's Sleepless Castle, Starlight Sanctuary, Jupiter, City in the Sky, Frozen Soil of Prosell, Vesta Cave, The Heroes' Hideout, Sky Dragons' Domain, Legendary Dragons' Footprints, Oceanus Falls, Hyperion Lava Flow, Tower of Nature, Tower of Flare, Ocean of Heaven, Kronos Forest, Polar Night Tower, Junos Island, Mars Crater, Tower to the Sky, Rhea-Themis Temple, Clayus Prison, The God-King's Floating Garden, Alt. Hemera Volcanic Belt, Alt. Temple of Trailokya, Alt. Shrine of Blazing Woods, Alt. Shrine of Liquid Flame, Tower of Blazing Fire, Forbidden Tower, Pirate Dragon's Hidden Grotto, Mystic Dragon Historic Site, Ancient Dragons' Mystic Realm, Mechdragons' Massive Fortress, Hemera Volcanic Belt, Temple of Trailokya, Shrine of Blazing Woods, Shrine of Liquid Flame, Blazing Highway, Alt. Aither Desert, Alt. Creek of Neleus, Aither Desert, Creek of Neleus, Alt. Talos's Abyss, Alt. Hypno Forest, Dragon Knight Sanctuary, Talos's Abyss, Hypno Forest, Tower of Ice Water, Ice Maze, Alt. Shrine of Green Water, Tower of Windy Woods, Shrine of Green Water, Fertile Land, Faithless Temple with No Name, Alt. Castle of Satan in Abyss, Castle of Satan in the Abyss, Twilight Woods	Lightless Devils' Nest, Scarlet Descended!, Linthia Descended!, Nordis Descended, Star Treasure Thieves' Den, Zeus (+297) Descended!, Hera (+297) Descended!, Hera Descended!, Zeus Descended!, Flame Mechdragon, Red Pirate Dragon, Poring Tower, Red Sprite, Alt. Shrine of Liquid Flame, Alt. Shrine of Blazing Woods, Alt. Temple of Trailokya, Alt. Starlight Sanctuary, Alt. Jupiter, City in the Sky, Alt. Frozen Soil of Prosell, Alt. Vesta Cave, Alt. Hemera Volcanic Belt, Fire Insect Dragon, September Quest Dungeon, Red Contract Dragon, Jormungandr Descended!, Aamir Descended!, Grimoires Descended!, Cauchemar Descended!, Hera-Sowilo Descended!, The Goddess Descended!, Hero Descended!, Legendary Flame Dragon, Sky Dragon of Flame, Scarlet Snake Princess, Sword of Flames, Alt. Oceanus Falls, Alt. Hyperion Lava Flow, Alt. Tower of Nature, Alt. Tower of Flare, Alt. Creek of Neleus, Alt. Aither Desert, October Quest Dungeon, Wood Guardian Dragon, Fire Guardian Dragon, Legendary Blizzard Dragon, Sky Dragon of Water, Blue Pirate Dragon, Blue Sprite, Alt. Ocean of Heaven, Alt. Kronos Forest, Alt. Polar Night Tower, Alt. Hypno Forest, Alt. Talos's Abyss, Water Insect Dragon, Light Guardian Dragon, Water Guardian Dragon, Hera-Is Descended!, Ice Mechdragon, Alt. Junos Island, Alt. Mars Crater, Blue Contract Dragon, Legendary Green Dragon, Sky Dragon of Wood, Green Pirate Dragon, Green Sprite, Dragon Guardian, Earth Insect Dragon, Wind Mechdragon, Alt. Shrine of Green Water, Green Contract Dragon, Legendary Mech Dragon, Sky Dragon of Light, Gold Pirate Dragon, Light Sprite, Gleaming Dragon, Blade of Justice, Dark-Breaking Wings, Alt. Tower to the Sky, Alt. Rhea-Themis Temple, Light Insect Dragon, Dark Guardian Dragon, Mephisto Descended!, Noble Mechdragon, Orange Contract Dragon, Dark Orb Dragon, Legendary Evil Dragon, Sky Dragon of Darkness, Black Pirate Dragon, Cold Steel, Shadow Sprite, Dragon in Motley, Dark Night Sword, Alt. Clayus Prison, Dark Insect Dragon, Rusted Mechdragon, Alt. Castle of Satan in Abyss, Black Contract Dragon
2000	Shinra Ultimate God Kai Card	Shinra Ultimate God Kai Card	.	Shinrabansho Choco Collab

Saving that to a string in Python and typing print myString.replace("\t", "\n") will split each thing up onto lines. E.g.:

>>> myString = """20	Moondragon D'spinas	D'spinas && Moondragon Lunar D'spinas && Tiamat && Evil Dragon Helheim && Fog Chimera && Blazing Dark Tiamat && Flowing Dark Tiamat && Wooden Dark Tiamat && Lightning Dark Tiamat && Dark Twin Star Tiamat && Moondragon D'spinas && ├¿┬ú┬Å├ú┬â┬ò├ú┬é┬⌐├ú┬â┬â├ú┬é┬░├ú┬é┬¡├ú┬â┬₧├ú┬é┬ñ├ú┬â┬⌐ && Goggler	Others, Legendary Dragons' Footprints, Alt. Talos's Abyss, Mechdragons' Massive Fortress, Alt. Castle of Satan in Abyss, Forbidden Tower, Mystic Dragon Historic Site, Dragon Knight Sanctuary, Ancient Dragons' Mystic Realm, Talos's Abyss, Castle of Satan in the Abyss, Twilight Woods	Ultimate Dragon Rush!, Extreme Dragon Rush! 2, Extreme Dragon Rush!, Gift from Heaven, Ruins of the Star Vault, Santa Claus Descended!, Zeus Mercury Descended!, Rusted Mechdragon, Purple Flower Dragon, Noah Descended!, Light Insect Dragon, Dark Cat Dragon, Light Cat Dragon, October Quest Dungeon, Alt. Castle of Satan in Abyss, Alt. Talos's Abyss, Dark Insect Dragon, Legendary Evil Dragon, Legendary Dragon Rush!, Mephisto Descended!, Hera-Is Descended!, Ultimate Dragon Rush!, Princess Punt Collab
200	Blood Demon	Pyro Demon && Frost Devil && Frost Demon && Taur Devil && Taur Demon && Harpie Devil && Harpie Demon && Blood Devil && Blood Demon && Pyro Devil && ├¿┬ú┬Å├ú┬â┬æ├ú┬é┬ñ├ú┬â┬¡├ú┬â┬ç├ú┬â┬╝├ú┬â┬ó├ú┬â┬│ && Hellray Harpie Demon && ├¿┬ú┬Å├º┬ü┬½├º┬é┬Ä├º┬ì┬ä├ú┬â┬╗├ú┬â┬æ├ú┬é┬ñ├ú┬â┬¡├ú┬â┬ç├ú┬â┬╝├ú┬â┬ó├ú┬â┬│ && Hellice Frost Demon && Hellwind Taur Demon && Hellfire Pyro Demon && Helldark Blood Demon	Divine Queen's Sleepless Castle, Starlight Sanctuary, Jupiter, City in the Sky, Frozen Soil of Prosell, Vesta Cave, The Heroes' Hideout, Sky Dragons' Domain, Legendary Dragons' Footprints, Oceanus Falls, Hyperion Lava Flow, Tower of Nature, Tower of Flare, Ocean of Heaven, Kronos Forest, Polar Night Tower, Junos Island, Mars Crater, Tower to the Sky, Rhea-Themis Temple, Clayus Prison, The God-King's Floating Garden, Alt. Hemera Volcanic Belt, Alt. Temple of Trailokya, Alt. Shrine of Blazing Woods, Alt. Shrine of Liquid Flame, Tower of Blazing Fire, Forbidden Tower, Pirate Dragon's Hidden Grotto, Mystic Dragon Historic Site, Ancient Dragons' Mystic Realm, Mechdragons' Massive Fortress, Hemera Volcanic Belt, Temple of Trailokya, Shrine of Blazing Woods, Shrine of Liquid Flame, Blazing Highway, Alt. Aither Desert, Alt. Creek of Neleus, Aither Desert, Creek of Neleus, Alt. Talos's Abyss, Alt. Hypno Forest, Dragon Knight Sanctuary, Talos's Abyss, Hypno Forest, Tower of Ice Water, Ice Maze, Alt. Shrine of Green Water, Tower of Windy Woods, Shrine of Green Water, Fertile Land, Faithless Temple with No Name, Alt. Castle of Satan in Abyss, Castle of Satan in the Abyss, Twilight Woods	Lightless Devils' Nest, Scarlet Descended!, Linthia Descended!, Nordis Descended, Star Treasure Thieves' Den, Zeus (+297) Descended!, Hera (+297) Descended!, Hera Descended!, Zeus Descended!, Flame Mechdragon, Red Pirate Dragon, Poring Tower, Red Sprite, Alt. Shrine of Liquid Flame, Alt. Shrine of Blazing Woods, Alt. Temple of Trailokya, Alt. Starlight Sanctuary, Alt. Jupiter, City in the Sky, Alt. Frozen Soil of Prosell, Alt. Vesta Cave, Alt. Hemera Volcanic Belt, Fire Insect Dragon, September Quest Dungeon, Red Contract Dragon, Jormungandr Descended!, Aamir Descended!, Grimoires Descended!, Cauchemar Descended!, Hera-Sowilo Descended!, The Goddess Descended!, Hero Descended!, Legendary Flame Dragon, Sky Dragon of Flame, Scarlet Snake Princess, Sword of Flames, Alt. Oceanus Falls, Alt. Hyperion Lava Flow, Alt. Tower of Nature, Alt. Tower of Flare, Alt. Creek of Neleus, Alt. Aither Desert, October Quest Dungeon, Wood Guardian Dragon, Fire Guardian Dragon, Legendary Blizzard Dragon, Sky Dragon of Water, Blue Pirate Dragon, Blue Sprite, Alt. Ocean of Heaven, Alt. Kronos Forest, Alt. Polar Night Tower, Alt. Hypno Forest, Alt. Talos's Abyss, Water Insect Dragon, Light Guardian Dragon, Water Guardian Dragon, Hera-Is Descended!, Ice Mechdragon, Alt. Junos Island, Alt. Mars Crater, Blue Contract Dragon, Legendary Green Dragon, Sky Dragon of Wood, Green Pirate Dragon, Green Sprite, Dragon Guardian, Earth Insect Dragon, Wind Mechdragon, Alt. Shrine of Green Water, Green Contract Dragon, Legendary Mech Dragon, Sky Dragon of Light, Gold Pirate Dragon, Light Sprite, Gleaming Dragon, Blade of Justice, Dark-Breaking Wings, Alt. Tower to the Sky, Alt. Rhea-Themis Temple, Light Insect Dragon, Dark Guardian Dragon, Mephisto Descended!, Noble Mechdragon, Orange Contract Dragon, Dark Orb Dragon, Legendary Evil Dragon, Sky Dragon of Darkness, Black Pirate Dragon, Cold Steel, Shadow Sprite, Dragon in Motley, Dark Night Sword, Alt. Clayus Prison, Dark Insect Dragon, Rusted Mechdragon, Alt. Castle of Satan in Abyss, Black Contract Dragon
2000	Shinra Ultimate God Kai Card	Shinra Ultimate God Kai Card	.	Shinrabansho Choco Collab"""

>>> print myString.replace("\t", "\n")
20
Moondragon D'spinas
D'spinas && Moondragon Lunar D'spinas && Tiamat && Evil Dragon Helheim && Fog Chimera && Blazing Dark Tiamat && Flowing Dark Tiamat && Wooden Dark Tiamat && Lightning Dark Tiamat && Dark Twin Star Tiamat && Moondragon D'spinas && Γö£┬┐Γö¼├║Γö¼├àΓö£├║Γö¼├óΓö¼├▓Γö£├║Γö¼├⌐Γö¼ΓîÉΓö£├║Γö¼├óΓö¼├óΓö£├║Γö¼├⌐Γö¼ΓûæΓö£├║Γö¼├⌐Γö¼┬íΓö£├║Γö¼├óΓö¼ΓéºΓö£├║Γö¼├⌐Γö¼├▒Γö£├║Γö¼├óΓö¼ΓîÉ && Goggler
Others, Legendary Dragons' Footprints, Alt. Talos's Abyss, Mechdragons' Massive Fortress, Alt. Castle of Satan in Abyss, Forbidden Tower, Mystic Dragon Historic Site, Dragon Knight Sanctuary, Ancient Dragons' Mystic Realm, Talos's Abyss, Castle of Satan in the Abyss, Twilight Woods
Ultimate Dragon Rush!, Extreme Dragon Rush! 2, Extreme Dragon Rush!, Gift from Heaven, Ruins of the Star Vault, Santa Claus Descended!, Zeus Mercury Descended!, Rusted Mechdragon, Purple Flower Dragon, Noah Descended!, Light Insect Dragon, Dark Cat Dragon, Light Cat Dragon, October Quest Dungeon, Alt. Castle of Satan in Abyss, Alt. Talos's Abyss, Dark Insect Dragon, Legendary Evil Dragon, Legendary Dragon Rush!, Mephisto Descended!, Hera-Is Descended!, Ultimate Dragon Rush!, Princess Punt Collab
200
Blood Demon
Pyro Demon && Frost Devil && Frost Demon && Taur Devil && Taur Demon && Harpie Devil && Harpie Demon && Blood Devil && Blood Demon && Pyro Devil && Γö£┬┐Γö¼├║Γö¼├àΓö£├║Γö¼├óΓö¼├ªΓö£├║Γö¼├⌐Γö¼├▒Γö£├║Γö¼├óΓö¼┬íΓö£├║Γö¼├óΓö¼├ºΓö£├║Γö¼├óΓö¼Γò¥Γö£├║Γö¼├óΓö¼├│Γö£├║Γö¼├óΓö¼Γöé && Hellray Harpie Demon && Γö£┬┐Γö¼├║Γö¼├àΓö£┬║Γö¼├╝Γö¼┬╜Γö£┬║Γö¼├⌐Γö¼├äΓö£┬║Γö¼├¼Γö¼├ñΓö£├║Γö¼├óΓö¼ΓòùΓö£├║Γö¼├óΓö¼├ªΓö£├║Γö¼├⌐Γö¼├▒Γö£├║Γö¼├óΓö¼┬íΓö£├║Γö¼├óΓö¼├ºΓö£├║Γö¼├óΓö¼Γò¥Γö£├║Γö¼├óΓö¼├│Γö£├║Γö¼├óΓö¼Γöé && Hellice Frost Demon && Hellwind Taur Demon && Hellfire Pyro Demon && Helldark Blood Demon
Divine Queen's Sleepless Castle, Starlight Sanctuary, Jupiter, City in the Sky, Frozen Soil of Prosell, Vesta Cave, The Heroes' Hideout, Sky Dragons' Domain, Legendary Dragons' Footprints, Oceanus Falls, Hyperion Lava Flow, Tower of Nature, Tower of Flare, Ocean of Heaven, Kronos Forest, Polar Night Tower, Junos Island, Mars Crater, Tower to the Sky, Rhea-Themis Temple, Clayus Prison, The God-King's Floating Garden, Alt. Hemera Volcanic Belt, Alt. Temple of Trailokya, Alt. Shrine of Blazing Woods, Alt. Shrine of Liquid Flame, Tower of Blazing Fire, Forbidden Tower, Pirate Dragon's Hidden Grotto, Mystic Dragon Historic Site, Ancient Dragons' Mystic Realm, Mechdragons' Massive Fortress, Hemera Volcanic Belt, Temple of Trailokya, Shrine of Blazing Woods, Shrine of Liquid Flame, Blazing Highway, Alt. Aither Desert, Alt. Creek of Neleus, Aither Desert, Creek of Neleus, Alt. Talos's Abyss, Alt. Hypno Forest, Dragon Knight Sanctuary, Talos's Abyss, Hypno Forest, Tower of Ice Water, Ice Maze, Alt. Shrine of Green Water, Tower of Windy Woods, Shrine of Green Water, Fertile Land, Faithless Temple with No Name, Alt. Castle of Satan in Abyss, Castle of Satan in the Abyss, Twilight Woods
Lightless Devils' Nest, Scarlet Descended!, Linthia Descended!, Nordis Descended, Star Treasure Thieves' Den, Zeus (+297) Descended!, Hera (+297) Descended!, Hera Descended!, Zeus Descended!, Flame Mechdragon, Red Pirate Dragon, Poring Tower, Red Sprite, Alt. Shrine of Liquid Flame, Alt. Shrine of Blazing Woods, Alt. Temple of Trailokya, Alt. Starlight Sanctuary, Alt. Jupiter, City in the Sky, Alt. Frozen Soil of Prosell, Alt. Vesta Cave, Alt. Hemera Volcanic Belt, Fire Insect Dragon, September Quest Dungeon, Red Contract Dragon, Jormungandr Descended!, Aamir Descended!, Grimoires Descended!, Cauchemar Descended!, Hera-Sowilo Descended!, The Goddess Descended!, Hero Descended!, Legendary Flame Dragon, Sky Dragon of Flame, Scarlet Snake Princess, Sword of Flames, Alt. Oceanus Falls, Alt. Hyperion Lava Flow, Alt. Tower of Nature, Alt. Tower of Flare, Alt. Creek of Neleus, Alt. Aither Desert, October Quest Dungeon, Wood Guardian Dragon, Fire Guardian Dragon, Legendary Blizzard Dragon, Sky Dragon of Water, Blue Pirate Dragon, Blue Sprite, Alt. Ocean of Heaven, Alt. Kronos Forest, Alt. Polar Night Tower, Alt. Hypno Forest, Alt. Talos's Abyss, Water Insect Dragon, Light Guardian Dragon, Water Guardian Dragon, Hera-Is Descended!, Ice Mechdragon, Alt. Junos Island, Alt. Mars Crater, Blue Contract Dragon, Legendary Green Dragon, Sky Dragon of Wood, Green Pirate Dragon, Green Sprite, Dragon Guardian, Earth Insect Dragon, Wind Mechdragon, Alt. Shrine of Green Water, Green Contract Dragon, Legendary Mech Dragon, Sky Dragon of Light, Gold Pirate Dragon, Light Sprite, Gleaming Dragon, Blade of Justice, Dark-Breaking Wings, Alt. Tower to the Sky, Alt. Rhea-Themis Temple, Light Insect Dragon, Dark Guardian Dragon, Mephisto Descended!, Noble Mechdragon, Orange Contract Dragon, Dark Orb Dragon, Legendary Evil Dragon, Sky Dragon of Darkness, Black Pirate Dragon, Cold Steel, Shadow Sprite, Dragon in Motley, Dark Night Sword, Alt. Clayus Prison, Dark Insect Dragon, Rusted Mechdragon, Alt. Castle of Satan in Abyss, Black Contract Dragon
2000
Shinra Ultimate God Kai Card
Shinra Ultimate God Kai Card
.
Shinrabansho Choco Collab



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
20	Moondragon D'spinas	Purple Flower Dragon, Light Insect Dragon, Legendary Dragon Rush!, October Quest Dungeon, Ultimate Dragon Rush!, Dark Insect Dragon
200	Blood Demon	Water Insect Dragon, Light Insect Dragon, October Quest Dungeon, Dark Orb Dragon, Earth Insect Dragon, Dark Insect Dragon, Nordis Descended, Fire Insect Dragon

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
