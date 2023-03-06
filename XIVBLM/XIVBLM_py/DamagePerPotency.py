def damage_per_potency(WD=111, Int=447):
    return (1/100) * (WD + (390*115/1000)) * ((100 + (Int - 390)*195/390)/100)
