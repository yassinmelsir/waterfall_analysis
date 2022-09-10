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
        c_payout += payout_ammount*(c_shares/total_shares)
        total_shares -= c_shares
        payout_ammount -= c_payout
        b_payout += payout_ammount*(b_shares/total_shares)
        total_shares -= b_shares
        payout_ammount -= b_payout
        a_payout += payout_ammount*(a_shares/total_shares)
        total_shares -= a_shares
        payout_ammount -= a_payout
        com_payout += payout_ammount*(com_shares/total_shares)
        return print(c_payout, b_payout, a_payout, com_payout, valuation == (c_payout + b_payout + a_payout + com_payout))
    
    # at valuations less than 60m and greater than or equal to 40m it never makes sense for pref C or pref B to take common shares, and B will always Cap.
    # at valulations of more than or equal to ..... C will always cap, C will always LP until .... where CS start too outpace LPs
    # at valulations of more than or equal to ..... B will always cap, B will always LP until .... where CS start too outpace LPs
    # at valulations of more than or equal to 31.5m A will always cap, A will always LP until 43.5m where CS start too outpace LPs
    # 
    elif  valuation >= 35000000:

        # 4 scenarios here: A and B take common shares, A and B take LPs, A takes Lps and B takes common shares or A takes common shares and B takes Lps
        # C takes LP, A and B take common shares
        # scenario_One = [cap_Table['c']['invested']+(payout_ammount-cap_Table['c']['invested'])*(c_shares/total_shares),payout_ammount*(b_shares/total_shares),payout_ammount*(a_shares/total_shares),payout_ammount*(com_shares/total_shares)]
        # print('C takes LP, A and B take common shares: ', scenario_One)

        # C, B, and A choose LPs
        scO_payout_ammount = payout_ammount-cap_Table['c']['invested']-cap_Table['b']['invested']*2-cap_Table['a']['invested']
        scO_shares = total_shares - cap_Table['b']['shares']
        scenario_Two = [cap_Table['c']['invested']+scO_payout_ammount*(c_shares/scO_shares), b_cap, cap_Table['a']['invested']+scO_payout_ammount*(a_shares/scO_shares), (scO_payout_ammount)*(com_shares/scO_shares)]
        print('C, B, and A choose LPs: ', scenario_Two)

        # C and B take LPs, A takes Common shares
        scT_payout_ammount = payout_ammount-cap_Table['c']['invested']-cap_Table['b']['invested']*2
        scT_shares = total_shares - cap_Table['b']['shares']
        scenario_Two = [cap_Table['c']['invested']+scT_payout_ammount*(c_shares/scT_shares), b_cap, scT_payout_ammount*(a_shares/scT_shares), (scO_payout_ammount)*(com_shares/scT_shares)]
        print('C, B, choose LPs, A chooses common shares: ', scenario_Two)
        # # C and B take LPs, B takes Common shares
        # scF_payout_ammount = payout_ammount-cap_Table['c']['invested']-cap_Table['a']['invested']
        # scenario_Four = [cap_Table['c']['invested']+scF_payout_ammount*(c_shares/total_shares),scF_payout_ammount*(b_shares/total_shares),cap_Table['a']['invested']+scF_payout_ammount*(a_shares/total_shares),scF_payout_ammount*(com_shares/total_shares)]
        # print('C and A take LPs, B takes Common shares: ', scenario_Four)
        return None   
    elif 31500000 > valuation:
        # at 31.5m A begins to Cap
        scO_payout_ammount = payout_ammount-cap_Table['c']['invested']-cap_Table['b']['invested']-cap_Table['a']['invested']*2
        scO_shares = total_shares-cap_Table['a']['shares']
        scenario_Two = [cap_Table['c']['invested']+scO_payout_ammount*(c_shares/scO_shares), cap_Table['b']['invested']+scO_payout_ammount*(b_shares/scO_shares), a_cap, (scO_payout_ammount)*(com_shares/scO_shares)]
        print('C, B, and A choose LPs: ', scenario_Two)
        return None

        

        


    if c_liq_payout > c_cap:
        if b_liq_payout > b_cap:
            if a_liq_payout > a_cap:
                c_payout += payout_ammount*(c_shares/total_shares)
                total_shares -= c_shares
                payout_ammount -= c_payout
                b_payout += payout_ammount*(b_shares/total_shares)
                total_shares -= b_shares
                payout_ammount -= b_payout
                a_payout += payout_ammount*(a_shares/total_shares)
                total_shares -= a_shares
                payout_ammount -= a_payout
                com_payout += payout_ammount*(com_shares/total_shares)
            else:
                print('')

        else:
            if a_liq_payout > a_cap:
                print('')
            else:
                print('')
    else:
        if b_liq_payout > b_cap:
            if a_liq_payout > a_cap:
                b_payout += b_cap
                total_shares -= b_shares
                payout_ammount -= b_payout
                if payout_ammount*(c_shares/total_shares) > (cap_Table['c']['invested'] + (valuation-cap_Table['c']['invested']-b_payout)*(c_shares/(total_shares))):
                    c_payout += payout_ammount*(c_shares/total_shares)
                    total_shares -= c_shares
                    payout_ammount -= c_payout
                else: 
                    c_payout += (cap_Table['c']['invested'] + (valuation-cap_Table['c']['invested']-b_payout)*(c_shares/(total_shares)))
                    payout_ammount -= cap_Table['c']['invested']

                if (payout_ammount)*(a_shares/total_shares) > (valuation-cap_Table['c']['invested']-b_payout)*(a_shares/total_shares):
                    print(payout_ammount)
                    a_payout += payout_ammount*(a_shares/total_shares)
                else: 
                    if (cap_Table['a']['invested'] + (valuation-cap_Table['c']['invested']-b_payout)*(a_shares/total_shares)) < a_cap:
                        a_payout += (cap_Table['a']['invested'] + (valuation-cap_Table['c']['invested']-b_payout)*(a_shares/total_shares))
                    else: 
                        a_payout += payout_ammount*(a_shares/total_shares)
                
                com_payout = valuation - a_payout - b_payout - c_payout
            else:
               print('')
            

        else:
            if a_liq_payout > a_cap:
                a_payout += a_cap
                total_shares -= a_shares
                payout_ammount -= a_payout
                if payout_ammount*(c_shares/total_shares) > (cap_Table['c']['invested'] + (valuation-financed_valuation-a_payout/2)*(c_shares/(total_shares))):
                    c_payout += payout_ammount*(c_shares/total_shares)
                    total_shares -= c_shares
                    payout_ammount -= c_payout
                else: 
                    c_payout += (cap_Table['c']['invested'] + (valuation-financed_valuation-a_payout/2)*(c_shares/(total_shares)))
        
                if payout_ammount*(b_shares/total_shares) > (cap_Table['b']['invested'] + (valuation-financed_valuation-a_payout/2)*(b_shares/(total_shares))):
                    b_payout += payout_ammount*(b_shares/total_shares)
                    total_shares -= b_shares
                    payout_ammount -= b_payout
                else: 
                    b_payout += (cap_Table['b']['invested'] + (valuation-financed_valuation-a_payout/2)*(b_shares/(total_shares)))
                
                
                com_payout = valuation - a_payout - b_payout - c_payout
            else:
                if payout_ammount*(c_shares/total_shares) > (cap_Table['c']['invested'] + (valuation-financed_valuation)*(c_shares/(3000000))):
                    c_payout += payout_ammount*(c_shares/total_shares)
                    total_shares -= c_shares
                    payout_ammount -= c_payout
                else: 
                    c_payout += (cap_Table['c']['invested'] + (valuation-financed_valuation)*(c_shares/(3000000)))
        
                if payout_ammount*(b_shares/total_shares) > (cap_Table['b']['invested'] + (valuation-financed_valuation)*(b_shares/(3000000))):
                    b_payout += payout_ammount*(b_shares/total_shares)
                    total_shares -= b_shares
                    payout_ammount -= b_payout
                else: 
                    b_payout += (cap_Table['b']['invested'] + (valuation-financed_valuation)*(b_shares/(3000000)))

                if payout_ammount*(a_shares/total_shares) > (cap_Table['a']['invested'] + (valuation-financed_valuation)*(a_shares/(3000000))):
                    a_payout += payout_ammount*(a_shares/total_shares)
                    total_shares -= a_shares
                    payout_ammount -= a_payout
                else: 
                    print('b')
                    a_payout += (cap_Table['a']['invested'] + (valuation-financed_valuation)*(a_shares/(3000000)))
                # a_payout += (cap_Table['a']['invested'] + (valuation-financed_valuation)*(a_shares/total_shares))
                com_payout = valuation - a_payout - b_payout - c_payout
                
                
    print(c_payout, b_payout, a_payout, com_payout, valuation == (c_payout + b_payout + a_payout + com_payout))
    # (c_payout + b_payout + a_payout)
    
# exit_dist(60000000)
exit_dist(25000000)
exit_dist(31500000)
exit_dist(34000000)
# exit_dist(35000000)
# exit_dist(37000000)
# exit_dist(43500000)
# exit_dist(44000000)
# exit_dist(45000000)
# C begins to cap......
# exit_dist(46800000)
# exit_dist(47000000)
# exit_dist(50000000)
# exit_dist(55000000)
# exit_dist(58000000)
# exit_dist(70000000)
# exit_dist(39000000)
