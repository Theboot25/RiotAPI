import json;
import urllib2
import os.path
import re;
import time
import operator;
from itertools import izip;
from collections import Counter;


base = {"Taliyah":0,"Jax":0,"Twisted Fate":0,"Udyr":0,"Rek'Sai":0,"Shaco":0,"Lucian":0,"Ivern":0,"Leona":0,"Caitlyn":0,"Zyra":0,"Azir":0,"Nocturne":0,"Kled":0,"Yasuo":0,"Brand":0,"Rammus":0,"Illaoi":0,"Corki":0,"Braum":0,"Fiddlestcks":0,"Anivia":0,"Rumble":0,"Tryndamere":0,"Skarner":0,"Kennen":0,"Urgot":0,"Wukong":0,"Amumu":0,"Galio":0,"Heimerdinger":0,"Xerath":0,"Vel'Koz":0,"Sivir":0,"Rengar":0,"Volibear":0,"Ashe":0,"Gangplank":0,"Talon":0,"Malphite":0,"Singed":0,"Ryze":0,"Miss Fortune":0,"Poppy":0,"Varus":0,"Twitch":0,"Kog'Maw":0,"Lee Sin":0,"Garen":0,"Zilean":0,"Blitzcrank":0,"Karthus":0,"Jayce":0,"Diana":0,"Trundle":0,"Sejuani":0,"Nidalee":0,"Elise":0,"Alistar":0,"Katarina":0,"Ekko":0,"Mordekaiser":0,"Graves":0,"Morgana":0,"Gnar":0,"Kha'Zix":0,"Lux":0,"Shyvana":0,"Jarvan IV":0,"Warwick":0,"Zac":0,"Camille":0,"Yorick":0,"Renekton":0,"Aatrox":0,"Draven":0,"Fiora":0,"Jinx":0,"Kalista":0,"Fizz":0,"Kassadin":0,"Sona":0,"Tahm Kench":0,"Vladimir":0,"Orianna":0,"Pantheon":0,"Riven":0,"Kindred":0,"Xin Zhao":0,"Cassiopeia":0,"Maokai":0,"Thresh":0,"Kayle":0,"Nami":0,"Taric":0,"Malzahar":0,"Darius":0,"Lissandra":0,"Nunu":0,"Bard":0,"Tristana":0,"Olaf":0,"Ziggs":0,"Irelia":0,"Mecarim":0,"Jhin":0,"Soraka":0,"Karma":0,"Annie":0,"Akali":0,"LeBlanc":0,"Syndra":0,"Veigar":0,"Cho'Gath":0,"Janna":0,"Nautilus":0,"Evelynn":0,"Gragas":0,"Zed":0,"Shen":0,"Vi":0,"Viktor":0,"Lulu":0,"Teemo":0,"Dr. Mundo":0,"Master Yi":0,"Swain":0,"Ahri":0,"Aurelion Sol":0,"Quinn":0,"Sion":0,"Vayne":0,"Nasus":0,"Ezreal":0};


if os.path.isfile('test.json') == False:
	with open("test.json","a+") as outfile:
		json.dump(base, outfile);
	
if os.path.isfile('test.json') == True:
	with open('test.json') as json_data:
		d = json.load(json_data)
		print "check";

def getJSONReply(URL):
    response = urllib2.urlopen(URL);
    html = response.read();
    data = json.loads(html);
    return data;
	
test="https://na.api.pvp.net/api/lol/na/v2.5/league/master?type=RANKED_SOLO_5x5&api_key=RGAPI-BC4FC362-6747-438F-A23F-805B21AF6E77";
#print test;
mh_data=getJSONReply(test);
test1=mh_data['entries'];

IDs = [];
matches = [];
x=0;
while x < 400:
	IDs.append(test1[x]['playerOrTeamId']);
	matches.append("https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/" + IDs[x]+  "/recent?api_key=RGAPI-BC4FC362-6747-438F-A23F-805B21AF6E77");
	x = x + 1;
#print IDs;
#print matches;


#matches_list['games'][y]['championId']
#matches_list['games'][y]['gameId']
#matches_list['games'][y]['fellowPlayers'][z]['summonerId']

championIDs = [];
total = 0;
x = 0;
y = 0;
while x < 180:
	matches_list=getJSONReply(matches[x]);
	while y < 10:
		championIDs.append(matches_list['games'][y]['championId']);
		#print matches_list['games'][y]['gameId'];
		y = y + 1;
		z = 0;
	x = x + 1;
	y = 0;
	time.sleep(2);
#print championIDs;

CID=Counter(championIDs).items();
CID = list(CID);
#print CID;

CName = [];
x=0;
while x < len(CID):
	names="https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(CID[x][0])+ "?api_key=RGAPI-BC4FC362-6747-438F-A23F-805B21AF6E77";
	#print names;
	names_list=getJSONReply(names);
	championName=names_list['name'];
	#print championName;
	CName.append(championName);
	CName.append(str(CID[x][1]));
	x = x + 1;
	
#print CName;

i = iter(CName);
Data = dict(izip(i, i));

i = iter(CName);
stringData = dict(izip(i, i));

Data = dict((k,int(v)) for k,v in stringData.iteritems());


FinalData = Counter();
A = Counter(d);
B = Counter(Data);

FinalData.update(A);
FinalData.update(B);

FinalData = dict(FinalData);
#print FinalData;
	
with open("test.json","w") as outfile:
	json.dump(FinalData, outfile);    

sorted_Data = sorted(FinalData.items(), key=operator.itemgetter(1), reverse = True);
print sorted_Data;
