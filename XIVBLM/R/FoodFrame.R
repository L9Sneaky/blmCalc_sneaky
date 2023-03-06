FoodFrame<-function(Menu=Menu,minIlvl=0){
  Food<-Menu[which(Menu$Ilvl>=minIlvl),]
  Food$Remove<-NA

  for(i in 1:nrow(Food)){
    Food$Remove[i]<-length(intersect(
      intersect(which(Food$DH>=Food$DH[i]),which(Food$Crit>=Food$Crit[i])),
      intersect(which(Food$Det>=Food$Det[i]),which(Food$SS>=Food$SS[i]))
    ))-1
  }

    Food<-Food[Food$Remove<1,]
    Food$Remove<-NULL
    rownames(Food)<-1:nrow(Food)
  return(Food)
}
