.libPaths(c("/home/hp/personal/blmCalc_sneaky/XIVBLM", .libPaths()))
library(XIVBLM)

GearFile<-file.choose()
MateriaFrame<-MateriaFrameGenerate(GearFile)
GearFile<-gsub('.csv','',basename(GearFile))

Food<-FoodFrame(Menu=Menu,minIlvl=max(Menu$Ilvl))

StatWeightChart<-read.csv('Tables\\StatWeightStart.csv')

for(i in 1:nrow(StatWeightChart)){
  Set<-StatWeightGearSet(MateriaFrame,
                         DHWeight = StatWeightChart$InitialDHWeight[i],
                         CritWeight = StatWeightChart$InitialCritWeight[i],
                         DetWeight = StatWeightChart$InitialDetWeight[i],
                         SSWeight = StatWeightChart$InitialSSWeight[i]
                         )

  print(paste(sep="","Running set ",i,"/",nrow(StatWeightChart),":",
              " DH=",StatWeightChart$InitialDHWeight[i],
              " Crit=",StatWeightChart$InitialCritWeight[i],
              " Det=",StatWeightChart$InitialDetWeight[i],
              " SS=",StatWeightChart$InitialSSWeight[i]))

  Set<-BiSLoop(MateriaFrame,Food,Set)

  for(slot in 5:15){
    StatWeightChart[i,slot]<-ItemReturnString(MateriaFrame,Set[slot-4])
  }
  Attributes<-Food.Apply(MateriaFrame,Set,Food)
  for(slot in 16:23){
    StatWeightChart[i,slot]<-Attributes[slot-15]
  }
}

rm(i,slot,Attributes,Set)

StatWeightChart<-StatWeightChart[order(-as.numeric(StatWeightChart$DPS)),]

OutputName<-paste("GearSetOutcomes",GearFile)
#write.csv(StatWeightChart,paste(OutputName,' (Debug).csv',sep=''),row.names = FALSE)
write.csv(StatWeightChart[!(duplicated(StatWeightChart[,17:23])),c(5:23)],paste(OutputName,'.csv',sep=''),row.names = FALSE)
rm(OutputName,GearFile)
