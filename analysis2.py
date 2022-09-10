from logging import captureWarnings
from data import cap_Table

def exit_dist(valuation):
    c_payout = 0
    b_payout = 0
    a_payout = 0
    com_payout = 0
    financed_valuation = cap_Table['common']['invested'] + cap_Table['a']['invested'] + cap_Table['b']['invested'] + cap_Table['c']['invested']
    total_shares = cap_Table['common']['shares'] + cap_Table['a']['shares'] + cap_Table['b']['shares'] + cap_Table['c']['shares']
    payout_ammount = valuation

    c_shares = cap_Table['c']['shares']
    b_shares = cap_Table['b']['shares']
    a_shares = cap_Table['a']['shares']
    com_shares = cap_Table['common']['shares']

    c_cap = 2*cap_Table['c']['invested']
    b_cap = 2*cap_Table['b']['invested']
    a_cap = 2*cap_Table['a']['invested']

    b_liq_payout = (valuation-financed_valuation)*(cap_Table['b']['shares']/total_shares) + cap_Table['b']['invested']
    a_liq_payout = (valuation-financed_valuation)*(cap_Table['a']['shares']/total_shares) + cap_Table['a']['invested']
    c_liq_payout = (valuation-financed_valuation)*(cap_Table['c']['shares']/total_shares) + cap_Table['c']['invested']

    # with a cap of 2x and three rounds of preferred investors at amounts >= 60m, best outcome for investors will always be to convert to common shares 
    if valuation >= 60000000:
        scenario_Two = [payout_ammount*(c_shares/total_shares), payout_ammount*(b_shares/total_shares), payout_ammount*(a_shares/total_shares), payout_ammount*(com_shares/total_shares)]
        print('all cs', scenario_Two)
    # assumption: each investors attempts to maximize their profits
    # at valuations less than 60m and greater than or equal to 40m it never makes sense for pref C or pref B to take common shares, and B will always Cap.
    # at valulations of more than or equal to 46.2m C will always cap, C will always LP until 60m where CS start too outpace LPs
    # at valulations of more than or equal to 38.5 B will always cap, B will always LP until 51m where CS start too outpace LPs
    # at valulations of more than or equal to 31.5m A will always cap, A will always LP until 43.5 where CS start too outpace LPs
    elif 60000000 > valuation > 51000000:
        # a cs, b cs, c cap
        scTw_payout_ammount = payout_ammount-cap_Table['c']['invested']*2
        scTw_shares = total_shares-cap_Table['c']['shares']
        scenario_Two = [c_cap, (scTw_payout_ammount)*(b_shares/scTw_shares), (scTw_payout_ammount)*(a_shares/scTw_shares), (scTw_payout_ammount)*(com_shares/scTw_shares)]
        print('a cs, b cap, C lps: ', scenario_Two)
        return None
    elif 51000000 >= valuation > 46200000:
        # a cs, b cap, c cap
        scO_payout_ammount = payout_ammount-cap_Table['c']['invested']*2-cap_Table['b']['invested']*2
        scO_shares = total_shares-cap_Table['b']['shares']-cap_Table['c']['shares']
        scenario_Two = [c_cap, b_cap, (scO_payout_ammount)*(a_shares/scO_shares), (scO_payout_ammount)*(com_shares/scO_shares)]
        print('a cs, b cap, C lps: ', scenario_Two)
        # a cs, b cs, c cap
        scTw_payout_ammount = payout_ammount-cap_Table['c']['invested']*2
        scTw_shares = total_shares-cap_Table['c']['shares']
        scenario_Two = [c_cap, (scTw_payout_ammount)*(b_shares/scTw_shares), (scTw_payout_ammount)*(a_shares/scTw_shares), (scTw_payout_ammount)*(com_shares/scTw_shares)]
        print('a cs, b cap, C lps: ', scenario_Two)
        return None
        

    elif 46200000 >= valuation > 43500000:
        # a cs, b cap, C lps
        scT_payout_ammount = payout_ammount-cap_Table['c']['invested']-cap_Table['b']['invested']*2
        scT_shares = total_shares-cap_Table['b']['shares']
        scenario_Two = [cap_Table['c']['invested']+scT_payout_ammount*(c_shares/scT_shares), b_cap, (scT_payout_ammount)*(a_shares/scT_shares), (scT_payout_ammount)*(com_shares/scT_shares)]
        print('a cs, b cap, C lps: ', scenario_Two)
        return None

    elif 43500000 >= valuation > 38500000:
        # a cap, b cap, C lps
        scO_payout_ammount = payout_ammount-cap_Table['c']['invested']-cap_Table['b']['invested']*2-cap_Table['a']['invested']*2
        scO_shares = total_shares-cap_Table['a']['shares']-cap_Table['b']['shares']
        print(scO_payout_ammount,(c_shares/scO_shares))
        scenario_Two = [cap_Table['c']['invested']+(scO_payout_ammount*(c_shares/scO_shares)), b_cap, a_cap, (scO_payout_ammount)*(com_shares/scO_shares)]
        print('r a cap, b cap, C lps: ', scenario_Two)
        return None

    elif 38500000 >=  valuation >= 31500000:
        scO_payout_ammount = payout_ammount-cap_Table['c']['invested']-cap_Table['b']['invested']-cap_Table['a']['invested']*2
        scO_shares = total_shares-cap_Table['a']['shares']
        scenario_Two = [cap_Table['c']['invested']+scO_payout_ammount*(c_shares/scO_shares), cap_Table['b']['invested']+scO_payout_ammount*(b_shares/scO_shares), a_cap, (scO_payout_ammount)*(com_shares/scO_shares)]
        print('C, B, and A choose LPs: ', scenario_Two)
        return None

    elif 31500000 > valuation :
        # at 31.5m A begins to Cap
        scO_payout_ammount = payout_ammount-cap_Table['c']['invested']-cap_Table['b']['invested']-cap_Table['a']['invested']
        scO_shares = total_shares
        scenario_Two = [cap_Table['c']['invested']+scO_payout_ammount*(c_shares/scO_shares), cap_Table['b']['invested']+scO_payout_ammount*(b_shares/scO_shares), cap_Table['a']['invested']+scO_payout_ammount*(a_shares/scO_shares), (scO_payout_ammount)*(com_shares/scO_shares)]
        print('C, B, and A choose LPs: ', scenario_Two)
        return None

        
exit_dist(60000000)
exit_dist(25000000)
# exit_dist(31500000)
exit_dist(35000000)
# exit_dist(40000000)
# exit_dist(37500000)
exit_dist(45000000)
# exit_dist(46200000)
# C begins to cap......
# exit_dist(46800000)
# exit_dist(47000000)
# exit_dist(50000000)
# exit_dist(51000000)
# exit_dist(55000000)
exit_dist(70000000)
# exit_dist(39000000)
