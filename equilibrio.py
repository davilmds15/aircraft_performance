import parametros
from modelo_ambiental import ISA
import numpy as np
from dinamica_translacao import dinamica_translacao
from controles import controles_planeio
from scipy.optimize import fsolve
from aerodinamica import modelo_aerodinamico_planeio

def obj_eq_planeio(x,*dados):
    He, alfaf, m, g=dados
    Ve=x[0];gamae=x[1]
    CLe,Fe,phie,Y=controles_planeio()
    _,_,rhoe,_,_,_=ISA(He,0)
    Le,De,alfe,Y=modelo_aerodinamico_planeio(CLe, Ve, rhoe)
    
    Xe = np.array([Ve,gamae,0,0,0,He])
    U  = np.array([CLe,Fe,phie,Y])
    Xp = dinamica_translacao(0,Xe,U)
    der= np.array([Xp[0],Xp[1]])
    return der

def equilibrio_planeio(H):
    m=parametros.M;g=parametros.G;CD0=parametros.CD0;alfaf=parametros.ALFAF
    k=parametros.K;S=parametros.S;He=parametros.H0
    dados = (He, alfaf, m, g)
    _,_,rho,_,_,_=ISA(He,0)
    CLas=np.sqrt(CD0/k) # CL*
    Vas = np.sqrt(2*m*g/(rho*S*CLas))
    x0=np.array([Vas,0])
    res = fsolve(obj_eq_planeio,x0,args=dados)
    Xe=np.array([res[0],res[1],0,0,0,H])
    return Xe
