Food.Apply<-function(MateriaFrame,Set,Menu=Food){
  if(Gear_Illegal(MateriaFrame,Set)){return(c(Food='Illegal',
                                              WD=0,
                                              Int=0,
                                              DH=0,
                                              Crit=0,
                                              Det=0,
                                              SS=0,
                                              DPS=0))
                                      }
  BaseStats<-GearStats(MateriaFrame,Set)

  Menu$DPS<-NA
  for(i in 1:nrow(Menu)){
    Menu[i,'DH']<-min(floor(1.1*BaseStats['DH']),BaseStats['DH']+Menu[i,'DH'])
    Menu[i,'Crit']<-min(floor(1.1*BaseStats['Crit']),BaseStats['Crit']+Menu[i,'Crit'])
    Menu[i,'Det']<-min(floor(1.1*BaseStats['Det']),BaseStats['Det']+Menu[i,'Det'])
    Menu[i,'SS']<-min(floor(1.1*BaseStats['SS']),BaseStats['SS']+Menu[i,'SS'])

    Menu[i,'DPS']<-DPS(WD=BaseStats['WD'],Int=BaseStats['Int'],
                        DH=Menu[i,'DH'],Crit=Menu[i,'Crit'],Det=Menu[i,'Det'],SS=Menu[i,'SS'])
    }

  Chef<-min(which(Menu$DPS==max(Menu$DPS)))
  return(c(Food=Menu$Food[Chef],
           BaseStats['WD'],
           BaseStats['Int'],
           DH=Menu$DH[Chef],
           Crit=Menu$Crit[Chef],
           Det=Menu$Det[Chef],
           SS=Menu$SS[Chef],
           DPS=Menu$DPS[Chef]))
}
