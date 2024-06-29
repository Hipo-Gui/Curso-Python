"""
CONSTANTE = 'Variáveis' que não vão mudar(ruim) 
    <- contagem de complexidade(ruim)

"""
velocidade = 61 # valocidade atual do carro 
local_carro = 101 # local em que o carro está na estrada.

RADAR_1 = 60 #Valocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está 
RADAR_RANGE = 1 # A distância onde o radar pega

valocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and valocidade_carro_passou_radar_1  

  
if  valocidade_carro_passou_radar_1:
    print('Velocidade carro passou o radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if  carro_passou_radar_1:
    print('Carro multado em radar 1')      