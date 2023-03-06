DPS<-function(WD,Int,DH,Crit,Det,SS){
  SelfEsteem<-floor(100*PPS(SS)*DamagePerPotency(WD,floor(Int*1.05)))
  SelfEsteem<-floor(SelfEsteem*Det_DPS(Det)/100)
  SelfEsteem<-floor(1.3*SelfEsteem)
  SelfEsteem<-floor(1.2*SelfEsteem)
  return(SelfEsteem*DH_DPS(DH)*Crit_DPS(Crit))
}
