## Football Tournament Project

### Table of Contents
1. Motivation
2. Function Description
3. Datasource
3. Structure
4. How to set up
5. How to use the functions


### Motivation:
Since the uefa womens euro (football tournament) starts in July 2022, 
I was motivated to work with corresponding Fifa football player data. 
Regarding the functions, I tried to think about things a fan or coach would like to know before the tournament starts. In the end I came up with the functions specified below.

### Datasource 
As data source, I use the csv file called female_players_22.csv from the fifa 2022 dataset from Kaggle (https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset?select=female_players_22.csv).
To run the code it is neccessery to download the csv file from Kaggle

### Function Description: 
1. player_type_dis(dataframe, specification): restructures the dataframe and
 makes a stacked barplot displaying how many world class/good or moderate players are in the specified national teams

2. get_top5(nationalityName, criteria): sorts ths specified nationalteam by the criteria 
so that in the first row there is the player with the best rating of this criteria. 
Then the function displays the faces of the best 5 players (rows) with their corresponding names

3. youngsters_to_watch_out(dataframe): extracts young players with a high potential rating and then side by side, displays their faces with the corresponding name 

4. physic_overall_corr(dataframe): plots the correlation of the overall rating with the passing, ball control and physic rating compared for defenders and offensive players

5. get_best_formation(dataframe, team, criteria): returns the best football formation  
and lineup for a specified team plus its resulting overall rating. This is done by maximizing the players rating for each position in a formation

6. player_info(dataframe, player_name): returns a table with player facts and her face

### Structure:
All functions are in the single py file 'SP_project' and they are called in the ipynp file 'visualization'.
The visualization (e.g. plot or images) of the functions output is done in the function itself. 

### How to set up:
To set up, you need to run the following:

import pandas as pd <br>
from SP_project import * <br>

players = pd.read_csv('female_players_22.csv') <br>
add_rankingtype(players) <br>
clean_data_to_purpose(players) <br>

afterwards, all functions should be callable.
 
### How to use the functions: 
Specification of valid arguments: 
- player_type_dis(dataframe, specification): 
        - The first argument is the name of the whole dataframe
        - To get the stacked barplot for all european countries write 'none' (string) as the second argument
        - For only three nations write an array with three entries,
          namely three nations from the nationality_name column as second argument
- get_top5(nationalityName, criteria): 
        - The first argument is either an entry of the column "nationality_name"
          or if you insert 'all' the whole datatframe is taken
        - The second argument can be the name of any column which contains exclusively integers
- youngsters_to_watch_out(dataframe): the argument is the name of the whole dataframe
- physic_overall_corr(dataframe): the argument is the name of the whole dataframe
- get_best_formation(dataframe, team, criteria): 
        - The first argument is the name of the whole dataframe
        - To get the best lineup of the whole dataframe write 'all' (string) as the second argument
        - For the best lineup of a specific team write the corresponding nationality_name as string as second argument
        - the third argument can be the name of any column with integers
- player_info(dataframe, player_name): 
        - The first argument is the name of the whole dataframe 
        - The second argument is an entry of the column 'short_name'
