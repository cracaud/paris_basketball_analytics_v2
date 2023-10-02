from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import numpy as np
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}}
app.config['MYSQL_CHARSET'] = 'latin1'

mysql = MySQL(app)

@app.route('/', methods=["POST", "GET"])
def index():
    datalist=[]
    groupdata=[]
    cur = mysql.connection.cursor()

    cur.execute("SELECT DISTINCT player_id FROM play_by_play ORDER BY player_id")
    player_id=cur.fetchall()
    
    cur.execute("SELECT DISTINCT team_id FROM play_by_play ORDER BY team_id")
    team_id=cur.fetchall()
    
    cur.execute("SELECT DISTINCT season_id FROM play_by_play ORDER BY season_id")
    season_id=cur.fetchall()
    
    if request.method == 'POST':
        player_ids1 = request.form.get('search_filter_player1')
        player_ids2 = request.form.get('search_filter_player2')
        player_ids3 = request.form.get('search_filter_player3')
        player_ids4 = request.form.get('search_filter_player4')
        player_ids5 = request.form.get('search_filter_player5')
        player_ids6 = request.form.get('search_filter_player6')
        player_ids7 = request.form.get('search_filter_player7')
        player_ids8 = request.form.get('search_filter_player8')
        player_ids9 = request.form.get('search_filter_player9')
        player_ids10 = request.form.get('search_filter_player10')
        competitions = request.form.get('search_filter_competition')
        locations = request.form.get('search_filter_location')
        starts = request.form.get('start')
        ends = request.form.get('end')

        # Create a cursor
        cur = mysql.connection.cursor()

        # Only On Court filters
        if player_ids1 != "" and player_ids2 != "" and player_ids3 != "" and player_ids4 != "" and player_ids5 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids1, player_ids2, player_ids3, player_ids4, player_ids5])
        elif player_ids1 != "" and player_ids2 != "" and player_ids3 != "" and player_ids4 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids1, player_ids2, player_ids3, player_ids4])
        elif player_ids1 != "" and player_ids2 != "" and player_ids3 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids1, player_ids2, player_ids3])
        elif player_ids1 != "" and player_ids2 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids1, player_ids2])
        elif player_ids1 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids1])
        # Only Off Court filters
        elif player_ids6 != "" and player_ids7 != "" and player_ids8 != "" and player_ids9 != "" and player_ids10 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids6, player_ids7, player_ids8, player_ids9, player_ids10])
        elif player_ids6 != "" and player_ids7 != "" and player_ids8 != "" and player_ids9 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids6, player_ids7, player_ids8, player_ids9])
        elif player_ids6 != "" and player_ids7 != "" and player_ids8 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids6, player_ids7, player_ids8])
        elif player_ids6 != "" and player_ids7 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids6, player_ids7])
        elif player_ids6 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids6])
        #Only Location filters
        elif locations != "":
            cur.execute("SELECT * FROM play_by_play WHERE location IN (%s);", [locations])
        #Only Competitions filters
        elif competitions != "":
            cur.execute("SELECT * FROM play_by_play WHERE edition_id IN (%s);", [competitions])
        #Only Date Filters
        elif starts != "" and ends != "":
            cur.execute("SELECT * FROM play_by_play WHERE (date BETWEEN (%s) AND (%s));", [starts, ends])
            
        else:
            pass

        datalist = cur.fetchall()

        # Close the cursor
        cur.close()
        #Calculations for shooting data
        datalist = pd.DataFrame(datalist, columns=['id', 'season_id', 'edition_id', 'game_id', 'action_number', 'period',
                                                    'home_score', 'away_score', 'remaining_period_time', 'action', 'player_id',
                                                    'team_id', 'opponent_id', 'x', 'y', 'details', 'linked_action_number',
                                                    'h1', 'h2', 'h3', 'h4', 'h5', 'a1', 'a2', 'a3', 'a4', 'a5', 'date', 
                                                    'home_team','away_team', 'location'])
        
        

        def lineup(row):
            if row['home_team'] == "Paris":
                val = row[['h1','h2','h3','h4','h5']].values.tolist()
            elif row['away_team'] == "Paris":
                val = row[['a1','a2','a3','a4','a5']].values.tolist()
            else:
                val = "ERROR"
            return val
        datalist['lineup'] = datalist.apply(lineup, axis=1)
                    
        def ListToString(row):
            if len(row['lineup']) != 0:
                val = ' - '.join(row['lineup'])
            else:
                val = "ERROR"
            return val
        datalist['lineup_string'] = datalist.apply(ListToString, axis=1)

        def PBA3FGM(row):
            if row['action'] == "3FGM" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['3FGM_PBA'] = datalist.apply(PBA3FGM, axis=1)
        
        def PBA3FGA(row):
            if row['action'] == "3FGA" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['3FGA_PBA'] = datalist.apply(PBA3FGA, axis=1)
        
        def PBA2FGM(row):
            if row['action'] == "2FGM" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['2FGM_PBA'] = datalist.apply(PBA2FGM, axis=1)
        
        def PBA2FGA(row):
            if row['action'] == "2FGA" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['2FGA_PBA'] = datalist.apply(PBA2FGA, axis=1)
        
        def PBATOV(row):
            if row['action'] == "TOV" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['TOV_PBA'] = datalist.apply(PBATOV, axis=1)
        
        def PBAFTM(row):
            if row['action'] == "FTM" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['FTM_PBA'] = datalist.apply(PBAFTM, axis=1)
        
        def PBAFTA(row):
            if row['action'] == "FTA" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['FTA_PBA'] = datalist.apply(PBAFTA, axis=1)
        
        def PBAOREB(row):
            if row['action'] == "OREB" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['OREB_PBA'] = datalist.apply(PBAOREB, axis=1)
        
        def PBADREB(row):
            if row['action'] == "DREB" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['DREB_PBA'] = datalist.apply(PBADREB, axis=1)
        
        def PBASTL(row):
            if row['action'] == "STL" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['STL_PBA'] = datalist.apply(PBASTL, axis=1)
        
        def PBABLK(row):
            if row['action'] == "BLK" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['BLK_PBA'] = datalist.apply(PBABLK, axis=1)
        
        def PBAAST(row):
            if row['action'] == "AST" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['AST_PBA'] = datalist.apply(PBAAST, axis=1)
        
        def OPP3FGM(row):
            if row['action'] == "3FGM" and row['team_id'] != "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['3FGM_OPP'] = datalist.apply(OPP3FGM, axis=1)
        
        def OPP3FGA(row):
            if row['action'] == "3FGA" and row['team_id'] != "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['3FGA_OPP'] = datalist.apply(OPP3FGA, axis=1)
        
        def OPP2FGM(row):
            if row['action'] == "2FGM" and row['team_id'] != "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['2FGM_OPP'] = datalist.apply(OPP2FGM, axis=1)
        
        def OPP2FGA(row):
            if row['action'] == "2FGA" and row['team_id'] != "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['2FGA_OPP'] = datalist.apply(OPP2FGA, axis=1)
        
        def OPPTOV(row):
            if row['action'] == "TOV" and row['team_id'] != "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['TOV_OPP'] = datalist.apply(OPPTOV, axis=1)
        
        def OPPFTM(row):
            if row['action'] == "FTM" and row['team_id'] != "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['FTM_OPP'] = datalist.apply(OPPFTM, axis=1)
        
        def OPPFTA(row):
            if row['action'] == "FTA" and row['team_id'] != "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['FTA_OPP'] = datalist.apply(OPPFTA, axis=1)
        
        def OPPOREB(row):
            if row['action'] == "OREB" and row['team_id'] != "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['OREB_OPP'] = datalist.apply(OPPOREB, axis=1)
        
        def OPPDREB(row):
            if row['action'] == "DREB" and row['team_id'] != "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['DREB_OPP'] = datalist.apply(OPPDREB, axis=1)
        
        def OPPSTL(row):
            if row['action'] == "STL" and row['team_id'] != "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['STL_OPP'] = datalist.apply(OPPSTL, axis=1)
        
        def OPPBLK(row):
            if row['action'] == "BLK" and row['team_id'] != "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['BLK_OPP'] = datalist.apply(OPPBLK, axis=1)
        
        def OPPAST(row):
            if row['action'] == "AST" and row['team_id'] != "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['AST_OPP'] = datalist.apply(OPPAST, axis=1)
        
        datalist = datalist.groupby('lineup_string').agg({'3FGM_PBA':'sum', '3FGA_PBA':'sum', '2FGM_PBA':'sum', '2FGA_PBA':'sum', 
                                                          'FTM_PBA':'sum', 'FTA_PBA':'sum', 'OREB_PBA':'sum', 'DREB_PBA':'sum', 
                                                          'AST_PBA':'sum', 'TOV_PBA':'sum', 'STL_PBA':'sum', 'BLK_PBA':'sum',
                                                          '3FGM_OPP':'sum', '3FGA_OPP':'sum', '2FGM_OPP':'sum', '2FGA_OPP':'sum', 
                                                          'FTM_OPP':'sum', 'FTA_OPP':'sum', 'OREB_OPP':'sum', 'DREB_OPP':'sum', 
                                                          'AST_OPP':'sum', 'TOV_OPP':'sum', 'STL_OPP':'sum', 'BLK_OPP':'sum'})
        datalist = datalist.reset_index()
        
        groupdata = (datalist[['3FGM_PBA', '3FGA_PBA', '2FGM_PBA','2FGA_PBA', 'FTM_PBA', 'FTA_PBA', 'OREB_PBA', 
                               'DREB_PBA', 'AST_PBA', 'TOV_PBA', 'STL_PBA', 'BLK_PBA', '3FGM_OPP', '3FGA_OPP', '2FGM_OPP', '2FGA_OPP', 
                               'FTM_OPP', 'FTA_OPP', 'OREB_OPP', 'DREB_OPP', 'AST_OPP', 'TOV_OPP', 'STL_OPP', 'BLK_OPP']])
        groupdata.loc['total'] = groupdata.sum()
        groupdata = groupdata.loc[['total']] 
        
        teamdata = (groupdata[['3FGM_PBA', '3FGA_PBA', '2FGM_PBA','2FGA_PBA', 'FTM_PBA', 'FTA_PBA', 'OREB_PBA', 
                               'DREB_PBA', 'AST_PBA', 'TOV_PBA', 'STL_PBA', 'BLK_PBA', '3FGM_OPP', '3FGA_OPP', '2FGM_OPP', '2FGA_OPP', 
                               'FTM_OPP', 'FTA_OPP', 'OREB_OPP', 'DREB_OPP', 'AST_OPP', 'TOV_OPP', 'STL_OPP', 'BLK_OPP']])
        oppdata = (groupdata[['3FGM_PBA', '3FGA_PBA', '2FGM_PBA','2FGA_PBA', 'FTM_PBA', 'FTA_PBA', 'OREB_PBA', 
                               'DREB_PBA', 'AST_PBA', 'TOV_PBA', 'STL_PBA', 'BLK_PBA', '3FGM_OPP', '3FGA_OPP', '2FGM_OPP', '2FGA_OPP', 
                               'FTM_OPP', 'FTA_OPP', 'OREB_OPP', 'DREB_OPP', 'AST_OPP', 'TOV_OPP', 'STL_OPP', 'BLK_OPP']])
        
        teamdata = teamdata.rename(columns={"3FGM_PBA": "3FGM", "3FGA_PBA": "3FGA", "2FGM_PBA": "2FGM", "2FGA_PBA": "2FGA", "FTM_PBA": "FTM",
                                 "FTA_PBA": "FTA", "OREB_PBA": "OREB", "DREB_PBA": "DREB", "AST_PBA": "AST",
                                 "TOV_PBA": "TOV", "STL_PBA": "STL", "BLK_PBA": "BLK"})
        oppdata = oppdata.rename(columns={"3FGM_OPP": "3FGM", "3FGA_OPP": "3FGA", "2FGM_OPP": "2FGM", "2FGA_OPP": "2FGA", "FTM_OPP": "FTM",
                                 "FTA_OPP": "FTA", "OREB_OPP": "OREB", "DREB_OPP": "DREB", "AST_OPP": "AST", "TOV_OPP": "TOV", 
                                 "STL_OPP": "STL", "BLK_OPP": "BLK", "3FGM_PBA": "3FGM_OPP", "3FGA_PBA": "3FGA_OPP", 
                                 "2FGM_PBA": "2FGM_OPP", "2FGA_PBA": "2FGA_OPP", "FTM_PBA": "FTM_OPP", "FTA_PBA": "FTA_OPP", 
                                 "OREB_PBA": "OREB_OPP", "DREB_PBA": "DREB_OPP", "AST_PBA": "AST_OPP", "TOV_PBA": "TOV_OPP", 
                                 "STL_PBA": "STL_OPP", "BLK_PBA": "BLK_OPP"})
        
        groupdata = pd.concat([teamdata, oppdata])
        teams = ['Team', 'Opponents']
        groupdata['lineup_string'] = teams
        
        datalist['poss_PBA'] = (datalist['3FGM_PBA'] + datalist['3FGA_PBA'] + datalist['2FGM_PBA'] + datalist['2FGA_PBA']) + datalist['TOV_PBA'] + 0.44*(datalist['FTM_PBA'] + datalist['FTA_PBA']) - datalist['OREB_PBA']
        datalist['poss_OPP'] = (datalist['3FGM_OPP'] + datalist['3FGA_OPP'] + datalist['2FGM_OPP'] + datalist['2FGA_OPP']) + datalist['TOV_OPP'] + 0.44*(datalist['FTM_OPP'] + datalist['FTA_OPP']) - datalist['OREB_OPP']
        datalist['ORTG_PBA'] = ((datalist['3FGM_PBA']*3 + datalist['2FGM_PBA']*2 + datalist['FTM_PBA']) / datalist['poss_PBA'])*100
        datalist['DRTG_PBA'] = ((datalist['3FGM_OPP']*3 + datalist['2FGM_OPP']*2 + datalist['FTM_OPP']) / datalist['poss_OPP'])*100
        datalist['NRTG_PBA'] = datalist['ORTG_PBA'] - datalist['DRTG_PBA']
        datalist['eFG%_PBA'] = ((datalist['2FGM_PBA'] + datalist['3FGM_PBA']*1.5) / (datalist['2FGA_PBA'] + datalist['3FGA_PBA'] + datalist['2FGM_PBA'] + datalist['3FGM_PBA'])) * 100
        datalist['TOV%_PBA'] = (datalist['TOV_PBA'] / datalist['poss_PBA'])*100
        datalist['OREB%_PBA'] = (datalist['OREB_PBA'] / (datalist['OREB_PBA'] + datalist['DREB_OPP']))*100
        datalist['DREB%_PBA'] = (datalist['DREB_PBA'] / (datalist['DREB_PBA'] + datalist['OREB_OPP']))*100
        datalist['FTAr_PBA'] = ((datalist['FTM_PBA'] + datalist['FTA_PBA']) / (datalist['2FGA_PBA'] + datalist['3FGA_PBA'] + datalist['2FGM_PBA'] + datalist['3FGM_PBA']))*100
        datalist['eFG%_OPP'] = ((datalist['2FGM_OPP'] + datalist['3FGM_OPP']*1.5) / (datalist['2FGA_OPP'] + datalist['3FGA_OPP'] + datalist['2FGM_OPP'] + datalist['3FGM_OPP'])) * 100
        datalist['TOV%_OPP'] = (datalist['TOV_OPP'] / datalist['poss_OPP'])*100
        datalist['OREB%_OPP'] = (datalist['OREB_OPP'] / (datalist['OREB_OPP'] + datalist['DREB_PBA']))*100
        datalist['DREB%_OPP'] = (datalist['DREB_OPP'] / (datalist['DREB_OPP'] + datalist['OREB_PBA']))*100
        datalist['FTAr_OPP'] = ((datalist['FTM_OPP'] + datalist['FTA_OPP']) / (datalist['2FGA_OPP'] + datalist['3FGA_OPP'] + datalist['2FGM_OPP'] + datalist['3FGM_OPP']))*100
        datalist['STL%_PBA'] = (datalist['STL_PBA'] / datalist['poss_OPP'])*100
        datalist['BLK%_PBA'] = (datalist['BLK_PBA'] / (datalist['2FGA_OPP'] + datalist['3FGA_OPP'] + datalist['2FGM_OPP'] + datalist['3FGM_OPP']))*100
        datalist['AST%_PBA'] = (datalist['AST_PBA'] / (datalist['2FGM_PBA'] + datalist['3FGM_PBA']))*100
        
        groupdata['poss'] = (groupdata['3FGM'] + groupdata['3FGA'] + groupdata['2FGM'] + groupdata['2FGA']) + groupdata['TOV'] + 0.44*(groupdata['FTM'] + groupdata['FTA']) - groupdata['OREB']
        groupdata['RTG'] = ((groupdata['3FGM']*3 + groupdata['2FGM']*2 + groupdata['FTM']) / groupdata['poss'])*100
        groupdata['eFG%'] = ((groupdata['2FGM'] + groupdata['3FGM']*1.5) / (groupdata['2FGA'] + groupdata['3FGA'] + groupdata['2FGM'] + groupdata['3FGM'])) * 100
        groupdata['TS%'] = ((groupdata['3FGM'] + groupdata['2FGM'] + groupdata['FTM']) / (2*((groupdata['2FGA'] + groupdata['3FGA'] + groupdata['2FGM'] + groupdata['3FGM']) + 0.44*(groupdata['FTM'] + groupdata['FTA'])))) *100
        groupdata['TOV%'] = (groupdata['TOV'] / groupdata['poss'])*100
        groupdata['OREB%'] = (groupdata['OREB'] / (groupdata['OREB'] + groupdata['DREB_OPP']))*100
        groupdata['DREB%'] = (groupdata['DREB'] / (groupdata['DREB'] + groupdata['OREB_OPP']))*100
        groupdata['FTAr'] = ((groupdata['FTM'] + groupdata['FTA']) / (groupdata['2FGA'] + groupdata['3FGA'] + groupdata['2FGM'] + groupdata['3FGM']))*100
        groupdata['STL%'] = (groupdata['STL'] / groupdata['poss'])*100
        groupdata['BLK%'] = (groupdata['BLK'] / (groupdata['2FGA'] + groupdata['3FGA'] + groupdata['2FGM'] + groupdata['3FGM']))*100
        groupdata['AST%'] = (groupdata['AST'] / (groupdata['2FGM'] + groupdata['3FGM']))*100
        
        datalist = (datalist[['lineup_string', 'poss_PBA', 'NRTG_PBA', 'ORTG_PBA', 'DRTG_PBA', 'eFG%_PBA', 'TOV%_PBA', 'OREB%_PBA', 'DREB%_PBA', 
                              'FTAr_PBA', 'eFG%_OPP', 'TOV%_OPP', 'OREB%_OPP', 'DREB%_OPP', 'FTAr_OPP', 'STL%_PBA', 'BLK%_PBA', 'AST%_PBA']])
        groupdata = (groupdata[['lineup_string', 'poss', 'RTG', 'eFG%', 'TS%', 'TOV%', 'OREB%', 'DREB%', 'FTAr', 'STL%', 'BLK%', 'AST%']])
        
        datalist = datalist.sort_values(by=['poss_PBA'], ascending=False)
        
        datalist = datalist.round(2)
        groupdata = groupdata.round(2)
        
        groupdata['eFG%'] = groupdata['eFG%'].fillna('-').astype(str) + ' %'
            
        datalist = tuple(datalist.itertuples(index=False, name=None))
        groupdata = tuple(groupdata.itertuples(index=False, name=None))
        
        return render_template('index.html', datalist=datalist,player_id=player_id, team_id=team_id, season_id=season_id, groupdata=groupdata)

    return render_template('index.html', datalist=datalist, player_id=player_id, team_id=team_id, season_id=season_id, groupdata=groupdata)

@app.route('/shooting', methods=["POST", "GET"])
def shooting():
    datalist=[]
    cur = mysql.connection.cursor()

    sql=("SELECT DISTINCT player_id FROM play_by_play ORDER BY player_id")
    cur.execute(sql)
    player_id=cur.fetchall()
    if request.method == 'POST':
        player_ids1 = request.form.get('search_filter_player1')
        player_ids2 = request.form.get('search_filter_player2')
        player_ids3 = request.form.get('search_filter_player3')
        player_ids4 = request.form.get('search_filter_player4')
        player_ids5 = request.form.get('search_filter_player5')
        player_ids6 = request.form.get('search_filter_player6')
        player_ids7 = request.form.get('search_filter_player7')
        player_ids8 = request.form.get('search_filter_player8')
        player_ids9 = request.form.get('search_filter_player9')
        player_ids10 = request.form.get('search_filter_player10')
        competitions = request.form.get('search_filter_competition')
        locations = request.form.get('search_filter_location')
        starts = request.form.get('start')
        ends = request.form.get('end')

        # Create a cursor
        cur = mysql.connection.cursor()

        # Only On Court filters
        if player_ids1 != "" and player_ids2 != "" and player_ids3 != "" and player_ids4 != "" and player_ids5 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids1, player_ids2, player_ids3, player_ids4, player_ids5])
        elif player_ids1 != "" and player_ids2 != "" and player_ids3 != "" and player_ids4 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids1, player_ids2, player_ids3, player_ids4])
        elif player_ids1 != "" and player_ids2 != "" and player_ids3 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids1, player_ids2, player_ids3])
        elif player_ids1 != "" and player_ids2 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids1, player_ids2])
        elif player_ids1 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids1])
        # Only Off Court filters
        elif player_ids6 != "" and player_ids7 != "" and player_ids8 != "" and player_ids9 != "" and player_ids10 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids6, player_ids7, player_ids8, player_ids9, player_ids10])
        elif player_ids6 != "" and player_ids7 != "" and player_ids8 != "" and player_ids9 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids6, player_ids7, player_ids8, player_ids9])
        elif player_ids6 != "" and player_ids7 != "" and player_ids8 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids6, player_ids7, player_ids8])
        elif player_ids6 != "" and player_ids7 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5) AND %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids6, player_ids7])
        elif player_ids6 != "":
            cur.execute("SELECT * FROM play_by_play WHERE %s NOT IN (h1, h2, h3, h4, h5, a1, a2, a3, a4, a5);", [player_ids6])
        #Only Location filters
        elif locations != "":
            cur.execute("SELECT * FROM play_by_play WHERE location IN (%s);", [locations])
        #Only Competitions filters
        elif competitions != "":
            cur.execute("SELECT * FROM play_by_play WHERE edition_id IN (%s);", [competitions])
        #Only Date Filters
        elif starts != "" and ends != "":
            cur.execute("SELECT * FROM play_by_play WHERE (date BETWEEN (%s) AND (%s));", [starts, ends])
            
        else:
            pass

        datalist = cur.fetchall()

        # Close the cursor
        cur.close()
        #Calculations for shooting data
        datalist = pd.DataFrame(datalist, columns=['id', 'season_id', 'edition_id', 'game_id', 'action_number', 'period',
                                                    'home_score', 'away_score', 'remaining_period_time', 'action', 'player_id',
                                                    'team_id', 'opponent_id', 'x', 'y', 'details', 'linked_action_number',
                                                    'h1', 'h2', 'h3', 'h4', 'h5', 'a1', 'a2', 'a3', 'a4', 'a5', 'date', 'home_team',
                                                    'away_team', 'location'])

        def lineup(row):
            if row['home_team'] == "Paris":
                val = row[['h1','h2','h3','h4','h5']].values.tolist()
            elif row['away_team'] == "Paris":
                val = row[['a1','a2','a3','a4','a5']].values.tolist()
            else:
                val = "ERROR"
            return val
        datalist['lineup'] = datalist.apply(lineup, axis=1)

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

        def zone_details(row):
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
        datalist['zone_details'] = datalist.apply(zone_details, axis=1)
                    
        def ListToString(row):
            if len(row['lineup']) != 0:
                val = ' - '.join(row['lineup'])
            else:
                val = "ERROR"
            return val
        datalist['lineup_string'] = datalist.apply(ListToString, axis=1)

        def Rim_Made(row):
            if row['zone_details'] == "Rim" and row['action'] == "2FGM" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['Rim_Made'] = datalist.apply(Rim_Made, axis=1)
            
        def Rim_Miss(row):
            if row['zone_details'] == "Rim" and row['action'] == "2FGA" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['Rim_Miss'] = datalist.apply(Rim_Miss, axis=1)

        def Paint_Made(row):
            if row['zone_details'] == "Paint" and row['action'] == "2FGM" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['Paint_Made'] = datalist.apply(Paint_Made, axis=1)

        def Paint_Miss(row):
            if row['zone_details'] == "Paint" and row['action'] == "2FGA" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['Paint_Miss'] = datalist.apply(Paint_Miss, axis=1)

        def Short2_Made(row):
            if row['zone_details'] == "Short 2" and row['action'] == "2FGM" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['Short2_Made'] = datalist.apply(Short2_Made, axis=1)

        def Short2_Miss(row):
            if row['zone_details'] == "Short 2" and row['action'] == "2FGA" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['Short2_Miss'] = datalist.apply(Short2_Miss, axis=1)

        def Long2_Made(row):
            if row['zone_details'] == "Long 2" and row['action'] == "2FGM" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['Long2_Made'] = datalist.apply(Long2_Made, axis=1)

        def Long2_Miss(row):
            if row['zone_details'] == "Long 2" and row['action'] == "2FGA" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['Long2_Miss'] = datalist.apply(Long2_Miss, axis=1)

        def Pts3_Made(row):
            if row['zone_details'] == "3pts" and row['action'] == "3FGM" and row['team_id'] == "Paris":
                val = 1
            else:
                val = 0
            return val
        datalist['Pts3_Made'] = datalist.apply(Pts3_Made, axis=1)

        def Pts3_Miss(row):
            if row['zone_details'] == "3pts" and row['action'] == "3FGA" and row['team_id'] == "Paris":
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
        datalist['3pts_dist'] = (datalist['Pts3_Attempt'] / datalist['Tot_Attempt'])*100
        datalist['3pts_FG%'] = (datalist['Pts3_Made'] / datalist['Pts3_Attempt'])*100

        datalist = (datalist[['lineup_string', 'Rim_dist', 'Rim_FG%', 'Paint_dist', 'Paint_FG%', 'Short2_dist', 'Short2_FG%', 'Long2_dist', 'Long2_FG%', '3pts_dist', '3pts_FG%']])
        datalist = datalist.round(2)
        datalist['Rim_dist'] = datalist['Rim_dist'].fillna('-').astype(str) + ' %'
        datalist['Paint_dist'] = datalist['Paint_dist'].fillna('-').astype(str) + ' %'
        datalist['Short2_dist'] = datalist['Short2_dist'].fillna('-').astype(str) + ' %'
        datalist['Long2_dist'] = datalist['Long2_dist'].fillna('-').astype(str) + ' %'
        datalist['3pts_dist'] = datalist['3pts_dist'].fillna('-').astype(str) + ' %'
        datalist['Rim_FG%'] = datalist['Rim_FG%'].fillna('-').astype(str) + ' %'
        datalist['Paint_FG%'] = datalist['Paint_FG%'].fillna('-').astype(str) + ' %'
        datalist['Short2_FG%'] = datalist['Short2_FG%'].fillna('-').astype(str) + ' %'
        datalist['Long2_FG%'] = datalist['Long2_FG%'].fillna('-').astype(str) + ' %'
        datalist['3pts_FG%'] = datalist['3pts_FG%'].fillna('-').astype(str) + ' %'
            
        datalist = tuple(datalist.itertuples(index=False, name=None))
        
        return render_template('shooting.html', datalist=datalist,player_id=player_id)

    return render_template('shooting.html', datalist=datalist, player_id=player_id)

if __name__ == "__main__":
    app.run(debug=True)
    
# A FAIRE 
# REVOIR LE FILTRE OFF COURT PARCE QUE L'APPLICATION PREND EN COMPTE TOUTES LES POSSESSIONS MÊME QUAND PARIS NE JOUE PAS
# ----> Filtres : 
#           On Court OK, 
#           Off Court OK, 
#           Competitions OK, 
#           Location OK, 
#           Game Result TO DO, 
#           Dates OK
# ----> Faire toutes les combinaisons de filtres possibles
# ----> Faire toute la partie CSS pour donner du style
# ----> Faire quelque chose pour conserver les filtres choisis après Submit
# ----> Mise en couleurs

# MODIFICATIONS A FAIRE SUR LA DATA DEPUIS SDENG : 
# - Modifier Edition_id : 22-23 PROA --> PROA (pour le filtre competition)
# ...

# - Séparer Game_id pour avoir Date, Home team, Away team
#       ----> ALTER TABLE play_by_play ADD column_name datatype;
#       ----> UPDATE play_by_play SET columnB = columnA; 
#   Pour Date :
#       Créer une copie de la colonne "game_id" et la nommer "date"
#       ----> UPDATE play_by_play SET date = SUBSTRING(date, 1, 10);
#   Pour Home_team :
#       Créer une copie de la colonne "game_id" et la nommer "home_team"
#       ----> UPDATE play_by_play SET home_team = SUBSTRING(home_team, 12, 100); 
#       ----> UPDATE play_by_play SET home_team = SUBSTRING_INDEX(home_team, '-', 1); 
#       ----> UPDATE play_by_play SET home_team = REPLACE(home_team, 'Bourg', 'Bourg-en-Bresse'); 
#       ----> UPDATE play_by_play SET home_team = REPLACE(home_team, 'Lyon', 'Lyon-Villeurbanne'); 
#       ----> UPDATE play_by_play SET home_team = REPLACE(home_team, 'Gravelines', 'Gravelines-Dunkerque'); 
#       ----> UPDATE play_by_play SET home_team = REPLACE(home_team, 'Boulogne', 'Boulogne-Levallois'); 
#       ----> UPDATE play_by_play SET home_team = REPLACE(home_team, 'Saint', 'Saint-Quentin'); 
#       ----> UPDATE play_by_play SET home_team = REPLACE(home_team, 'nullcy', 'Nancy'); 
#       ----> UPDATE play_by_play SET home_team = REPLACE(home_team, 'nullterre', 'Nanterre'); 
#       ----> UPDATE play_by_play SET home_team = REPLACE(home_team, 'Chalon/Sa��ne', 'Chalon/Saone'); 
#
#   Pour Away_Team :
#       ----> UPDATE play_by_play SET away_team = SUBSTRING(away_team, 12, 100);
#       ----> UPDATE play_by_play SET away_team = SUBSTRING_INDEX(away_team, '-', -1);
#       ----> UPDATE play_by_play SET away_team = REPLACE(away_team, 'Bresse', 'Bourg-en-Bresse');
#       ----> UPDATE play_by_play SET away_team = REPLACE(away_team, 'Villeurbanne', 'Lyon-Villeurbanne');
#       ----> UPDATE play_by_play SET away_team = REPLACE(away_team, 'Dunkerque', 'Gravelines-Dunkerque');
#       ----> UPDATE play_by_play SET away_team = REPLACE(away_team, 'Levallois', 'Boulogne-Levallois');
#       ----> UPDATE play_by_play SET away_team = REPLACE(away_team, 'Quentin', 'Saint-Quentin');
#       ----> UPDATE play_by_play SET away_team = REPLACE(away_team, 'nullcy', 'Nancy');
#       ----> UPDATE play_by_play SET away_team = REPLACE(away_team, 'nullterre', 'Nanterre');
#       ----> UPDATE play_by_play SET away_team = REPLACE(away_team, 'Chalon/Sa��ne', 'Chalon/Saone');
#
#   Pour Location :
#       Créer une nouvelle colonne "location"
#       ----> UPDATE play_by_play SET location = 'Home' WHERE home_team = "Paris";
#       ----> UPDATE play_by_play SET location = 'Away' WHERE away_team = "Paris";
#       ----> UPDATE play_by_play SET location = 'Neutral' WHERE game_id = "2022-10-16:Paris-Monaco";
#
#   Pour player_id :
#       ----> UPDATE play_by_play SET player_id = REPLACE(player_id, 'nulldo De Colo', 'Nando De Colo');
#
# ADD DATA TO THE DATABASE : INSERT INTO play_by_play VALUES
# UPDATE play_by_play SET team_id = REPLACE(team_id, 'nullterre', 'Nanterre');