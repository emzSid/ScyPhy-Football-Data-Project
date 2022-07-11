## Football Tournament Project

### Table of Contents
1. Motivation
2. Datasource
3. Structure
4. Functions Description
5. How to set up
6. Specification of valid arguments


### Motivation:
Since the uefa womens euro (football tournament) starts in July 2022, I was motivated to work with corresponding Fifa football player data. 
Regarding the functions, I tried to think about things a fan or coach would like to know before the tournament starts. In the end I came up with the functions specified below.

### Datasource 
As data source, I use the csv file called female_players_22.csv from the Fifa 2022 dataset from [Kaggle](https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset?select=female_players_22.csv). <br>
To run the code it is neccessery to download the csv file from Kaggle.

### Structure:
All functions are in the single py file 'SP_project' and they are called in the ipynp file 'visualization'.<br>
The visualization (e.g. plot or images) of the functions output is done in the function itself. <br>

### Function Description: 
- **clean_data_to_purpose(data):** <br>
     Deletes unneccesary columns and only keeps the european players <br>

     Args: <br>
      data: dataframe female_players_22.csv from Kaggle<br>
     Results: <br>
      changed dataframe as specified above<br>
      
- **add_rankingtype(data):** <br>
     Defines categories for moderate, good and world class players and assigns each player one of these categories in a new colum<br>

     Args: <br>
      data: cleaned dataframe (female_players_22.csv from Kaggle)<br>
     Results: <br>
      dataframe with additional column <br>
      
- **player_info(data, player_name):** <br>
     Extracts some facts of a player, and shows them in a table together with the face of the player<br>

     Args: <br>
      data: cleaned dataframe (female_players_22.csv from Kaggle)<br>
      player_name: entry of the column 'short_name' from the dataframe (String)<br>
     Results: <br>
        Subplot with the players face on the left and a table with player facts on the right<br>
        
 - **youngsters_to_watch_out(dataframe):** <br>
      Extracts young players with a high potential rate and displays their faces and name side by side<br>

      Args: <br>
        data: cleaned dataframe (female_players_22.csv from Kaggle)<br>
      Results: <br>
        Subplot with four images per row (two rows) displaying the players face <br>

 - **extract_one_team(data ,team):** <br>
      Extracts the squad for one team<br>

      Args: <br>
        data: cleaned dataframe (female_players_22.csv from Kaggle)<br>
        team: entry of the column 'nationality_name' (String)<br>
      Results: <br>
        Dataframe which is reduced to only players of one nation<br>

- **get_top5(data, team, criteria):** <br>
      Sorts the team by a criteria and displays the faces of the best 5 players of it<br>
      
      Args: <br>
        data: cleaned dataframe (female_players_22.csv from Kaggle)<br>
        team: entry of the column 'nationality_name' (String)<br>
        criteria: any column name of the datframe with integers (String)<br>
      Results: <br>
        Subplot with five images side by side displaying the players face <br>
        
- **get_best_formation(data, specification):**<br>
     Maximizes the sum of the players overall rating for each possible formation and keeps the corresponding selected players as lineup <br>

     Args: <br>
       data: cleaned dataframe (female_players_22.csv from Kaggle)<br>
       specification: entry of the column 'nationality_name' (String)<br>
     Results: <br>
       A table with the 11 selected players and a print statement which reveals the best formation for this team and its overall rating then<br>

 - **physic_overall_corr(data):** <br>
      Plots the correlation of overall with passing, ball control and physic rating compared for defenders and offensive players<br>

      Args: <br>
        data: cleaned dataframe (female_players_22.csv from Kaggle)<br>
      Results: <br>
        Three seaborn pairplots side by side<br>

- **player_type_dis(data, specification):** <br>
      Displays a stacked barplot of the counts of each ranking type in the specified national teams<br>
      
      Args: <br>
        data: cleaned dataframe (female_players_22.csv from Kaggle)<br>
        specification: entry of the column 'nationality_name'<br>
      Results: <br>
        Stacked barplot

### How to set up:
To set up, you need to run the following:<br>

import pandas as pd <br>
from SP_project import * <br>

players = pd.read_csv('female_players_22.csv') <br>
add_rankingtype(players) <br>
clean_data_to_purpose(players) <br>

afterwards, all functions should be callable.
 
### Specification of valid arguments for specific functions: 
- player_type_dis(dataframe, specification): <br>
        - To get the stacked barplot for all european countries write 'none' (string) as the second argument<br>
        - For only three nations write an array with three entries, namely three nations from the nationality_name column as second argument<br>
- get_top5(nationalityName, criteria): <br>
        - The first argument is either an entry of the column "nationality_name or if you insert 'all' the whole datatframe is taken
