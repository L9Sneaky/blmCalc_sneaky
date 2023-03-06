GearStats<-function(MateriaFrame,GearSet){
  GearSetFrame<-GearSetFrameGen(MateriaFrame,GearSet)[,c('WD','Int','DH','Crit','Det','SS')]
  GearSetFrame$WD<-as.numeric(GearSetFrame$WD)
  GearSetFrame$Int<-as.numeric(GearSetFrame$Int)
  GearSetFrame$DH<-as.numeric(GearSetFrame$DH)
  GearSetFrame$Crit<-as.numeric(GearSetFrame$Crit)
  GearSetFrame$Det<-as.numeric(GearSetFrame$Det)
  GearSetFrame$SS<-as.numeric(GearSetFrame$SS)
  return(colSums(GearSetFrame))
}

