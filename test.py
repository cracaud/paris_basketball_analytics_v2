import mysql.connector
import pandas as pd
import numpy as np

mydb = mysql.connector.connect(
  host="aws.connect.psdb.cloud",
  user="3ysp4iy6u7i4fjxkl778",
  password="pscale_pw_zoCO9O3nmho171us0ql8Z3CTAdNWaV7w9GGq3awGXxD",
  database="sdeng"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM actions WHERE a1 = 'Aamir Simms'")

datalist = mycursor.fetchall()

# START OF SCRIPT

datalist = pd.DataFrame(datalist, columns=['id', 'season_id', 'edition_id', 'game_id', 'action_number', 'period',
                                                   'home_score', 'away_score', 'remaining_period_time', 'action', 'player_id',
                                                   'team_id', 'opponent_id', 'x', 'y', 'details', 'linked_action_number',
                                                   'h1', 'h2', 'h3', 'h4', 'h5', 'a1', 'a2', 'a3', 'a4', 'a5', 'location'])

def f(row):
    if row['h1'] == "Aamir Simms" or row['h1'] == "Axel Toupane" or row['h1'] == "Ismael Kamagate" or row['h1'] == "Kyle Allman" or row['h1'] == "Tyrone Wallace" or row['h1'] == "Gauthier Denis" or row['h1'] == "Amar Gegic" or row['h1'] == "Dustin Sleva" or row['h1'] == "Chris Goulding" or row['h1'] == "Juhann Begarin" or row['h1'] == "Jeremy Evans" or row['h1'] == "Michael Roll" or row['h1'] == "Alfonso Plummer" or row['h1'] == "Mohamed Diawara" or row['h1'] == "Killian Malwaya" or row['h1'] == "Mael Hamon-Crespin" or row['h1'] == "Kevan Moreno" or row['h1'] == "Jean Noba":
        val = row[['h1','h2','h3','h4','h5']].values.tolist()
    elif row['a1'] == "Aamir Simms" or row['a1'] == "Axel Toupane" or row['a1'] == "Ismael Kamagate" or row['a1'] == "Kyle Allman" or row['a1'] == "Tyrone Wallace" or row['a1'] == "Gauthier Denis" or row['a1'] == "Amar Gegic" or row['a1'] == "Dustin Sleva" or row['a1'] == "Chris Goulding" or row['a1'] == "Juhann Begarin" or row['a1'] == "Jeremy Evans" or row['a1'] == "Michael Roll" or row['a1'] == "Alfonso Plummer" or row['a1'] == "Mohamed Diawara" or row['a1'] == "Killian Malwaya" or row['a1'] == "Mael Hamon-Crespin" or row['a1'] == "Kevan Moreno" or row['a1'] == "Jean Noba":
        val = row[['a1','a2','a3','a4','a5']].values.tolist()
    else:
        val = "ERROR"
    return val
datalist['lineup'] = datalist.apply(f, axis=1)

datalist['x'] = datalist['x'].astype(float)
datalist['y'] = datalist['y'].astype(float)
def distance(row):
    if row['x'] != 0 and row['y'] != 0:
        val = (np.sqrt(row['x']**2 + row['y']**2))
    elif row['x'] == 0 and row['y'] != 0:
        val = (np.sqrt(row['y']**2))
    elif row['x'] != 0 and row['y'] == 0:
        val = (np.sqrt(row['x']**2))
    elif row['x'] is None and row['y'] is None:
        val = 0
    elif row['x'] is None and row['y'] != 0:
        val = (np.sqrt(row['y']**2))
    elif row['x'] != 0 and row['y']is None:
        val = (np.sqrt(row['x']**2))
    else:
        val = 0
    return val
datalist['distance'] = datalist.apply(distance, axis=1)

def f(row):
    if row['distance'] > 6.75:
        val = "3pts"
    elif row['distance'] > 4.5:
        val = "Long 2"
    elif row['distance'] > 2.5:
        val = "Short 2"
    elif row['distance'] > 1.2:
        val = "Paint"
    elif row['distance'] > 0:
        val = "Rim"
    else:
        val = "ERROR"
    return val
datalist['zone_details'] = datalist.apply(f, axis=1)
        
def ListToString(row):
    if len(row['lineup']) != 0:
        val = ' - '.join(row['lineup'])
    else:
        val = "ERROR"
    return val
datalist['lineup_string'] = datalist.apply(ListToString, axis=1)

def Rim_Made(row):
    if row['zone_details'] == "Rim" and row['action'] == "2FGM":
        val = 1
    else:
        val = 0
    return val
datalist['Rim_Made'] = datalist.apply(Rim_Made, axis=1)

def Rim_Miss(row):
    if row['zone_details'] == "Rim" and row['action'] == "2FGA":
        val = 1
    else:
        val = 0
    return val
datalist['Rim_Miss'] = datalist.apply(Rim_Miss, axis=1)

def Paint_Made(row):
    if row['zone_details'] == "Paint" and row['action'] == "2FGM":
        val = 1
    else:
        val = 0
    return val
datalist['Paint_Made'] = datalist.apply(Paint_Made, axis=1)

def Paint_Miss(row):
    if row['zone_details'] == "Paint" and row['action'] == "2FGA":
        val = 1
    else:
        val = 0
    return val
datalist['Paint_Miss'] = datalist.apply(Paint_Miss, axis=1)

def Short2_Made(row):
    if row['zone_details'] == "Short 2" and row['action'] == "2FGM":
        val = 1
    else:
        val = 0
    return val
datalist['Short2_Made'] = datalist.apply(Short2_Made, axis=1)

def Short2_Miss(row):
    if row['zone_details'] == "Short 2" and row['action'] == "2FGA":
        val = 1
    else:
        val = 0
    return val
datalist['Short2_Miss'] = datalist.apply(Short2_Miss, axis=1)

def Long2_Made(row):
    if row['zone_details'] == "Long 2" and row['action'] == "2FGM":
        val = 1
    else:
        val = 0
    return val
datalist['Long2_Made'] = datalist.apply(Long2_Made, axis=1)

def Long2_Miss(row):
    if row['zone_details'] == "Long 2" and row['action'] == "2FGA":
        val = 1
    else:
        val = 0
    return val
datalist['Long2_Miss'] = datalist.apply(Long2_Miss, axis=1)

def Pts3_Made(row):
    if row['zone_details'] == "3pts" and row['action'] == "3FGM":
        val = 1
    else:
        val = 0
    return val
datalist['Pts3_Made'] = datalist.apply(Pts3_Made, axis=1)

def Pts3_Miss(row):
    if row['zone_details'] == "3pts" and row['action'] == "3FGA":
        val = 1
    else:
        val = 0
    return val
datalist['Pts3_Miss'] = datalist.apply(Pts3_Miss, axis=1)

datalist = datalist.groupby('lineup_string').agg({'Rim_Made':'sum', 'Rim_Miss':'sum', 'Paint_Made':'sum', 'Paint_Miss':'sum', 'Short2_Made':'sum', 'Short2_Miss':'sum', 'Long2_Made':'sum', 'Long2_Miss':'sum', 'Pts3_Made':'sum', 'Pts3_Miss':'sum'})
datalist = datalist.reset_index()

datalist['Rim_Attempt'] = datalist['Rim_Made'] + datalist['Rim_Miss']
datalist['Paint_Attempt'] = datalist['Paint_Made'] + datalist['Paint_Miss']
datalist['Short2_Attempt'] = datalist['Short2_Made'] + datalist['Short2_Miss']
datalist['Long2_Attempt'] = datalist['Long2_Made'] + datalist['Long2_Miss']
datalist['Pts3_Attempt'] = datalist['Pts3_Made'] + datalist['Pts3_Miss']
datalist['Tot_Attempt'] = datalist['Rim_Attempt'] + datalist['Paint_Attempt'] + datalist['Short2_Attempt'] + datalist['Long2_Attempt'] + datalist['Pts3_Attempt']
        
datalist = (datalist[['lineup_string', 'Rim_Attempt', 'Rim_Made', 'Paint_Attempt', 'Paint_Made', 'Short2_Attempt', 'Short2_Made', 'Long2_Attempt', 'Long2_Made', 'Pts3_Attempt', 'Pts3_Made', 'Tot_Attempt']])

datalist['Rim_dist'] = (datalist['Rim_Attempt'] / datalist['Tot_Attempt'])*100
datalist['Rim_FG%'] = (datalist['Rim_Made'] / datalist['Rim_Attempt'])*100
datalist['Paint_dist'] = (datalist['Paint_Attempt'] / datalist['Tot_Attempt'])*100
datalist['Paint_FG%'] = (datalist['Paint_Made'] / datalist['Paint_Attempt'])*100
datalist['Short2_dist'] = (datalist['Short2_Attempt'] / datalist['Tot_Attempt'])*100
datalist['Short2_FG%'] = (datalist['Short2_Made'] / datalist['Short2_Attempt'])*100
datalist['Long2_dist'] = (datalist['Long2_Attempt'] / datalist['Tot_Attempt'])*100
datalist['Long2_FG%'] = (datalist['Long2_Made'] / datalist['Long2_Attempt'])*100
datalist['Pts3_dist'] = (datalist['Pts3_Attempt'] / datalist['Tot_Attempt'])*100
datalist['Pts3_FG%'] = (datalist['Pts3_Made'] / datalist['Pts3_Attempt'])*100

datalist = (datalist[['lineup_string', 'Rim_dist', 'Rim_FG%', 'Paint_dist', 'Paint_FG%', 'Short2_dist', 'Short2_FG%', 'Long2_dist', 'Long2_FG%', 'Pts3_dist', 'Pts3_FG%']])
   
datalist = tuple(datalist.itertuples(index=False, name=None))
        
print(datalist)