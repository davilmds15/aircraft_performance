import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import datetime
import sys
from equilibrio import equilibrio_planeio
import parametros
from modelo_ambiental import ISA
from modelos_dinamicos_desempenho import simula_planeio

g = 9.80665;

alfaf =0
CLa   =5
CL0   =0

av = int(input("Digite a opção de avião (1) Planador generico (2) Jato Executivo: "))
if av==1:
    CD0 =0.017
    k   = 0.021
    m   = 840*0.453592
    S   = 102*0.3048**2
else:
    CD0 = 0.0245
    k   = 0.0765
    m   = 13000*0.453592
    S   = 225*0.3048**2

print('Dados da Aeronave:');
print('CD0: ',CD0);
print('k: ',k);
print('m (Kg): ',m);
print('S (m**2): ',S);

pl = int(input("Escolha a opção de CL (1) Máximo Alcance (2) Máxima Autonomia (3) CL qualquer: "))
if pl==1:
    CL = np.sqrt(CD0/k);
    print("CL de máximo alcance: ",CL)
elif pl==2:
    CL = np.sqrt(3*CD0/k);
    print("CL de máxima autonomia: ",CL)
else:
    CL=0.5
    print("CL qualquer: ",CL)

H0 = float(input("Digite a altitude inicial (m): "))

parametros.G=g
parametros.CD0=CD0
parametros.K=k
parametros.M=m
parametros.S=S
parametros.ALFAF=alfaf
parametros.CLA=CLa
parametros.CL0=CL0
parametros.H0=H0
parametros.CL=CL

TF = float(input("Digite a duração da simulação (s): "))

Xe = equilibrio_planeio(H0);
print("Condição de equilíbrio")
print("Velocidade (m/s): ",Xe[0])
print("Ângulo de Trajetória (graus): ",Xe[1]*180/np.pi)
print("Ângulo de Guinada (graus): ",Xe[2]*180/np.pi)
print("Posição inicial x (m): ",Xe[3])
print("Posição inicial y (m): ",Xe[4])
print("Altitude inicial (m): ",Xe[5])

CD = CD0+k*CL**2
gamma_teo = -np.arctan(CD/CL)
_,_,rho,_,_,_=ISA(H0,0)
V_teo = np.sqrt(2*m*g/(rho*S*np.sqrt(CD**2+CL**2)))
print("Valor teórico da velocidade (m/s): ",V_teo)
print("Valor teórico do ângulo de trajetória (°): ", gamma_teo*180/np.pi)

sol = solve_ivp(simula_planeio,[0,TF],Xe)

t=np.array(sol.t)
V=np.array(sol.y[0]); gama=np.array(sol.y[1]); psi=np.array(sol.y[2])
x0=np.array(sol.y[3]); y0=np.array(sol.y[4]); H=np.array(sol.y[5])

N=np.size(t)
iN=0
while H[iN]>=0:
    iN=iN+1
    if iN>N-1:
        break

if iN==N:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Tempo insuficiente para concluir o voo de planeio")
    print("Rode o programa novamente com um tempo maior")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    sys.exit(0)

t = np.array(t[0:iN])
V = np.array(V[0:iN]); gama = np.array(gama[0:iN]); psi = np.array(psi[0:iN])
x0 = np.array(x0[0:iN]);y0 = np.array(y0[0:iN]); H = np.array(H[0:iN])

print("Resultados do Voo de Planeio");
print("Tempo do voo (hr:min:seg):",datetime.timedelta(seconds = t[-1]))
print("Distância percorrida (m): ",x0[-1]/1e3)

plt.close("all")

plt.figure(1)

plt.subplot(3,2,1);plt.plot(t,V)
plt.xlabel('t(s)');plt.ylabel('V (m/s)'); plt.grid()

plt.subplot(3,2,2);plt.plot(t,gama*180/np.pi)
plt.xlabel('t(s)');plt.ylabel('gama (graus)'); plt.grid()

plt.subplot(3,2,3);plt.plot(t,psi*180/np.pi)
plt.xlabel('t(s)');plt.ylabel('psi (graus)'); plt.grid()

plt.subplot(3,2,4);plt.plot(t,x0/1e3)
plt.xlabel('t(s)');plt.ylabel('x_0 (km)'); plt.grid()

plt.subplot(3,2,5);plt.plot(t,y0/1e3)
plt.xlabel('t(s)');plt.ylabel('y_0 (km)'); plt.grid()

plt.subplot(3,2,6);plt.plot(t,H)
plt.xlabel('t(s)');plt.ylabel('H (m)'); plt.grid()

fig2 = plt.figure(2)

ax = fig2.add_subplot(111,projection='3d')
ax.plot(x0/1e3,y0/1e3,H)
ax.set_xlabel('x (km)'); ax.set_ylabel('y (km)'); ax.set_zlabel('H (m)')



    