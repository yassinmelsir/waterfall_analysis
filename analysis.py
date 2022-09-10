from data import cap_Table

def exit_dist(valuation):
    c_payout = 0
    financed_valuation = cap_Table['common']['invested'] + cap_Table['a']['invested'] + cap_Table['b']['invested'] + cap_Table['c']['invested']
    total_shares = cap_Table['common']['shares'] + cap_Table['a']['shares'] + cap_Table['b']['shares'] + cap_Table['c']['shares']
    pro_rata_ammount = valuation - financed_valuation
    pro_rata_shares = total_shares

    c_common_payout = valuation*(cap_Table['c']['shares']/total_shares)
    b_common_payout = valuation*(cap_Table['b']['shares']/total_shares)
    a_common_payout = valuation*(cap_Table['a']['shares']/total_shares)

    c_cap = 2*cap_Table['c']['invested']
    b_cap = 2*cap_Table['b']['invested']
    a_cap = 2*cap_Table['a']['invested']

    b_liq_payout = (valuation-financed_valuation)*(cap_Table['b']['shares']/total_shares) + cap_Table['b']['invested']
    a_liq_payout = (valuation-financed_valuation)*(cap_Table['a']['shares']/total_shares) + cap_Table['a']['invested']
    c_liq_payout = (valuation-financed_valuation)*(cap_Table['c']['shares']/total_shares) + cap_Table['c']['invested']
    print(b_liq_payout > b_cap)
    
    if c_common_payout < c_liq_payout:
        if c_liq_payout > c_cap:
            c_payout = c_cap
        else:
            c_payout = cap_Table['c']['invested']
            if b_liq_payout > b_cap:
                print(a_liq_payout > a_cap)
                if a_liq_payout > a_cap:
                    pro_rata_ammount -= (b_cap + a_cap)/2
                    pro_rata_shares -= (cap_Table['b']['shares'] + cap_Table['a']['shares'])
                    c_payout += pro_rata_ammount*(cap_Table['c']['shares']/pro_rata_shares)
                else:
                    print('1')
                    pro_rata_ammount -= b_cap/2
                    pro_rata_shares -= cap_Table['b']['shares']
                    c_payout += pro_rata_ammount*(cap_Table['c']['shares']/pro_rata_shares)

            else:
                if a_liq_payout > a_cap:
                    pro_rata_ammount -= a_cap/2
                    pro_rata_shares -= cap_Table['a']['shares']
                    c_payout += pro_rata_ammount*(cap_Table['c']['shares']/pro_rata_shares)
                else:
                    c_payout += pro_rata_ammount*(cap_Table['c']['shares']/pro_rata_shares)
    else: 
        c_payout = c_common_payout
            

    # print(c_payout)
    
   


exit_dist(60000000)
exit_dist(25000000)
exit_dist(35000000)
exit_dist(45000000)