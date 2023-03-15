import numpy as np

def SpsScalar(SpS):
    S = ((1000+ np.floor(130*(SpS-400)/1900))/1000)
    return S

# def finalResult2(sps):
#     casterTax = 0.12
#     firePps = FirePps(sps, casterTax)
#     thunderPps = ThunderPps(sps, casterTax)
#     # anyPps = (70 + 390 * sharpAprob + 40 * SpsScalar(sps[i]) * newHRCTimeAny()/3 + (newHRCTimeAny()-((3*casterTax+(GcdCalc(2500,sps[i],True)+2*GcdCalc(2500,sps[i],False))/3)+((GcdCalc(2500,sps[i],True)+2*GcdCalc(2500,sps[i],False))/3)*(sharpAprob+1)))*AnyP(sps[i], casterTax,sharpAprob,noB4))/(newHRCTimeAny())
#     return firePps, thunderPps

def new_BLM_thunder_pps(sps):
    caster_tax = 0.12 # 0.1 + 2/fps
    fast_f3_b3 = 182
    B4 = 310
    Xeno = 800
    F3P = 1.8 * 260
    F4 = 1.8 * 310
    Desp = 1.8 * 340
    Para = 500
    T3 = 50
    F4_rotation = fast_f3_b3 * 2 + B4 + Para * 2 + F4 * 6 + Desp
    f_proc_num = 0.4
    t_proc_num = 1

    # getCycel start
    short_gcd = GcdCalc(2500, sps, False)
    long_gcd = GcdCalc(2800, sps, False)
    desp_gcd = GcdCalc(3000, sps, False)
    instant_gain_8 = (3 * (desp_gcd + caster_tax - short_gcd) + 5 * (long_gcd + caster_tax - short_gcd))  # say, 3 despairs 5 f4s being instant

    fast_b3_f3_clips = max((70 - max(100 * GcdCalc(2500, sps, False), 150) + np.floor(100 * 0.5 * GcdCalc(3500, sps, False))), 0) / 100
    fast_b3_f3_clips_ll = max((70 - max(100 * GcdCalc(2500, sps, True), 150) + np.floor(100 * 0.5 * GcdCalc(3500, sps, True))), 0) / 100
    # short gcds = 4 * (5; B4, 2* Para, 2* fastcast)
    # long gcds = 4 * 6 F4s
    # caster tax = 4 * (9; b4, para, 6F4 despair)
    base_time = 20 * short_gcd + 24 * long_gcd + 4 * desp_gcd  # why are we doing 4 loops? vestigial, it doesn't matter.
    base_time += 1 * fast_b3_f3_clips + 1 * fast_b3_f3_clips_ll + 36 * caster_tax
    cycle_time = ((30 / 0.85 + 90) + instant_gain_8 - 1 * long_gcd - 9 * short_gcd - 1 * desp_gcd - (6 - 4 * t_proc_num) * caster_tax)  # time of base (ice/fire) rotation to do an actual 120s cycle
    
    n_cycles = base_time / cycle_time  # how many 120s cycles we actually did
    xeno_p = n_cycles * 5 * Xeno
    mf_p = n_cycles * (F4 + Desp)
    thunder_p = n_cycles * 4 * (T3 + 10 * SpsScalar(sps) * 35 + t_proc_num * 350)  # T3p is not affected by sps scalar

    potency = 4 * (F4_rotation + f_proc_num * fast_f3_b3) + xeno_p + mf_p + thunder_p
    time = n_cycles * 120
    return potency / time

def GcdCalc(gcd, sps, llFlag):
    time = round(1000 * (85 if llFlag else 100) * (gcd * (1000 - np.floor(130 * (sps - 400) / 1900)) / 1000) / 1000) / 100
    return time