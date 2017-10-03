import requests, os, time, copy, re
from bs4 import BeautifulSoup



"""
right now does not check if your monster changes skill on evolution. Assumes you want skillups for that skill.
Needs to remind users to check which parts of the dungeon can drop the monster---does not currently catalog this.
ONly considers monsters "farmable" if they drop from a dungeon. Gungho collab PEM is not considered farmable here.
Also, it does NOT look for monsters that evolve into monsters that skill up your monsters. 
   This was problematic with padx, and you usually don't want to do that anyway. 
   
   Because of how padx uses template pages, program needs to know what page numbers are too high to be real:
   If pad ever gets over 100,000 monsters, the templateNumber variable below needs to be made higher.
"""
templateNumber = 100000


s = requests.Session()


# DEBUG STUFF =================================
debugOn = True

def tdTag(tag):
    if tag.name == "td" and tag.has_attr('class'):
        print "-------------------------------------"
        print tag
        print tag['class']
        #print "======================================="
        #if tag
    return tag.name == "td" and tag.has_attr('class')

def lineText(text):
    return "-------------------------------------\n" + text

def linePrint(text):
    print "-------------------------------------"
    print text

def debugPrint(text):
    if debugOn:
        if isinstance(text, basestring):
            print text.encode('utf-8')
        else:
            print text

# Non-debug functions ===============================:

# PADX Page reading: =====================


def findTagWithTextInFirstChild(tags, text):
    for tag in tags:
        #print tag.contents[0].getText()
        if text in tag.getText(): 
            '''
            print "---------------------------------------------- "
            print tag
            print tag.contents
            print tag.contents[0]     
            '''
            if text in str(tag.contents[0]):
            #if tag.contents[0].getText() and text in tag.contents[0].string:   
                return tag  
    print "WARNING: NO TAG FOUND for " + text



def tdSectionTag(tag):
    return tag.name == "td" and tag.has_attr('class') and tag['class'][0] == u"section"

def findTagWithTextInFirstChildOfType(tags, text, typ):
    #print tags
    for tag in tags:
        if tag.find(typ) and text in tag.find(typ).getText():
            return tag
        '''
        #print tag.contents[0].getText()
        if text in tag.getText(): 
            
            if text in str(tag.contents[0]):
            #if tag.contents[0].getText() and text in tag.contents[0].string:   
                return tag  '''
    print "WARNING: NO TAG FOUND for " + text



def selectTagsByNameAndAttrs(tags, name, attrDict):
    toReturn = []
    for tag in tags:
        if tag.name == name:
            for attr in attrDict:
                if tag.has_attr(attr) and " ".join(tag[attr]) == attrDict[attr]:
                    toReturn.append(tag)
    return toReturn
    
# Currently, "Certain descended dungeons during events (that also has an image) gets past this..."
def dungeonType(source):
    # takes a tr tag inside the Drop Locations Section
    #maybe = selectTagsByNameAndAttrs(source.find_all('td'), 'td', {"class":"title nowrap"})
    maybe = selectTagsByNameAndAttrs(source.find_all('img'), 'img', {"class":"dungeonxsmall"})
    maybe2 = selectTagsByNameAndAttrs(source.find_all('td'), 'td', {"class":"title nowrap"})
    if maybe and maybe2:
        dType = maybe[0]['src']
        dTypes = ["dungeon0", "normal", "special", "technical", "dungeon4", "ranking", "multiplayer"]
        if "dungeon" in dType:
            return dTypes[int(dType[dType.find("dungeon")+7])]
    return '' # Not a dungeon.

def dungeonName(source):
    # Assumes it is a dungeon!
    maybe = selectTagsByNameAndAttrs(source.find_all('td'), 'td', {"class":"title nowrap"})
    #print maybe
    return maybe[0].getText()
    #maybe = source.find_all('td')
    #print maybe[0]['class']



        
def getSkillInfo(cardNum, dungeonsToExclude):
    debugPrint("========================= Starting number: " + str(cardNum))
    cardName = ''
    # We DON'T start with orig_card in this so it will check that card's dungeon availability as well.
    cardsLookedAt = [] 
    origPage = s.get('http://puzzledragonx.com/en/monster.asp?n=' + str(cardNum))
    origCardPg = BeautifulSoup(origPage.text, 'html.parser')    
    #print cardPage_info.text.encode('utf-8')
    #trs = origCardPg.find_all('tr')
    SmSkillTag = findTagWithTextInFirstChild(origCardPg.find_all('tr'), "Same Skill")
    sameSkillMons = {}
    for tag in SmSkillTag.find_all('a'):
        nameFull = tag.find('img')['alt']
        num = int(nameFull[3:nameFull.find(' ')])
        name = nameFull[nameFull.find(' ')+1:]
        sameSkillMons[num] = name
    debugPrint(sameSkillMons)
    farmableSkillMons = {}
    #farmablePrevoSkillMons = {} # get skill on evolution, don't have yet
    dungeonBase = {"dungeon0":[], "normal":[], "special":[], "technical":[], 
                   "dungeon4":[], "ranking":[], "multiplayer":[]} # I still have no idea what dungeon4 is.
    skillupDungeons = copy.deepcopy(dungeonBase)
    dropDungeons = []
    #preSkillupDungeons = copy.deepcopy(dungeonBase)
    for mon in sameSkillMons:
        num = mon
        if num == cardNum:
            cardName = str(sameSkillMons[num])
        if not num in cardsLookedAt and int(num) < templateNumber:
            debugPrint("-------------------------------------")
            debugPrint("#" + str(num) + ", " + sameSkillMons[num])
            cardsLookedAt.append(num)
            cardPgInf = s.get('http://puzzledragonx.com/en/monster.asp?n=' + str(num))
            cardPg = BeautifulSoup(cardPgInf.text, 'html.parser')   
            dropTag = findTagWithTextInFirstChildOfType(cardPg.find_all(tdSectionTag), "Drop Locations for ", 'tr')
            sources = dropTag.find_all('tr')
            otherTiers = 0
            #preEvoNum = 0
            #preEvoName = ''
            dropDungeons = copy.deepcopy(dungeonBase)
            #prevoDropDungeons = copy.deepcopy(dungeonBase)
            for source in sources:
                #debugPrint(source.getText())
                dType = dungeonType(source)                
                if dType:
                    name = dungeonName(source)
                    include = True
                    for nm in dungeonsToExclude:
                        if nm in name:
                            include = False
                    if include and otherTiers == 0:
                        dropDungeons[dType] = dropDungeons[dType] + [dungeonName(source)]    
                    #if include and otherTiers == 1:
                    #    prevoDropDungeons[dType] = prevoDropDungeons[dType] + [dungeonName(source)]
                #elif "Evolution from " in source.getText():
                #    (preEvoNum, preEvoName) = getPreEvoInfoFromSource(source)
                #    if preEvoNum in sameSkillMons or preEvoNum in farmablePrevoSkillMons:
                #        otherTiers = 2 '''              
                elif "Other tiers of this card" in source.getText(): # Issue is that this can contain higher evos...
                    '''
                    if otherTiers == 2:
                        continue # we've already recorded these or will get these. Next skillupMon.
                    else:
                        otherTiers = 1 '''
                    continue                
            debugPrint(dropDungeons)
            
        hasDungeons = 0
        for key in dropDungeons:
            if dropDungeons[key]:
                hasDungeons = 1
                for dungeon in dropDungeons[key]:
                    if not dungeon in skillupDungeons[key]:
                        skillupDungeons[key] = skillupDungeons[key] + [dungeon]
        if hasDungeons:
            farmableSkillMons[mon] = sameSkillMons[mon]
    linePrint("farmableSkillMons: " + str(farmableSkillMons))
    linePrint("skillupDungeons: " + str(skillupDungeons))
    packed = (cardNum, cardName, farmableSkillMons, skillupDungeons)
    return packed


# THis is more for checking things!


def retrieveFrontPageSpecialDungeons():
    frontPage = s.get('http://puzzledragonx.com/')
    text = frontPage.text
    # We have to cut the home page down some to work with it, because
    # it has words like "Today" showing up repeatedly
    text = text[text.index("NA Puzzle &amp; Dragons Dungeon Schedule"):text.index("NA Puzzle &amp; Dragons Event Schedule")]
    # Just assuming it stays this way for now, hardcoding... 
    # Cut for even html boundaries so Beautiful Soup is clean
    text = text[text.index("<tr>"):text.rfind("</table>")]
    # Separate by date
    todayText = text[text.index("<tr>")+2:text.index("Tomorrow")]
    todayText = todayText[todayText.index("<tr>"):todayText.rfind("<tr>")] # Soup clean
    #debugPrint(lineText(todayText))
    tomorrowText = text[text.index("Tomorrow"):text.rfind('<div class="lineseparator">')]
    tomorrowText = tomorrowText[tomorrowText.index("<tr>"):tomorrowText.rfind("<tr>")] # Soup CLean
    #debugPrint(lineText(tomorrowText))
    futureText = text[text.rfind('<div class="lineseparator">'):text.rfind('adsbygoogle')]
    futureText = futureText[futureText.index("<tr>"):futureText.rfind("<tr>")] # Soup CLean    
    #debugPrint(lineText(futureText))
    # FOr now, just looking at today ........
    today = BeautifulSoup(todayText, 'html.parser')
    #myDungeonTrs = tod
    myDungeonTds = selectTagsByNameAndAttrs(today.find_all('td'), 'td', {"class":"eventname"})
    myDungeons = {} # (dungeonName, dungeonLink). COuld add dungeonDate eventually.
    for dng in myDungeonTds:
        dungeonName = dng.contents[0].get_text()
        link = "http://puzzledragonx.com/" + dng.a['href']
        #debugPrint((dungeonName, link))
        myDungeons[dungeonName] = link
    return myDungeons

def retrieveCoinDungeons(excludeThese):
    coinPage = s.get('http://www.puzzledragonx.com/en/coin-dungeons.asp')
    cP = coinPage.text
    # Sometimes padx displays current coin dungeon rotation and upcoming rotation.
    if cP.count("<h2>") > 1:
        #firstEndH2 = cP.find("</h2>")+5
        #section = cP[cP.find("</h2>")+5:]
        cP = cP[cP.find("</h2>")+5:]
        cP = cP[:cP.find("<h2>")]
    coinPg = BeautifulSoup(cP, 'html.parser')
    myLinks = coinPg.find_all('a')
    myDungeons = {}
    for tag in myLinks:
        #debugPrint(tag)
        if tag.has_attr('href') and "mission" in tag['href'] and tag.get_text():
            dungeonName = tag.get_text()
            if not dungeonName in excludeThese:
                link = "http://puzzledragonx.com/" + tag['href']
                #debugPrint((dungeonName, link))
                myDungeons[dungeonName]= link 
    return myDungeons

# NEEDS TESTING!
def allOtherSubdungeonPages(link):
    # link should be to one dungeon page.
    subPage = s.get(link)
    subPgTextSplits = subPage.text.split('<td class="section">')
    subPgText = ''
    for split in subPgTextSplits:
        if "<h2>Dungeon</h2>" in split:
            subPgText = split
            break
    subPg = BeautifulSoup(subPgText, 'html.parser')
    myLinks = subPg.find_all('a')
    myDungeons = {}
    for tag in myLinks:
        #debugPrint(tag)
        if tag.has_attr('href') and "mission" in tag['href'] and tag.get_text():
            dungeonName = tag.get_text()
            link = "http://puzzledragonx.com/" + tag['href']
            #debugPrint((dungeonName, link))
            myDungeons[dungeonName]= link    
    return myDungeons

def monstersDroppedInDungeon(link):
    dungeonPage = s.get(link)
    


            
            
            
    
    
    
    #for line in myCardLines:  
    # TODO!!!


# Formatting =============================================

def cardReport(cardNum, cardName, farmableSkillMons, skillupDungeons):
    # "Number\tName\tfarmableSkillUps\tNormal or Technical dungeons\tOther dungeons"
    cardLine = str(cardNum) + "\t" + cardName
    cardLine += "\t" + " && ".join(farmableSkillMons.values()) # Many card names have commas in them...
    normTech = skillupDungeons['normal'] + skillupDungeons['technical']
    if len(normTech):
        cardLine += "\t" + ", ".join(normTech) # I haven't seen a dungeon name that has a comma in it yet.
    else:
        cardLine += "\t."
    otherDungeons = []
    for key in skillupDungeons:
        if not key == "normal" and not key == "technical":
            otherDungeons += skillupDungeons[key]
    if len(otherDungeons):
        cardLine += "\t" + ", ".join(otherDungeons)
    else:
        cardLine += "\t."
    return cardLine

def isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
        
def readCardReport(reportStr):
    # "Number\tName\tfarmableSkillUps\tNormal or Technical dungeons\tOther dungeons"
    # packed = (cardNum, cardName, farmableSkillMons, skillupDungeons)
    splits = reportStr.split('\t')
    if len(splits) < 5:
        print "Warning: card report in wrong format!" # Not debug print. People need to know about this.
        return ""
    if not isInt(splits[0]):
        return "" # THis was a comment-line
    cardNum = int(splits[0])
    cardName = splits[1]
    farmableSkillMons = splits[2].split(" && ")
    # Marks everything as normal or other, because it doesn't store more detail.
    skillupDungeons = {}
    skillupDungeons['normal'] = splits[3].split(", ")
    skillupDungeons['other'] = splits[4].split(", ")
    debugPrint((cardNum, cardName, farmableSkillMons, skillupDungeons))
    return (cardNum, cardName, farmableSkillMons, skillupDungeons)
    

def cardReport2(packed):
    # packed = (cardNum, cardName, farmableSkillMons, skillupDungeons)
    # "Number\tName\tfarmableSkillUps\tNormal or Technical dungeons\tOther dungeons"
    (cardNum, cardName, farmableSkillMons, skillupDungeons) = packed
    return cardReport(cardNum, cardName, farmableSkillMons, skillupDungeons)




        
    

    

# ===================================== FUNCTIONS TO RUN =======================
# michael is 624
#cardNum = 1099

# Sample dungeonsToExclude: (these are not useful for visual checking)
dToE = ['Challenge', 'Tournament']
alwaysInCoin = ['Gungho Collab', 'Nordis Descended', 'Gainaut Descended!', 'Volsung Descended!', 'Scarlet Descended!', 'Linthia Descended!', 'Myr Descended!']

def listMySkillInfo(cardNumList, dungeonsToExclude):
    '''It will exclude any dungeons that have a word in their name that is in
    the dungeonsToExclude list. This is useful if you want to look at the list,
    because otherwise you get a billion challenge dungeons.'''
    myCardLines = []
    for num in cardNumList:
        myCardLines.append(cardReport2(getSkillInfo(num, dungeonsToExclude)))
    print "Number\tName\tfarmableSkillUps\tNormal or Technical dungeons\tOther dungeons"
    for cardLine in myCardLines:
        print cardLine.encode('utf-8')
        
        

# THis should go in functions to Call
# Currently, this DOES NOT manually check Challenge, Tournament for skillups.
# Note: throwing out 'Challenge' does hit a few real dungeons, I think.
def checkForAvailableSkillups(normallyExcluded, alwaysInCoin, fullCardReportStr):
    # Assumes that you don't want to be reminded of normal/technical dungeon skillups.
    # ignores any line that does not begin with a number.
    # normallyExcluded is usually ['Challenge', 'Tournament']. It tells the function to 
    # check any dungeon with this word in the name manually for skillups, instead 
    # of just checking dungeon name against input list.
    # alwaysInCoin tells it to exclude coin dungeons with that exact name.
    lines = fullCardReportStr.split('\n')
    # technically "my card lines with dungeons other than normal or technical dungeons": NOPE: not assuming you include temp dungeons in your list!
    # However, am assuming it knows all farmable skillup cards. So it is "myCardLines that have farmable skillups".
    myCardLines = [] 
    for line in lines:
        packed = readCardReport(line)
        if packed and len(packed[2])> 0: # Is a real card line and Has farmable skillups.
            myCardLines.append(packed)
    urgentCards   = {} # urgentCards[cardnum] = [urgent dungeons with skillups]    
    coinDungeons = retrieveCoinDungeons(alwaysInCoin) # We want to test if coin dungeon...
    
    frontDungeons = retrieveFrontPageSpecialDungeons()
    tempDungeons = retrieveCoinDungeons(alwaysInCoin)
    # Now Add in the front page, overwriting any coin dungeon ref to same dungeon, 
    # since we'd rather not pay coins if we don't have to.
    tempDungeons.update(retrieveFrontPageSpecialDungeons())
    for dng in tempDungeons:
        checkDrops = False
        for word in normallyExcluded:
            if word in dng:
                checkDrops = True 
                print "Hey, check my drops: " + dng
                print allOtherSubdungeonPages(tempDungeons[dng])
                # MAKE THAT DO SOMETHING: TODO
        for card in myCardLines:
            if checkDrops:
                x = 1 # Just to put something here for now...
            else:
                for key in card[3]:
                    if dng in card[3][key]:
                        name = dng
                        #if dng in coinDungeons and not dng in frontDungeons:
                        #    name = "Coin: " + dng                        
                        if card[0] in urgentCards:
                            urgentCards[card[0]].append(name)
                        else:
                            urgentCards[card[0]] = [name]
    print "reminder: Dungeons come from today's Special Dungeons, or the Coin Dungeons"
    print "CardNum\tCardName\tDungeonsAvailable"
    for card in myCardLines:
        if card[0] in urgentCards:
            print str(card[0]) + "\t" + card[1] + "\t" + ", ".join(urgentCards[card[0]])


# SCRATCH: rejected code that may yet someday be useful ===========


# From retrieveFrontPageSpecialDungeons() ==================
    """
    dungeonRE = re.compile('<tr><td class="eventdate"><span class="brown">(?P<sMonth>\d{2})/(?P<sDay>\d{2}) (?P<sHour>\d{2}):(?P<sMin>\d{2})</span>') #<br>(?P<endDate>.*)
    dungeonRE = re.compile('<tr><td class="eventdate"><span class="brown">(?P<sDate>\d{2}/\d{2} \d{2}:\d{2})</span>') #<br>(?P<endDate>.*)
    
    allDungeons =  re.finditer(dungeonRE, text)
        for dung in allDungeons:
            debugPrint(dung.groups())
            
        #dungeonRE = re.compile('<tr><td class="eventdate"><span class="brown">(?P<sMonth>.*)</span><br>(?P<endDate>.*)
    """
    # This may one day be more flexible, but probably not worth.
    """
    daysTextRaw = text.split('<div class="dateseparator">') 
    daysTextClean = [] 
    for rawDay in daysTextRaw:
        # Date Name, cleanText
        dayName = rawDay[:rawDay.index("</div>")] # NOte: may be blank
        cleanText = rawDay[rawDay.index("<tr>"):rawDay.rfind("<tr>")]
        daysTextClean.append((dayName, cleanText))
        debugPrint(lineText(dayName))
        debugPrint(cleanText)     
    debugPrint(lineText("Pre-fix"))
    # last one is a little messed up:
    (lastDay, ldt) = daysTextClean[len(daysTextClean)-1]
    daysTextClean[len(daysTextClean)-1] = (lastDay, ldt[:ldt.rfind("<tr>")])
    for day in daysTextClean: # NOte they may not be exactly days. Last one isn't.
        (dayName, cleanText) = day
        debugPrint(lineText(dayName))
        debugPrint(cleanText)        
    """   
   








        




    



    