import math

# Potencies for our spells
fastF3B3 = 182
B4 = 310
Xeno = 880
F3P = 1.8 * 260
F4 = 1.8 * 310
Desp = 1.8 * 340
Para = 500
T3 = 50
F4Rotation = fastF3B3 * 2 + B4 + Para * 2 + F4 * 6 + Desp

def xenoValue(rotationLength):
    return Xeno * (rotationLength / 30)

def xenoTime(sps, rotationLength):
    return GcdCalc(2500, sps, False) * (rotationLength / 30)

# Scale Manafont since our cycles are longer than 120s
def mfValue(rotationLength):
    return (F4 + Desp) * (rotationLength / 120)

def mfTime(sps, rotationLength, casterTax):
    return (GcdCalc(2800, sps, False) + GcdCalc(3000, sps, False) * 120 / ((30 / 0.85) + 90) + 2 * casterTax) * (rotationLength / 120)

def amplyValue(rotationLength):
    return Xeno * (rotationLength / 120)

def amplyTime(sps, rotationLength):
    return GcdCalc(2500, sps, False) * 120 / ((30 / 0.85) + 90) * (rotationLength / 120)

def thunderTime(sps, casterTax, rotationLength, tprocNum):
    return (GcdCalc(2500, sps, False) * 120 / ((30 / 0.85) + 90) + (1 - tprocNum) * casterTax) * (rotationLength / 30)

def thunderValue(sps, rotationLength, tprocNum):
    return (T3 + 10 * SpsScalar(sps) * 35 + tprocNum * 350) * (rotationLength / 30)

def instaCasts(sps, rotationLength, casterTax):
    return 4 * ((GcdCalc(2500, sps, False) - GcdCalc(2800, sps, False)) * 120 / ((30 / 0.85) + 90) - casterTax) * (rotationLength / 60)

# Average potency of a 2min fire rotation with X fire procs
def GetThunderP(fprocNum, XenoP, MfP, AmplyX, thunderP):
    result = 0
    result += 4 * (F4Rotation + fprocNum * fastF3B3) + XenoP + MfP + AmplyX + thunderP
    return result

# Actual time taken by a 2min fire rotation with X fire procs
def getCycle(sps, casterTax = 0.12):
    shortGcd = GcdCalc(2500, sps, False)
    longGcd = GcdCalc(2800, sps, False)
    despGcd = GcdCalc(3000, sps, False)
    result = 0
    fastB3F3Clips = max((70 - max(100 * GcdCalc(2500, sps, False), 150) + math.floor(100 * 0.5 * GcdCalc(3500, sps, False))), 0) / 100
    fastB3F3ClipsLL = max((70 - max(100 * GcdCalc(2500, sps, True), 150) + math.floor(100 * 0.5 * GcdCalc(3500, sps, True))), 0) / 100
    result += 20 * shortGcd + 24 * longGcd + 4 * despGcd
    result *= 120 / ((30 / 0.85) + 90)
    result += 1 * fastB3F3Clips + 1 * fastB3F3ClipsLL + 36 * casterTax
    return result

def FirePps(sps, casterTax = 0.12):
    fprocNum = 1
    tprocNum = (1 - math.pow(0.9, 10))

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

    potency = GetThunderP(fprocNum, xenoP, mfP, amplyP, thunderP) / (cycle + mfT + xenoT + amplyT + instas + thunderT)
    return potency

def ThunderPps(sps, casterTax = 0.12):
    fprocNum = 0.4
    tprocNum = 1

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

    potency = GetThunderP(fprocNum, xenoP, mfP, amplyP, thunderP) / (cycle + mfT + xenoT + amplyT + instas + thunderT)
    return potency

# Returns the probability of getting X F3P procs naturally
# def probFunction(numberOfProcs, numberOfDowngrades, anyFlag):
#     (anyFlag ? givenF1s : 0)
#     if anyFlag:
#         idk = givenF1s
#     else:
#         idk = 0
#     prob = math.pow(2 / 5, numberOfProcs) * math.pow(3 / 5, (totalF1s - numberOfProcs - idk + numberOfDowngrades))
#     return prob

def SpsScalar(SpS):
    S = ((1000 + math.floor(130 * (SpS - 400) / 1900)) / 1000)
    return S

def reduce(arr, callback, initialVal):
    accumulator = initialVal if initialVal is not None else None
    for i in range(len(arr)):
        if accumulator is not None:
            accumulator = callback(accumulator, arr[i], i, None)
        else:
            accumulator = arr[i]
    return accumulator

# Gives an array back of Pascal's triangle
def pasc(n):
    result = []
    result.append([1])
    result.append([1, 1])
    for row in range(2, n):
        result.append([1])
        for col in range(1, row - 1):
            result[row][col] = result[row - 1][col] + result[row - 1][col - 1]
            result[row].append(1)
    return result

def GcdCalc(gcd, sps, llFlag):
    if llFlag:
        ll = 85
    else:
        ll = 100
    time = math.floor(math.floor(1000 * ll * (math.floor(gcd * (1000 - math.floor(130 * (sps - 400) / 1900)) / 1000) / 1000)) / 1000) / 100
    return time
