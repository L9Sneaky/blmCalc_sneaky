GearDPS<-function(MateriaFrame,GearSet){
  Stats<-GearStats(MateriaFrame,GearSet)
  if(Gear_Illegal(MateriaFrame,GearSet)){return(0)}
  return(as.numeric(DPS(WD=Stats['WD'],
                        Int=Stats['Int'],
                        DH=Stats['DH'],
                        Crit=Stats['Crit'],
                        Det=Stats['Det'],
                        SS=Stats['SS'])))
}

