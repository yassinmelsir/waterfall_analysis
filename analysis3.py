from data import cap_Table

def exit_dist(valuation):
    # common shares payout for pref c is always higher than cap for c at valuations of >= 60: all commons at 60
    # common shares payout for pref b is always higher than cap for b at valuations of >= 42: commons for ba at 60 > val >= 42
    # common shares payout for pref a is always higher than cap for a at valuations of >= 27: commons for a at 42 > val >= 27
    if valuation >= 60:
        payout = valuation
        pc = 0.5*payout
        pb = 0.1*payout
        pa = (2/30)*payout
        pco = (1/3)*payout
        su = pc + pb + pa + pco
        payouts = [pc, pb, pa, pco, su == valuation]
    if 60 > valuation >= 42:
        payout = valuation - 15
        pc = 15 + 0.5*payout
        pb = 0.1*payout
        pa = (2/30)*payout
        pco = (1/3)*payout
        su = pc + pb + pa + pco
        payouts = [pc, pb, pa, pco, su == valuation]
    return print(payouts)

exit_dist(60)
exit_dist(45)