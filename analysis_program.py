from logging import captureWarnings
from analysis_data import cap_table

def exit_dist(valuation):

    total_shares = cap_table['common']['shares'] + cap_table['a']['shares'] + cap_table['b']['shares'] + cap_table['c']['shares']

    c_shares = cap_table['c']['shares']
    b_shares = cap_table['b']['shares']
    a_shares = cap_table['a']['shares']
    com_shares = cap_table['common']['shares']

    c_cap = 2*cap_table['c']['invested']
    b_cap = 2*cap_table['b']['invested']
    a_cap = 2*cap_table['a']['invested']    

    if valuation >= 60000000:
        #C, B and A convert to common shares
        payouts = [valuation*(c_shares/total_shares), valuation*(b_shares/total_shares), valuation*(a_shares/total_shares), valuation*(com_shares/total_shares)]
        print(payouts)
   
    elif 60000000 > valuation > 51000000:
        #C defers to LP, B and A converts to common shares
        payout_amount = valuation-c_cap
        payout_shares = total_shares-cap_table['c']['shares']
        payouts = [c_cap, (payout_amount)*(b_shares/payout_shares), (payout_amount)*(a_shares/payout_shares), (payout_amount)*(com_shares/payout_shares)]
        print(payouts)
        return None

    elif 51000000 >= valuation > 46200000:
        #C and B defer to liquid preferences, A converts to common shares
        payout_amount = valuation-c_cap-b_cap
        payout_shares = total_shares-cap_table['b']['shares']-cap_table['c']['shares']
        payouts = [c_cap, b_cap, (payout_amount)*(a_shares/payout_shares), (payout_amount)*(com_shares/payout_shares)]
        print(payouts)
        

    elif 46200000 >= valuation > 43500000:
        #C and B defer to liquid preferences, A converts to common shares; B is at cap.
        payout_amount = valuation-cap_table['c']['invested']-b_cap
        payout_shares = total_shares-cap_table['b']['shares']
        payouts = [cap_table['c']['invested']+payout_amount*(c_shares/payout_shares), b_cap, (payout_amount)*(a_shares/payout_shares), (payout_amount)*(com_shares/payout_shares)]
        print(payouts)
        return None

    elif 43500000 >= valuation > 38500000:
        #C, B and A defer to liquid preferences; B and A are both at cap.
        payout_amount = valuation-cap_table['c']['invested']-b_cap-a_cap
        payout_shares = total_shares-cap_table['a']['shares']-cap_table['b']['shares']
        payouts = [cap_table['c']['invested']+(payout_amount*(c_shares/payout_shares)), b_cap, a_cap, (payout_amount)*(com_shares/payout_shares)]
        print(payouts)
        return None

    elif 38500000 >=  valuation >= 31500000:
        #C, B and A defer to liquid preferences; A is at cap.
        payout_amount = valuation-cap_table['c']['invested']-cap_table['b']['invested']-cap_table['a']['invested']*2
        payout_shares = total_shares-cap_table['a']['shares']
        payouts = [cap_table['c']['invested']+payout_amount*(c_shares/payout_shares), cap_table['b']['invested']+payout_amount*(b_shares/payout_shares), a_cap, (payout_amount)*(com_shares/payout_shares)]
        print(payouts)
        return None

    else:
        #C, B and A defer to liquid preferences;
        payout_amount = valuation-cap_table['c']['invested']-cap_table['b']['invested']-cap_table['a']['invested']
        payout_shares = total_shares
        payouts = [cap_table['c']['invested']+payout_amount*(c_shares/payout_shares), cap_table['b']['invested']+payout_amount*(b_shares/payout_shares), cap_table['a']['invested']+payout_amount*(a_shares/payout_shares), (payout_amount)*(com_shares/payout_shares)]
        print(payouts)
        return None

print('stage 1')
exit_dist(60000000)
print('stage 2')
exit_dist(25000000)
print('stage 3')
exit_dist(35000000)
print('stage 4')
exit_dist(45000000)
print('stage 5')
exit_dist(40000000)
exit_dist(50000000)
exit_dist(70000000)
print('stage 6')
exit_dist(39000000)
exit_dist(44000000)
exit_dist(47000000)
