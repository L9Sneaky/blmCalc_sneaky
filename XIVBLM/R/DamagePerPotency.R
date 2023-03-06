DamagePerPotency<-function(WD=111,Int=447){
  return((1/100)*floor((WD+floor(390*115/1000)))*(floor(100+(Int-390)*195/390)/100))
}
