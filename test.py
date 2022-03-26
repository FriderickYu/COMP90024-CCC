import json
import ast

with open('./smallTwitter.json', 'r', encoding="utf-8") as f:
    data = json.load(f)
with open('./sydGrid.json', 'r', encoding="utf-8") as g:
    grid_data = json.load(g)

#language types
language_dict = {'en': 'English', 'ar': 'Arabic', 'bn': 'Bengali', 'cs': 'Czech', 'da': 'Danish', 'de': 'German', 'el': 'Greek','es': 'Spanish', 'fa': 'Persian', 'fi': 'Finnish', 'fil': 'Filipino', 'fr': 'French', 'he': 'Hebrew', 'hi': 'Hindi', 'hu': 'Hungarian', 'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese', 'ko': 'Korean', 'msa': 'Malay', 'nl': 'Dutch', 'no': 'Norwegian', 'pl': 'Polish', 'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'sv': 'Swedish', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'vi': 'Vietnamese', 'zh-cn': 'Chinese', 'zh-tw': 'Chinese'}

#print(data, type(data))
#print(data["rows"][0]["doc"]["coordinates"])


#filter all the none type data
def data_with_coordinates(twitters):
    list_a=[]
    for i in twitters["rows"]:
        if i["doc"]["coordinates"] != None:
            list_a.append(i)
        else:
            pass
    return list_a

list_a = data_with_coordinates(data)
print(list_a)
#print(len(list_a))


#append grid name with 4 points
grids = {}
for i in grid_data["features"]:
    #print(i['geometry']['coordinates'][0])
    grids[str(i['geometry']['coordinates'][0][:4])] = i['properties']['id']

#print(grids)
#print('test:',ast.literal_eval(str(i['geometry']['coordinates'][0])))


#the function that check whether this block in this grid
def whether_in_grid(point, grid):
    if point[0] <= grid[0][0]:
        return False
    elif point[1] > grid[0][1]:
        return False
    elif point[1] <= grid[1][1]:
        return False
    elif point[0] > grid[2][0]:
        return False
    else:
        return True


#print the result
print(' Cell     #Total Tweets  #Number of language used    #Top 10 Languages & #Tweets')

#compute the result
for j in list(grids):
    twitter_dict={}
    for k in list_a:
        if whether_in_grid(k["doc"]["coordinates"]['coordinates'], ast.literal_eval(j)) and k["doc"]["lang"] not in twitter_dict:
            twitter_dict[k["doc"]["lang"]] = 1
        elif whether_in_grid(k["doc"]["coordinates"]['coordinates'], ast.literal_eval(j)) and k["doc"]["lang"] in twitter_dict:
            number = twitter_dict[k["doc"]["lang"]]
            number = number + 1
            twitter_dict[k["doc"]["lang"]] = number
        else:
            pass
    top_10_dict = {k: v for k, v in sorted(twitter_dict.items(), key=lambda item: item[1])}
    top_10_list = []
    for (l,m) in list(top_10_dict.items()):
        if l in language_dict:
            top_10_list.append(str(language_dict[l]) + '-' + str(m))
        else:
            pass
    print(grids[j], sum(twitter_dict.values()), len(list(twitter_dict)), ','.join(top_10_list))


