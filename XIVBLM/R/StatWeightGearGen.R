StatWeightGearSet<-function(MateriaFrame,DHWeight=runif(1),
                                        CritWeight=runif(1),
                                        DetWeight=runif(1),
                                        SSWeight=runif(1)){

  Slots<-unique(MateriaFrame$Slot)
  Set<-character()
  for(slot in Slots){
    Items<-MateriaFrame[which(MateriaFrame$Slot==slot),]
    Items$Weights<-DHWeight*Items$DH+CritWeight*Items$Crit+DetWeight*Items$Det+SSWeight*Items$SS
    Weight_Max<-max(Items$Weights)
    Set<-c(Set,rownames(Items)[min(which(Items$Weights==Weight_Max))])
    }

Set<-as.numeric(Set)
Slots<-Slots[1:(length(Slots)-1)]
Slots<-c(Slots,'Finger1')
names(Set)<-Slots

  if(MateriaFrame$Unique[Set['Finger1']]){
    Items<-Items[-which(Items$Name==MateriaFrame$Name[Set['Finger1']]),]
    }
  Weight_Max<-max(Items$Weights)
  Set<-c(Set,as.numeric(rownames(Items)[min(which(Items$Weights==Weight_Max))]))
  names(Set)[length(Set)]='Finger2'
rm(Items,CritWeight,DetWeight,DHWeight,slot,Slots,SSWeight,Weight_Max)
return(Set)
}

