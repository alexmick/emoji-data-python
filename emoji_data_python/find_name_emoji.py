import emojis
import re 

def find_name(text  , return_list= True):
    try:
        if return_list == True:
            list_name =  re.findall(r':\w+:',str(emojis.decode(text))) # Lists the names of all emoji
            count_emojis = emojis.count(text) #Count the Emojis
            list_name_emoji = [] 
            for item in range(count_emojis):#for example convert  => :smile: to smile
                list_name_emoji.append((str(list_name[item]).replace(':',''))) 
            return list_name_emoji
        else:
            return str(emojis.decode(text)).replace(':','') # for example convert => :smile: to smile
    except:
        print("Eroor")
