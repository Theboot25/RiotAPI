import json;
import urllib2
import os.path
import re;
import time
import operator;
from itertools import izip;
from collections import Counter;

APIkey = raw_input('Enter your Riot API key: ')
print "Please wait while we pull the data. This could take a few minutes due to Riot's API restrictions.";
base = {}

if os.path.isfile('KRRiotDatabase.json') == False:
	with open("KRRiotDatabase.json","a+") as outfile:
		json.dump(base, outfile);
	
if os.path.isfile('KRRiotDatabase.json') == True:
	with open('KRRiotDatabase.json') as json_data:
		d = json.load(json_data)
		#print "check";

def getJSONReply(URL):
    response = urllib2.urlopen(URL);
    html = response.read();
    data = json.loads(html);
    return data;
	
test="https://kr.api.riotgames.com/api/lol/KR/v2.5/league/master?type=RANKED_SOLO_5x5&api_key=" + APIkey;
#print test;
mh_data=getJSONReply(test);
test1=mh_data['entries'];

IDs = [];
matches = [];
x=0;
while x < 400:
	IDs.append(test1[x]['playerOrTeamId']);
	matches.append("https://kr.api.riotgames.com/api/lol/KR/v1.3/game/by-summoner/" + IDs[x]+  "/recent?api_key=" + APIkey);
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
while x < 150:
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
	names="https://global.api.pvp.net/api/lol/static-data/KR/v1.2/champion/" + str(CID[x][0])+ "?api_key=" + APIkey;
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
	
with open("KRRiotDatabase.json","w") as outfile:
	json.dump(FinalData, outfile);    

sorted_Data = sorted(FinalData.items(), key=operator.itemgetter(1), reverse = True);
print '\n';
print sorted_Data;
