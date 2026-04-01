import numpy as np
# Cria o atalho que o MXNet espera encontrar
np.bool = bool
np.float = float
np.int = int

import mxnet as mx
# ... resto do seu código



import cv2
import geomstats.backend as gs
from GraphRicciCurvature.OllivierRicci import OllivierRicci


print("OpenCV versão:", cv2.__version__)
print("Backend Geomstats:", gs.__name__)
print("MXNet carregado com sucesso!")
