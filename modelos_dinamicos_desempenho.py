from dinamica_translacao import dinamica_translacao
from controles import controles_planeio
import numpy as np


def simula_planeio(t,X):
    CL,F,phi,Y=controles_planeio()
    U = np.array([CL,F,phi,Y])
    Xp = dinamica_translacao(t,X,U)
    return Xp
