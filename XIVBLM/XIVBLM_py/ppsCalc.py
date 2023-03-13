import math as Math
# potencies for our spells
fastF3B3 = 182
B4 = 310
Xeno = 760
F3P = 1.8*260
F4 = 1.8*310
Desp = 1.8*340
Para = 500
T3 = 50
F4Rotation = fastF3B3 * 2 + B4 + Para * 2 + F4 * 6 + Desp


def xenoValue(rotationLength):
    return Xeno * (rotationLength/30)


def xenoTime(sps, rotationLength):
    return GcdCalc(2500, sps, False) * (rotationLength/30)


# scale Manafont since our cycles are longer than 120s
def mfValue(rotationLength):
    return (F4+Desp)*(rotationLength/120)


def mfTime(sps, rotationLength, casterTax):
    return (GcdCalc(2800, sps, False)+GcdCalc(3000, sps, False)*120/((30/0.85)+90)+2*casterTax)*(rotationLength/120)


def amplyValue(rotationLength):
    return Xeno * (rotationLength/120)


def amplyTime(sps, rotationLength):
    return GcdCalc(2500, sps, False)*120/((30/0.85)+90) * (rotationLength/120)


def thunderTime(sps, casterTax, rotationLength, tprocNum):
    return (GcdCalc(2500, sps, False)*120/((30/0.85)+90) + (1-tprocNum)*casterTax) * (rotationLength/30)


def thunderValue(sps, rotationLength, tprocNum):
    return (T3 + 10*SpsScalar(sps)*35 + tprocNum * 350)*(rotationLength/30)


def instaCasts(sps, rotationLength, casterTax):
    return 4*((GcdCalc(2500, sps, False) - GcdCalc(2800, sps, False))*120/((30/0.85)+90) - casterTax) * (rotationLength/60)


# Average potency of a 2min fire rotation with X fire procs
def GetThunderP(fprocNum, XenoP, MfP, AmplyX, thunderP):
    result = 0
    result += 4 * (F4Rotation + fprocNum * fastF3B3) + XenoP + MfP + AmplyX + thunderP
    return result


# Actual time taken by a 2min fire rotation with X fire procs
def getCycle(sps, casterTax):
    shortGcd = GcdCalc(2500, sps, False)
    longGcd = GcdCalc(2800, sps, False)
    despGcd = GcdCalc(3000, sps, False)
    result = 0
    fastB3F3Clips = max((70 - max(100*GcdCalc(2500, sps, False), 150) + Math.floor(100*0.5*GcdCalc(3500, sps, False))),0)/100
    fastB3F3ClipsLL = max((70 - max(100*GcdCalc(2500, sps, True), 150) + Math.floor(100*0.5*GcdCalc(3500, sps, True))),0)/100
    # short gcds = 4 * (5 B4, 2* Para, 2* fastcast)
    # long gcds = 4 * 6 F4s
    # caster tax = 4 * (9 b4, para, 6F4 despair)
    result += 20 * shortGcd + 24 * longGcd + 4 * despGcd
    # LL normalized to 120s. Making it a multiplier instead of static uptime makes it scale with a cycle
    result *= 120/((30/0.85)+90)
    result += 1*fastB3F3Clips + 1*fastB3F3ClipsLL + 36 * casterTax
    return result


def FirePps(sps, casterTax = 0.12):
    #  sps = 1411
    #  casterTax = 0.12
    
    fprocNum = 1
    tprocNum = (1 - Math.pow(0.9,10))

    cycle = getCycle(sps, casterTax)
    xenoT = xenoTime(sps, cycle)
    xenoP = xenoValue(cycle)
    mfP = mfValue(cycle)
    mfT = mfTime(sps, cycle, casterTax)
    amplyT = amplyTime(sps, cycle)
    amplyP = amplyValue(cycle)
    instas = instaCasts(sps, cycle, casterTax)
    thunderT = thunderTime(sps, casterTax, cycle, tprocNum)
    thunderP = thunderValue(sps, cycle, tprocNum)

    potency = 0
    potency = GetThunderP(fprocNum, xenoP, mfP, amplyP, thunderP)/(cycle+mfT+xenoT + amplyT + instas + thunderT)
    return potency


def oldThunderPps(sps, casterTax):
    tprocNum = 1

    cycle = getCycle(sps, casterTax)
    fprocNum = 0.4
    xenoT = xenoTime(sps, cycle)
    xenoP = xenoValue(cycle)
    mfP = mfValue(cycle)
    mfT = mfTime(sps, cycle, casterTax)
    amplyT = amplyTime(sps, cycle)
    amplyP = amplyValue(cycle)
    instas = instaCasts(sps, cycle, casterTax)
    thunderT = thunderTime(sps, casterTax, cycle, tprocNum)
    thunderP = thunderValue(sps, cycle, tprocNum)

    potency = 0
    potency = GetThunderP(fprocNum, xenoP, mfP, amplyP, thunderP)/(cycle+mfT+xenoT + amplyT + instas + thunderT)
    return potency


# def SpsScalar(SpS):
#     S = ((1000+Math.floor(130*(SpS-400)/1900))/1000)
#     return S

# gives an array back of Pascal's triangle
def pasc(n):
    result = []
    result[0] = [1]
    result[1] = [1,1]
    for row in range(2, n):
        result[row] = [1]
        for col in range(1, row):
            result[row][col] = result[row-1][col] + result[row-1][col-1]
            result[row].push(1)
    return result


# def GcdCalc(gcd, sps, llFlag):
#     time = Math.floor(Math.floor(1000 * (85 if llFlag else 100) * (Math.floor(gcd * (1000 - Math.floor(130 * (sps-400) / 1900))/1000) / 1000)) / 1000)/100
#     return time



# Developed from Furst's BLM PPS Model. Main idea: it takes 30-2gcd time of ice/fire spells to generate t3 and xeno,
#  since using them takes the total to 30s.
# Every 120 actual seconds we have used:
    # mf = 1longGcd + 1despGcd + 2 casterTax
    # 4 xeno + amplify = 5 shortGcd
    # 4 thunder = 4 shortgcd + 4 (1-tprocNum)* casterTax
    # leylines and 8 instant casts
#  which means it takes ((30/0.85 + 90) + 8*instantGain - 1longGcd - 9 shortGcd - 1 despGcd - (6 - 4 tProcNum) casterTax) of base (ice/fire) rotation to generate all this and spend 120 actual seconds

def ThunderPps(sps):
    casterTax = 0.12  # 0.1 + 2/fps
    fastF3B3 = 182
    B4 = 310
    Xeno = 800
    F3P = 1.8 * 260
    F4 = 1.8 * 310
    Desp = 1.8 * 340
    Para = 500
    T3 = 50
    F4Rotation = fastF3B3 * 2 + B4 + Para * 2 + F4 * 6 + Desp

    fProcNum = 0.4
    tProcNum = 1

    shortGcd = GcdCalc(2500, sps, False)
    longGcd = GcdCalc(2800, sps, False)
    despGcd = GcdCalc(3000, sps, False)
    instantGain8 = (3*(despGcd+casterTax-shortGcd) + 5*(longGcd+casterTax-shortGcd)) # say, 3 despairs 5 f4s being instant

    fastB3F3Clips = max((70 - max(100*GcdCalc(2500,sps, False),150) + Math.floor(100*0.5*GcdCalc(3500, sps, False))),0)/100
    fastB3F3ClipsLL = max((70 - max(100*GcdCalc(2500,sps, True),150) + Math.floor(100*0.5*GcdCalc(3500, sps, True))),0)/100
    # short gcds = 4 * (5; B4, 2* Para, 2* fastcast)
    # long gcds = 4 * 6 F4s
    # caster tax = 4 * (9; b4, para, 6F4 despair)
    baseTime = 20 * shortGcd + 24 * longGcd + 4 * despGcd  # why are we doing 4 loops? vestigial, it doesn't matter.
    baseTime += 1*fastB3F3Clips + 1*fastB3F3ClipsLL  + 36 * casterTax

    cycleTime = ((30/0.85 + 90) + instantGain8 - 1*longGcd - 9*shortGcd - 1*despGcd - (6 - 4*tProcNum)*casterTax)  # time of base (ice/fire) rotation to do an actual 120s cycle
    nCycles = baseTime/cycleTime  # how many 120s cycles we actually did
    xenoP = nCycles*5*Xeno
    mfP = nCycles*(F4 + Desp)
    thunderP = nCycles*4*(T3 + 10*SpsScalar(sps)*35 + tProcNum * 350)  # T3p is not affected by sps scalar

    potency = 4 * (F4Rotation +  fProcNum * fastF3B3) + xenoP + mfP + thunderP
    time = nCycles*120 
    return potency/time

def SpsScalar(sps):
    S = (1000 + ((sps - 400) * 130 // 1900)) // 1000 + 0.1
    return S

def GcdCalc(gcd, sps, ll_flag):
    time = (gcd * (1000 - (SpsScalar(sps) - 0.1) * 130) // 1000) * (85 if ll_flag else 100) // 1000
    return time
