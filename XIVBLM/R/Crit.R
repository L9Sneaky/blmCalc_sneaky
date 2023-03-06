CritRate<-function(Crit=400){
  return(floor((200*(Crit-400)/1900+50))/1000)
}

CritBonus<-function(Crit=400){
  return(floor(200*(Crit-400)/1900+400)/1000)
}

Crit_DPS<-function(Crit=400){
  return(1+CritRate(Crit)*CritBonus(Crit))
}
