import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import requests
import matplotlib.patches as mpatches
from IPython.display import display
from matplotlib.font_manager import FontProperties


'''
cleans and structures the data delete unneccesary columns
'''
def clean_data_to_purpose(data):
    #data.set_index("short_name", inplace = True)
    data.drop(['player_url','league_name', 'club_name', 'nation_team_id', 'club_team_id','nationality_id','club_contract_valid_until', 'club_loaned_from','club_joined','league_level','club_position', 'wage_eur', 'value_eur','sofifa_id', 'club_jersey_number','attacking_volleys', 'club_logo_url', 'nation_logo_url', 'nation_flag_url', 'club_flag_url'], axis = 1, inplace= True)

    #make new column wich indicates if the player is european or not 
    data['Is_european'] = data['nationality_name'].map({'England': True, 'France': True,'Netherlands': True, 'Australia': False, 'United States': False,'Germany': True, 'Norway': True, 'Canada': False, 'Spain': True, 'Scotland': True, 'Sweden': True, 'New Zealand': False, 'Mexico': False, 'Brazil': False, 'China PR': False, 'Belgium': True, 'Portugal': True })

    #delete all players which are not european
    data.drop(data.index[data['Is_european'] == False], inplace=True)
    #delete bool column for is the player european or not 
    data.drop('Is_european', inplace=True, axis=1)


'''
defines categories for moderate, good and world class players and assigns each player one of these categories in a new column
'''
def add_rankingtype(data):
    
    # define categories world class/good/moderate player and make new column
    conditions = [
        (data['overall'] > 83),
        (data['overall'] > 75) & (data['overall'] < 84), 
        (data['overall'] < 75)
    ]
    #values which will be assigned to the conditions
    values = ['world class player', 'good player', 'moderate player']
    #create new column which will indicate the ranking type of the player (moderate, good or world class player)
    data['ranking type'] = np.select(conditions, values)


'''
returns a table with player facts and her face
'''
def player_info(data, player_name):
    #extract the row of the specified player
    df = data.loc[data['short_name'] == player_name]
    #select the columns of interest
    df = df[['long_name', 'dob', 'player_positions', 'overall','nationality_name', 'height_cm', 'preferred_foot', 'player_traits']]
    # ignore the columns which contain Nans
    df = df.dropna(axis=1)
    #reshape df
    df = df.set_index('long_name')
    df = df.T

    #get the picture url 
    url = data.loc[data['short_name'] == player_name].player_face_url
    url = url.to_string(index=False)

    #make subplots which display the image of the players faces and a table with facts    
    f, (ax1, ax2) = plt.subplots(1, 2) 

    #set the plot size
    plt.gcf().set_size_inches(10, 4)

    image = Image.open(requests.get(url, stream=True).raw)

    #show the image at the specific axis
    ax1.imshow(image)

    #show the table
    table = ax2.table(cellText=df.values, colLabels=df.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2)
    
    # make the name bold
    for (row, col), cell in table.get_celld().items():
        if (row == 0):
            cell.set_text_props(fontproperties=FontProperties(weight='bold'))

    # turn the axes off
    ax1.axis("off")
    ax2.axis("off")


'''
extracts young players with a high potential rate and displays their faces with name next to each other
'''
def youngsters_to_watch_out(data):
    #extract young players with a high potential rating
    youngsters_table = data[(data['age'] < 22) & (data['potential'] > 84)]
    #put names in a list
    youngsters_names = youngsters_table['short_name'].tolist()
    #get the picture urls for each name and put it in a list
    urls = []
    for n in youngsters_names: 
        urls.append(data.loc[data['short_name'] == n].player_face_url.to_string(index=False))
    
    #make subplots which display the images of the players faces
    f, axarr = plt.subplots(2,4)
    plt.gcf().set_size_inches(11, 5)
    image1 = Image.open(requests.get(urls.pop(), stream=True).raw)
    image2 = Image.open(requests.get(urls.pop(), stream=True).raw)
    image3 = Image.open(requests.get(urls.pop(), stream=True).raw)
    image4 = Image.open(requests.get(urls.pop(), stream=True).raw)
    image5 = Image.open(requests.get(urls.pop(), stream=True).raw)
    image6 = Image.open(requests.get(urls.pop(), stream=True).raw)
    image7 = Image.open(requests.get(urls.pop(), stream=True).raw)
    image8 = Image.open(requests.get(urls.pop(), stream=True).raw)
    #show the images at the specific axis
    axarr[0,0].imshow(image1)
    axarr[0,1].imshow(image2)
    axarr[0,2].imshow(image3)
    axarr[0,3].imshow(image4)
    axarr[1,0].imshow(image5)
    axarr[1,1].imshow(image6)
    axarr[1,2].imshow(image7)
    axarr[1,3].imshow(image8)

    #turn the axes off
    axarr[0,0].axis("off")
    axarr[0,1].axis("off")
    axarr[0,2].axis("off")
    axarr[0,3].axis("off")
    axarr[1,0].axis("off")
    axarr[1,1].axis("off")
    axarr[1,2].axis("off")
    axarr[1,3].axis("off")

    #write the players name as title
    axarr[0,0].set_title(youngsters_names.pop(), fontsize=14)
    axarr[0,1].set_title(youngsters_names.pop(), fontsize=14)
    axarr[0,2].set_title(youngsters_names.pop(), fontsize=14)
    axarr[0,3].set_title(youngsters_names.pop(), fontsize=14)
    axarr[1,0].set_title(youngsters_names.pop(), fontsize=14)
    axarr[1,1].set_title(youngsters_names.pop(), fontsize=14)
    axarr[1,2].set_title(youngsters_names.pop(), fontsize=14)
    axarr[1,3].set_title(youngsters_names.pop(), fontsize=14)

    f.suptitle('Young Players With Highest Potential', fontweight ='bold', size=17)
    f.tight_layout()



'''
extracts the squad for one team
'''
def extract_one_team(data ,team):
    single_team = data[data.nationality_name.str.contains(team ,case=False)]
    return single_team


'''
sorts the team by a criteria and displays the faces of the best 5 players of it
'''
def get_top5(data, team, criteria): 
    #if no specific team is stated continue with all layers, else continue with the list of players of this specific team 
    if(team !=  'all'): 
        team = extract_one_team(data,team)
    else: team = data
    #extract the players with the best 5 ratings of this criteria
    top_table =team.nlargest(5, criteria)
    #but the names in a list
    top_names = top_table['short_name'].tolist()

    #get the picture urls for each name and put it in a list
    urls = []
    for n in top_names: 
        urls.append(data.loc[data['short_name'] == n].player_face_url.to_string(index=False))

    #make subplots which display the images of the players faces   
    f, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5) 

    #set the plot size
    plt.gcf().set_size_inches(13, 6)

    image1 = Image.open(requests.get(urls.pop(), stream=True).raw)
    image2 = Image.open(requests.get(urls.pop(), stream=True).raw)
    image3 = Image.open(requests.get(urls.pop(), stream=True).raw)
    image4 = Image.open(requests.get(urls.pop(), stream=True).raw)
    image5 = Image.open(requests.get(urls.pop(), stream=True).raw)
    #show the images at the specific axis
    ax1.imshow(image1)
    ax2.imshow(image2)
    ax3.imshow(image3)
    ax4.imshow(image4)
    ax5.imshow(image5)
    # turn the axes off
    ax1.axis("off")
    ax2.axis("off")
    ax3.axis("off")
    ax4.axis("off")
    ax5.axis("off")
    #write the name of the player as title
    ax1.set_title(top_names.pop(), fontsize=14)
    ax2.set_title(top_names.pop(), fontsize=14)
    ax3.set_title(top_names.pop(), fontsize=14)
    ax4.set_title(top_names.pop(), fontsize=14)
    ax5.set_title(top_names.pop(), fontsize=14)



'''
returns best formation and lineup for this team plus its overall rating
'''
def get_best_formation(data, specification):
    d = data.copy()
    formations_dict = {'1-4-2-3-1': ['GK', 'RB|RWB', 'RCB|CB', 'LCB|CB', 'LB|LWB', 'CDM|CM', 'CDM|CM', 'RM|RW|RF', 'CM|CAM', 'LM|LW|LF', 'CF|ST'],
                '1-4-3-3': ['GK', 'RB|RWB', 'LCB|CB', 'RCB|CB', 'LB|LWB', 'CDM|CM', 'CDM|CM', 'CDM|CM|CAM', 'RW|RF|ST', 'CF|ST', 'LW|LF|ST'],
                '1-4-4-2': ['GK', 'RB|RWB', 'RCB|CB', 'LCB|CB', 'LB|LWB', 'RM|RW|RF', 'CDM|CM', 'CDM|CM|CAM', 'LM|LW|LF', 'CF|ST', 'CF|ST'],
                '1-4-5-1': ['GK', 'RB|RWB', 'RCB|CB', 'LCB|CB', 'LB|LWB', 'RM|RW|RF', 'CDM|CM', 'CDM|CM|CAM', 'LM|LW|LF', 'CF|ST', 'CF|ST'],
                '1-4-3-1-2': ['GK', 'RB|RWB', 'LCB|CB', 'RCB|CB', 'LB|LWB', 'CDM|CM', 'CDM|CM', 'CDM|CM|CAM', 'CM|CAM|CF', 'CF|ST', 'CF|ST'],
                '1-3-4-3': ['GK', 'RCB|CB', 'LCB|RCB|CB', 'LCB|CB|CDM', 'RWB|RM|RF', 'CDM|CM|CAM', 'CDM|CM|CAM', 'LWB|LM|LF', 'RW|RF|ST', 'CF|ST', 'LW|LF|ST'],
                '1-3-5-2': ['GK', 'RCB|CB', 'LCB|RCB|CB', 'LCB|CB|CDM', 'RM|RWB|RB', 'CDM|CM', 'CDM|CM|CAM', 'CDM|CM|CAM', 'LM|LWB|LB', 'CF|ST', 'CF|ST'], 
                '1-3-4-1-2': ['GK', 'RCB|CB', 'LCB|RCB|CB', 'LCB|CB|CDM', 'RM|RW|RF', 'CDM|CM', 'CDM|CM', 'LM|LW|LF', 'CM|CAM|CF', 'CF|ST', 'CF|ST'],}

    # the dataframe is reduced to only the specified team
    team = extract_one_team(d,specification)
    #reduce the datframe to only the columns of interest
    team = team[['short_name', "player_positions", 'overall']]

    # dict in which the formation string is assigned to its rating (sum of all players in this formation)
    formations_value_dict = {}
    last_max_val = 0
    #formation which had the best rating to this moment
    last_best_formation = ""

    #iterate over all formations in the dict
    for formation in formations_dict:
            # list with the valid positions for a formation
            positions_list = []
            positions_list = formations_dict[formation]
            #copy of the available squad
            team_copy = team.copy()
            #dictionary in which selected players (because theiy are the best at this position) are put
            save_players = {}

            # iterate over all positions in this fromation
            for pos in positions_list:
                    #extract all the players in the squad which ca play this position
                    best_ps = team_copy[team_copy['player_positions'].str.contains(pos)]
                    #select the player in the first row as best player at this position
                    try:
                        best_p = best_ps.iloc[0]
                    except: 
                        continue
                    #save the name of this player
                    name = best_p.short_name
                    #in the dict assign the players name its overall
                    save_players[name] = best_p.overall
                    #delete the selected player from the squad so that she can not ocurr twice in the lineup
                    team_copy.drop(team_copy.index[team_copy['short_name'] == name], inplace=True)
                    
                    #if the whole lineup which contain 11 players are found
                    if len(save_players) == 11:
                        #calculate the value for this formation: it is the sum of all individual players rating
                        team_rating = sum(save_players.values())
                        formations_value_dict[formation] = team_rating
                    else: 
                            # if the formation does not find 11 players, exclude this formation by setting the formation rate to 0
                            formations_value_dict[formation] = 0

                    # look at all formations ratings and select the one with the maximal value as current best formation (string)
                    current_best_formation = max(formations_value_dict, key=formations_value_dict.get)
                    # save the value of the formation with the highest rating
                    current_max_val = max(formations_value_dict.values())
                    # if the current formation has a higher formation rating than the ones before then set the current best formation to the current player list 
                    if(current_max_val > last_max_val):
                        current_player_list = save_players
                        last_max_val = current_max_val
                        last_best_formation = current_best_formation
                    #if there was no improvement in the rating of the formation then do nothing


    print('One of the best formations for ' + specification + ' is the ' + str(last_best_formation), end = '. \n')
    print('With the following lineup its overall rating is then ' + str(round((formations_value_dict[last_best_formation])/11, 2)), end ='. \n')


    formations_str_dict = {'1-4-2-3-1': ['Goalkeeper', 'Rightback', 'Centerback', 'Centerback', 'Leftback', 'Central Midfielder', 'Central Midfielder', 'Right Midfielder', 'Central Midfielder', 'Left Midfielder', 'Forward'],
                    '1-4-3-1-2': ['Goalkeeper', 'Rightback', 'Centerback', 'Centerback', 'Leftback', 'Central Midfielder', 'Central Midfielder', 'Central Midfielder', 'Central Midfielder', 'Forward', 'Forward'],
                    '1-4-3-2-1': ['Goalkeeper', 'Rightback', 'Centerback', 'Centerback', 'Leftback', 'Central Midfielder', 'Central Midfielder', 'Central Midfielder', 'Central Midfielder', 'Central Midfielder', 'Forward'],
                    '1-4-3-3': ['Goalkeeper', 'Rightback', 'Centerback', 'Centerback', 'Leftback', 'Central Midfielder', 'Central Midfielder', 'Central Midfielder', 'Forward', 'Forward', 'Forward'],
                    '1-4-4-2': ['Goalkeeper', 'Rightback', 'Centerback', 'Centerback', 'Leftback', 'Right Midfielder', 'Central Midfielder', 'Central Midfielder', 'Left Midfielder', 'Forward', 'Forward'],
                    '1-4-5-1': ['Goalkeeper', 'Rightback', 'Centerback', 'Centerback', 'Leftback', 'Right Midfielder', 'Central Midfielder', 'Central Midfielder', 'Left Midfielder', 'Central Midfielder', 'Forward'],
                    '1-3-4-1-2': ['Goalkeeper', 'Centerback', 'Centerback', 'Centerback', 'Right Midfielder', 'Central Midfielder', 'Central Midfielder', 'Left Midfielder', 'Central Midfielder', 'Forward', 'Forward'],
                    '1-3-4-3': ['Goalkeeper', 'Centerback', 'Centerback', 'Centerback', 'Right Midfielder', 'Central Midfielder', 'Central Midfielder', 'Left Midfielder', 'Forward', 'Forward', 'Forward'],
                    '1-3-5-2': ['Goalkeeper', 'Centerback', 'Centerback', 'Centerback', 'Right Midfielder', 'Central Midfielder', 'Central Midfielder', 'Central Midfielder', 'Left Midfielder', 'Forward', 'Forward']}
    
    #make a datframe to show the lineup in a table
    df = pd.DataFrame(list(current_player_list.items()), columns = ['Name', 'Overall Rating'])
    
    #get the more readable position description for the formation which was selected
    for formation in formations_str_dict:
        if(last_best_formation == formation):
            positions = list(formations_str_dict.get(formation))
            #insert the list of position as new column in the table
            df.insert(2, 'Position', positions)

    df = df.set_index('Name')
    display(df)

'''
plots the correlation of overall with passing, ball control and physic rating compared for defenders and offensive players
'''
def physic_overall_corr(data): 
    # get rid of nan problems
    data.fillna(0, inplace=True)
    # make a new boolean column with true if the player is a defender 
    data['is_defender'] = data['player_positions'].str.contains(pat = 'B') 
    #delete the gaolkeepers
    data.drop(data.index[data['player_positions'] == 'GK'], inplace=True)
    # delete players with zero values
    data.drop(data[data.physic == 0].index, inplace=True)
    data.drop(data[data.skill_ball_control == 0].index, inplace=True)
    data.drop(data[data.passing == 0].index, inplace=True)

    # define x and y values 
    x_vars = ["passing", "skill_ball_control", "physic"]
    y_vars = ["overall"]
    
    #make a opairplot with the specified x and y values, color discrimination by the column is_defender and with markers o and D
    g = sns.pairplot(data, hue="is_defender",markers=["o","D"], x_vars=x_vars, y_vars=y_vars)
    g.map_offdiag(sns.scatterplot)
    #set the plot size
    g.fig.set_size_inches(12,4)
    # remove the legend
    g._legend.remove()  
    # write a title 
    g.fig.suptitle('Correlation between Ratings', fontweight ='bold', fontsize=16)
    # make sure nothing is overlapping and the plot looks good
    g.fig.tight_layout() 
    #put a legend in the plot            
    g.fig.legend(labels=["Defenders","Attackers"])

    # draw an arrow and annotate it
    plt.gca().annotate(
        'better physic for defenders', 
        xy=(80, 70), 
        xytext=(87, 67),
        arrowprops=dict()
    )
    
    # draw polygon
    plt.gca().add_patch(mpatches.Polygon(([55.3, 66],[86, 71.8],[88.5, 92.5], [84, 92.5]),fill=False,edgecolor='black',lw=1, alpha=0.8))
    g.fig.set


'''
displays a stacked barplot of the counts of each ranking type in the specified national teams
'''
def player_type_dis(data, specification):
    #extract relevant columns
    df = data[['nationality_name', 'ranking type']]

    #drop other nations of only three nations should be displayed
    if(specification != 'none'):
        n1 = specification[0]
        n2 = specification[1]
        n3 = specification[2]
        df = df[ (df['nationality_name'] == n1) | (df['nationality_name']== n2) | (df['nationality_name'] == n3)]
    
    #count occurences of each ranking type
    df = df.groupby('nationality_name')['ranking type'].value_counts().to_frame()
    
    #name the column for the counts
    df = df.rename(columns={df.columns[0]: 'counts'})
    #reshape the dataframe
    df = df.reset_index()
    df = df.pivot(index='nationality_name', columns='ranking type', values= 'counts')
    #drop the column 0
    df= df[['moderate player', 'good player', 'world class player']]
    #replace all nans with zeros
    df = df.fillna(0)
    #sort by the value of moderate player
    df = df.sort_values(by = 'moderate player')

    #plot stacked bar plot
    df.plot(kind='bar', stacked=True, color=['red', 'gold' ,'lime' ])
    plt.gcf().set_size_inches(8, 5)

    # labels for x and y axis
    plt.ylabel(' Number of Players',  fontsize = 12)
    plt.ylabel('Nations',  fontsize = 12)
    # title of plot
    plt.title('Player Strength Distribution Per Nation', weight='bold').set_fontsize('14')


    













