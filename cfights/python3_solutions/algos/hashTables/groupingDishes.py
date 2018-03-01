from collections import Counter
from collections import OrderedDict

def groupingDishes(dishes):
    dish_dict = OrderedDict(sorted({dishes[lst][0]:sorted([dishes[lst][food] for food in range(1,len(dishes[lst]))]) for lst in range(len(dishes))}.items(),key=lambda t: t[0]))

    ing = [dishes[lst][1:] for lst in range(len(dishes))]
    flat_ing = []
    for lst in ing:
        flat_ing += lst
    flat_ing.sort()
    cnt_ing = Counter(flat_ing)
    two_or_more = sorted([[ingred] for ingred in cnt_ing if cnt_ing[ingred] > 1])
    for ingredient in two_or_more:
        for item in dish_dict:
            if ingredient[0] in dish_dict[item]:
                ingredient.append(item)
    return(two_or_more)
