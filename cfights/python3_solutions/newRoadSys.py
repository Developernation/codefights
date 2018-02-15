#Once upon a time, in a kingdom far, far away, there lived a king Byteasar I. 
#As a kind and wise ruler, he did everything in his (unlimited) power to make
#life of his subjects comfortable and pleasant. One cold evening a messenger 
#arrived to the king's castle with the latest news: all kings in the Kingdoms 
#Union started to enforce traffic laws! 
#In order not to lose his membership in the Union, king Byteasar had to do the 
#same in his kingdom. But what would the citizens think of it?

#The king decided to start introducing the changes with something more or 
#less simple: change all the roads in the kingdom from two-directional to 
#one-directional. He personally prepared the roadRegister of the new roads,
#and now he needs to make sure that the road system is convenient and there will 
#be no traffic jams, i.e. each city has the same number of incoming and outgoing roads. 
#As the Hand of the King, you're the one who should check it.

def newRoadSystem(roadReg):
    #count of out rows           
    rd_map = [{i:{'road_out':[roadReg[i].index(roadReg[i][elm],elm) for elm in range(len(roadReg[i])) if roadReg[i][elm] is True],'road_in':[]}} for i in range(len(roadReg))]
    rd_map_keys = [city for city in range(len(roadReg))]
    for elm in rd_map_keys: #elm represents city in the rd_map_keys list
        for ind in range(len(rd_map)):
            #does not count current city (ind = city key in the rd_map list of dicts)
            if ind != elm:            
                for item in rd_map[ind][ind]['road_out']:
                    if item == elm: #this means if the item in the list for roads_out lead to another city 
                        rd_map[elm][elm]['road_in'].append(ind) #now append it to the city that the road leads to
                        print(elm, ' ' + str(ind) +', ' +str(item))
        if len(rd_map[elm][elm]['road_out']) != len(rd_map[elm][elm]['road_in']):
            return False
    return True 