import json,os,urllib.request as u
_Z=[i*2654435761 for i in range(1561)];ZP=_Z[:1536];ZS=_Z[1536];ZC=_Z[1537:1553];ZE=_Z[1553:]
M=120000;X=128;H=136;J=1<<17;K=J*2;V=[0,100,320,330,500,900,0];N=[15]*128;N[0]=13;N[4]=12;N[7]=14;N[112]=7;N[116]=3;N[119]=11
KN=[33,31,18,14,-14,-18,-31,-33];RI=[1,-1,16,-16];BI=[15,17,-15,-17];KI=RI+BI;D=[0,0,KN,BI,RI,KI,KI]
def _p():
 PM=[[0]*128 for _ in range(7)];E6=[0]*128;a=[0,0,4,8,14,24,40,0]
 for r in range(8):
  for f in range(8):
   s=r*16+f;k=min(f,7-f)+min(r,7-r);d=f in(3,4)
   PM[1][s]=100+a[r]+5*min(r-1,7-r)*(r>2)*d;PM[2][s]=310+6*k;PM[3][s]=322+4*k;PM[4][s]=500+15*(r==6)+5*(r==0 and d);PM[5][s]=894+2*k;PM[6][s]=[20,25,10,0,0,10,25,20][f] if r==0 else-min(50,15*r);E6[s]=8*k-24
 return PM,PM[:6]+[E6]
PM,PE=_p()
def U(m):
 p=m>>14&7
 return chr(97+(m&7))+chr(49+(m>>4&7))+chr(97+(m>>7&7))+chr(49+(m>>11&7))+("nbrq"[p-2]if p else"")
BK=['0,01*(BB(0:/#(-=>>019;8$F7%=5&<%K0>#C$H#A%8#F#8#<','.*5(#?5.3*-I,/0(#*;61C&;F;>#6$;9A#-?%&C&W:O$B9S09<:0I#F#F&-$N#L6@#J$*$5%E#4$B#2$B$&+1',"..:6.10;712C#:3/$41>A9@.7*0@+%H,-<1#'4P#W,?7C#-+($:$2-6$>",",,#@(503@,')/#;/*D/A1@#PA7E)I4F>6%;#A'$9M'.-A$#8D$$-,#G$M#1"]
class B:
 def __init__(self):self.f()
 def f(self):
  self.b=[0]*128;self.sd=self.hf=self.mg=self.eg=self.np=self.hh=0;self.ep=-1;self.kg=[4,116];self.ud=[]
  for i,p in enumerate((4,2,3,5,6,3,2,4)):
   self.b[i]=p;self.a(p,i);self.b[112+i]=-p;self.a(-p,112+i);self.b[16+i]=1;self.a(1,16+i);self.b[96+i]=-1;self.a(-1,96+i)
  self.ct=15;self.hh^=ZC[15];self.hist=[self.hh]
 def a(self,pc,sq,s=1):
  t=abs(pc);q=sq^112*(pc<0);w=1-2*(pc<0)
  self.mg+=s*w*PM[t][q];self.eg+=s*w*PE[t][q];self.hh^=ZP[(t-1+6*(pc<0))*128+sq]
  if t!=1:self.np+=s*V[t]
 def A(self,sq,by):
  b=self.b;v=1-by*2
  for d in(15,17):
   t=sq-d*v
   if not t&H and b[t]==v:return 1
  for D,P in((KN,2),(KI,6)):
   for d in D:
    t=sq+d
    if not t&H and b[t]==P*v:return 1
  for D,P in((BI,3),(RI,4)):
   for d in D:
    t=sq+d
    while not t&H:
     pc=b[t]
     if pc:
      if pc==P*v or pc==5*v:return 1
      break
     t+=d
  return 0
 def c(self):return self.A(self.kg[self.sd],self.sd^1)
 def g(self,co=0):
  b=self.b;us=self.sd;o=[]
  for fr in range(128):
   if fr&H:continue
   pc=b[fr]
   if not pc or(pc>0)!=(us==0):continue
   t=abs(pc)
   if t==1:
    fwd=16-32*us;rank=fr>>4;last=6-5*us;one=fr+fwd
    if b[one]==0:
     if rank==last:
      for pr in(5,4,3,2):o.append(fr|one<<7|pr<<14)
     elif not co:
      o.append(fr|one<<7)
      if rank==1+5*us:
       two=one+fwd
       if b[two]==0:o.append(fr|two<<7|K*4)
    for d in(fwd-1,fwd+1):
     to=fr+d
     if to&H:continue
     tg=b[to]
     if tg and(tg>0)!=(us==0):
      if rank==last:
       for pr in(5,4,3,2):o.append(fr|to<<7|pr<<14|J)
      else:o.append(fr|to<<7|J)
     elif to==self.ep:o.append(fr|to<<7|J|K)
    continue
   st=D[t];sl=2<t<6
   for d in st:
    to=fr+d
    while not to&H:
     tg=b[to]
     if tg==0:
      if not co:o.append(fr|to<<7)
     else:
      if(tg>0)!=(us==0):o.append(fr|to<<7|J)
      break
     if not sl:break
     to+=d
   if t==6 and not co:self.C(o)
  return o
 def C(self,o):
  us=self.sd;k=112*us+4
  if self.kg[us]!=k or self.A(k,us^1):return
  b=self.b;kr=1+3*us
  if self.ct&kr and b[k+1]==0 and b[k+2]==0 and not self.A(k+1,us^1) and not self.A(k+2,us^1):o.append(k|(k+2)<<7|K*2)
  if self.ct&kr*2 and b[k-1]==0 and b[k-2]==0 and b[k-3]==0 and not self.A(k-1,us^1) and not self.A(k-2,us^1):o.append(k|(k-2)<<7|K*2)
 def m(self,m):
  b=self.b;fr=m&127;to=m>>7&127;pc=b[fr];us=self.sd;t=abs(pc)
  cs=to+32*us-16 if m&K else to;cp=b[cs]
  self.ud.append((m,cp,self.ct,self.ep,self.hf,self.hh,self.mg,self.eg,self.np))
  if cp:self.a(cp,cs,-1);b[cs]=0
  self.a(pc,fr,-1);b[fr]=0;pr=m>>14&7;pl=(pr or t)*(1-2*us);b[to]=pl;self.a(pl,to)
  if t==6:self.kg[us]=to
  if m&K*2:
   rf,rt=(fr+3,fr+1)if to>fr else(fr-4,fr-1);rk=b[rf];self.a(rk,rf,-1);b[rf]=0;b[rt]=rk;self.a(rk,rt)
  self.hh^=ZC[self.ct];self.ct&=N[fr]&N[to];self.hh^=ZC[self.ct]
  if self.ep>=0:self.hh^=ZE[self.ep&7]
  self.ep=-1
  if m&K*4:
   es=(fr+to)>>1;ew=2*us-1
   if(not(to-1)&H and b[to-1]==ew)or(not(to+1)&H and b[to+1]==ew):self.ep=es;self.hh^=ZE[es&7]
  self.hf=0 if t==1 or cp else self.hf+1;self.sd^=1;self.hh^=ZS;self.hist.append(self.hh)
  if self.A(self.kg[us],us^1):self.u();return 0
  return 1
 def u(self):
  m,cp,ca,ep,ha,h,mg,eg,np=self.ud.pop();b=self.b;fr=m&127;to=m>>7&127;self.sd^=1;us=self.sd
  if m&K*2:
   rf,rt=(fr+3,fr+1)if to>fr else(fr-4,fr-1);b[rf]=b[rt];b[rt]=0
  pl=b[to];b[to]=0;b[fr]=(1-2*us) if m>>14&7 else pl
  if b[fr]in(6,-6):self.kg[us]=fr
  cs=to+32*us-16 if m&K else to
  if cp:b[cs]=cp
  self.ct=ca;self.ep=ep;self.hf=ha;self.hh=h;self.mg=mg;self.eg=eg;self.np=np;self.hist.pop()
 def e(self):
  ph=self.np;s=(self.mg*ph+self.eg*(6400-ph))//6400
  return s*(1-2*self.sd)+10
 def l(self):
  return [m for m in self.g() if self.m(m) and self.u() is None]
 def r(self):
  h=self.hist
  for i in range(len(h)-3,-1,-2):
   if h[i]==self.hh:return 1
  return 0
class E:
 def __init__(self,b):
  self.p=b;self.nodes=0;self.limit=9e8;self.aborted=0;self.tt={};self.kill=[[0,0]for _ in range(X)]
 def o(self,mv,pl,tm):
  p=self.p;b=p.b;sc=[];k0,k1=self.kill[pl]
  for i,m in enumerate(mv):
   s=0
   if m&(J):
    vt=abs(b[m>>7&127])or 1;s=M+10*V[vt]-abs(b[m&127])
   pr=m>>14&7
   if pr:s+=2*M+V[pr]
   elif m==k0:s=50000
   elif m==k1:s=40000
   if m==tm:s=10*M
   sc.append((s-i,m))
  sc.sort(reverse=True);return[m for _,m in sc]
 def q(self,al,be,pl):
  self.nodes+=1
  if self.nodes>=self.limit:self.aborted=1;return 0
  p=self.p
  if pl>=X:return p.e()
  ch=p.c();be2=-M-1
  if not ch:
   st=p.e()
   if st>=be:return st
   be2=st
   al=max(al,st)
  mv=self.o(p.g(not ch),pl,0);le=0
  for m in mv:
   if not p.m(m):continue
   le+=1;s=-self.q(-be,-al,pl+1);p.u()
   if self.aborted:return 0
   if s>be2:be2=s
   al=max(al,s)
   if s>=be:return s
  if ch and le==0:return -M+pl
  return be2
 def s(self,d,al,be,pl):
  p=self.p
  if pl>0 and(p.hf>=100 or p.r()):return 0
  if d<=0 or pl>=X:return self.q(al,be,pl)
  self.nodes+=1
  if self.nodes>=self.limit:self.aborted=1;return 0
  h=p.hh;e=self.tt.get(h);tm=e[2]if e else 0
  if e:
   s=e[1];s+=pl*((s<-M+X)-(s>M-X))
   if e[0]>=d:
    if e[3]==0:return s
    if e[3]==1:al=max(al,s)
    elif e[3]==2:be=min(be,s)
    if al>=be:return s
  if d>2 and be<M-X and p.np>899 and p.e()>=be and not p.c():
   e0,g0=p.ep,p.hh
   if p.ep>=0:p.hh^=ZE[p.ep&7]
   p.ep=-1;p.sd^=1;p.hh^=ZS
   s=-self.s(d-3,-be,-be+1,pl+1)
   p.ep,p.hh=e0,g0;p.sd^=1
   if self.aborted:return 0
   if s>=be:return be
  ch=p.c();d+=ch*(d>1)
  a0=al;mv=self.o(p.g(),pl,tm);be2=-M-1;le=0
  for m in mv:
   if not p.m(m):continue
   le+=1;r=d-2 if d>2 and le>2 and not ch and not(m&J or m>>14&7) and not p.c() else d-1
   s=-self.s(r,-be,-al,pl+1)
   if r<d-1 and s>al and not self.aborted:s=-self.s(d-1,-be,-al,pl+1)
   p.u()
   if self.aborted:return 0
   if s>be2:be2=s;bm=m
   al=max(al,s)
   if al>=be:
    if not(m&J or m>>14&7):
     k=self.kill[pl]
     if k[0]!=m:k[1]=k[0];k[0]=m
    break
  if le==0:return -M+pl if ch else 0
  s=be2;s+=pl*((s<-M+X)-(s>M-X))
  self.tt[h]=(d,s,bm,(be2>=be)+2*(be2<=a0))
  return be2
 def R(self,bd):
  p=self.p;mv=p.l()
  if not mv:return None
  pl=len(p.hist)-1
  for L in BK:
   if 7<pl<len(L):
    b=B();ok=1
    for i in range(pl):
     lm=b.l();ix=ord(L[i])-35
     if ix>=len(lm) or not b.m(lm[ix]):ok=0;break
    if ok and b.hh==p.hh:
     ix=ord(L[pl])-35
     if ix<len(mv):return mv[ix]
  o=[(0,m)for m in mv]
  for d in range(1,65):
   self.aborted=0;al=-M-1
   if d>1:self.limit=bd
   for i,(_,m) in enumerate(o):
    p.m(m);s=-self.s(d-1,-M-1,-al,1);p.u()
    if self.aborted:break
    o[i]=(s,m)
    al=max(al,s)
   if self.aborted:break
   o.sort(key=lambda x:-x[0]);be=o[0][1]
   if o[0][0]>=M-X:break
  return be
def T(pa,bo):return json.load(u.urlopen(os.getenv("MAKEFUN_ENV_URL")+pa,json.dumps(bo).encode()))
def Y(b,g,ap):
 while ap<len(g["moves"]):
  mm=next((m for m in b.l()if U(m)==g["moves"][ap]),None)
  if mm is None:exit(1)
  b.m(mm);ap+=1
 return ap
def main():
 b=B();cg=0;ap=0
 while 1:
  g=T("/game",{})
  if g["status"]=="done":break
  if g["game"]!=cg:
   cg=g["game"];b.f();ap=0;en=E(b)
  ap=Y(b,g,ap)
  while g["status"]=="your_move":
   en.nodes=0;be=en.R(M)
   if be is None:exit(1)
   uc=U(be);b.m(be);ap+=1;g=T("/move",{"game":g["game"],"move":uc})
   ap=Y(b,g,ap)
if __name__=="__main__":main()
