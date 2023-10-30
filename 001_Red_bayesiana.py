pip install pgmpy

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Crear el modelo de la red bayesiana
model = BayesianNetwork([('Clima', 'LlevarParaguas')])

# Definir las tablas de probabilidad condicionada (CPDs)
cpd_clima = TabularCPD(variable='Clima', variable_card=2, values=[[0.7], [0.3]])
cpd_llevar_paraguas = TabularCPD(variable='LlevarParaguas', variable_card=2, values=[[0.9, 0.6], [0.1, 0.4]], evidence=['Clima'], evidence_card=[2])

# Agregar las CPDs al modelo
model.add_cpds(cpd_clima, cpd_llevar_paraguas)

# Verificar si el modelo es válido
model.check_model()

# Realizar inferencia en el modelo
inference = VariableElimination(model)
probability = inference.query(variables=['LlevarParaguas'], evidence={'Clima': 1})
print(probability)
