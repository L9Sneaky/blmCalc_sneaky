import math
from XIVBLM.XIVBLM_py.ppsCalc import FirePps, ThunderPps
casterTax = 0.12


def finalResult2(sps):
    if math.isnan(sps):
        return(['', ''])

    firePps = FirePps(sps, casterTax)
    thunderPps = ThunderPps(sps, casterTax)
    # anyPps = (70 + 390 * sharpAprob + 40 * SpsScalar(sps[i]) *newHRCTimeAny()
    #            /3 +
    #            (newHRCTimeAny()-((3*casterTax+(GcdCalc(2500,sps[i],true)+2*GcdCalc(2500,sps[i],false))3)+((GcdCalc(2500,sps[i],true)+
    #            2*GcdCalc(2500,sps[i],false))/3)*(sharpAprob+1)))*AnyP(sps[i],
    #            casterTax,sharpAprob,noB4))/(newHRCTimeAny())

    return firePps, thunderPps
