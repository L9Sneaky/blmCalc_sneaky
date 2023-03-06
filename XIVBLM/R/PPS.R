PPS <- function(SS=400,Crit=400) {
  Tier<-which.max(PPSTable$SpS>SS[1])-1
  return(PPSTable$PPS[Tier])
}
