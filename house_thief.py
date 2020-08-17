def house_thieves(house_net_worth, current_index):
    if current_index >= len(house_net_worth):
        return 0 
    
    #case1 - when first house is selected then after skipping adjacent house the 3 rd house is selected nd so on
    case1 = house_net_worth[current_index] + house_thieves(house_net_worth, current_index+2)
    #case2 - when first house is not selected and adjacent house that is 1st house is selected and so on
    case2 = house_thieves(house_net_worth, current_index+1)
    return max(case1, case2)

house_net_worth = [6,7,1,30,8,2,4]
print(house_thieves(house_net_worth, 0))