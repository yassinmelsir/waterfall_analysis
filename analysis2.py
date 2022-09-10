from logging import captureWarnings
from data import cap_Table

def exit_dist(valuation):

    total_shares = cap_Table['common']['shares'] + cap_Table['a']['shares'] + cap_Table['b']['shares'] + cap_Table['c']['shares']
    payout_ammount = valuation

    c_shares = cap_Table['c']['shares']
    b_shares = cap_Table['b']['shares']
    a_shares = cap_Table['a']['shares']
    com_shares = cap_Table['common']['shares']

    c_cap = 2*cap_Table['c']['invested']
    b_cap = 2*cap_Table['b']['invested']
    a_cap = 2*cap_Table['a']['invested']
    
    # Assumptions
    # Each investors attempts to maximize their profits
    # At valuations equal to or lower than 43.5m the best outome will always be for all investors defer to liquidation preferences.
    # At valuations greater than 43.5m, investor A will always convert to common shares
    # At valuations greater than 51m, investor B will always convert to common shares
    # At valuations equal to or greater than 60m the best outome will always be for all investors to convert to common shares.
    # At valulations of more than or equal to 46.2m investor C will always reach their cap
    # At valulations of more than or equal to 38.5 investor B will always reach their cap
    # At valulations of more than or equal to 31.5m investor A will always reach their cap

    if valuation >= 60000000:
        #C, B and A convert to common shares
        scenario_Two = [payout_ammount*(c_shares/total_shares), payout_ammount*(b_shares/total_shares), payout_ammount*(a_shares/total_shares), payout_ammount*(com_shares/total_shares)]
        print(scenario_Two)
   
    elif 60000000 > valuation > 51000000:
        #C defers to LP, B and A converts to common shares
        scTw_payout_ammount = payout_ammount-cap_Table['c']['invested']*2
        scTw_shares = total_shares-cap_Table['c']['shares']
        scenario_Two = [c_cap, (scTw_payout_ammount)*(b_shares/scTw_shares), (scTw_payout_ammount)*(a_shares/scTw_shares), (scTw_payout_ammount)*(com_shares/scTw_shares)]
        print(scenario_Two)
        return None

    elif 51000000 >= valuation > 46200000:
        #C and B defer to liquid preferences, A converts to common shares
        scO_payout_ammount = payout_ammount-cap_Table['c']['invested']*2-cap_Table['b']['invested']*2
        scO_shares = total_shares-cap_Table['b']['shares']-cap_Table['c']['shares']
        scenario_Two = [c_cap, b_cap, (scO_payout_ammount)*(a_shares/scO_shares), (scO_payout_ammount)*(com_shares/scO_shares)]
        print(scenario_Two)
        

    elif 46200000 >= valuation > 43500000:
        #C and B defer to liquid preferences, A converts to common shares; B is at cap.
        scT_payout_ammount = payout_ammount-cap_Table['c']['invested']-cap_Table['b']['invested']*2
        scT_shares = total_shares-cap_Table['b']['shares']
        scenario_Two = [cap_Table['c']['invested']+scT_payout_ammount*(c_shares/scT_shares), b_cap, (scT_payout_ammount)*(a_shares/scT_shares), (scT_payout_ammount)*(com_shares/scT_shares)]
        print(scenario_Two)
        return None

    elif 43500000 >= valuation > 38500000:
        #C, B and A defer to liquid preferences; B and A are both at cap.
        scO_payout_ammount = payout_ammount-cap_Table['c']['invested']-cap_Table['b']['invested']*2-cap_Table['a']['invested']*2
        scO_shares = total_shares-cap_Table['a']['shares']-cap_Table['b']['shares']
        scenario_Two = [cap_Table['c']['invested']+(scO_payout_ammount*(c_shares/scO_shares)), b_cap, a_cap, (scO_payout_ammount)*(com_shares/scO_shares)]
        print(scenario_Two)
        return None

    elif 38500000 >=  valuation >= 31500000:
        #C, B and A defer to liquid preferences; A is at cap.
        scO_payout_ammount = payout_ammount-cap_Table['c']['invested']-cap_Table['b']['invested']-cap_Table['a']['invested']*2
        scO_shares = total_shares-cap_Table['a']['shares']
        scenario_Two = [cap_Table['c']['invested']+scO_payout_ammount*(c_shares/scO_shares), cap_Table['b']['invested']+scO_payout_ammount*(b_shares/scO_shares), a_cap, (scO_payout_ammount)*(com_shares/scO_shares)]
        print(scenario_Two)
        return None

    elif 31500000 > valuation :
        #C, B and A defer to liquid preferences;
        scO_payout_ammount = payout_ammount-cap_Table['c']['invested']-cap_Table['b']['invested']-cap_Table['a']['invested']
        scO_shares = total_shares
        scenario_Two = [cap_Table['c']['invested']+scO_payout_ammount*(c_shares/scO_shares), cap_Table['b']['invested']+scO_payout_ammount*(b_shares/scO_shares), cap_Table['a']['invested']+scO_payout_ammount*(a_shares/scO_shares), (scO_payout_ammount)*(com_shares/scO_shares)]
        print(scenario_Two)
        return None

        
# exit_dist(60000000)
# exit_dist(25000000)
# exit_dist(35000000)
# exit_dist(45000000)
# exit_dist(40000000)
# exit_dist(50000000)
# exit_dist(70000000)
# exit_dist(39000000)
# exit_dist(44000000)
exit_dist(47000000)
