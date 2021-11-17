from collections import namedtuple

Genotype = namedtuple('Genotype', 'normal normal_concat reduce reduce_concat')

STEP=4

PRIMITIVES = [
    'none',
    'max_pool_3x3',
    'avg_pool_3x3',
    'skip_connect',
    'sep_conv_3x3',
    'sep_conv_5x5',
    'dil_conv_3x3',
    'dil_conv_5x5'
]


DARTS_V1 = Genotype(
	normal=[
	('sep_conv_3x3', 1), ('sep_conv_3x3', 0), 
	('skip_connect', 0), ('sep_conv_3x3', 1),
	('skip_connect', 0), ('sep_conv_3x3', 1),
	('sep_conv_3x3', 0), ('skip_connect', 2)], 
	normal_concat=[2, 3, 4, 5], 
	reduce=[
	('max_pool_3x3', 0), ('max_pool_3x3', 1), 
	('skip_connect', 2), ('max_pool_3x3', 0), 
	('max_pool_3x3', 0), ('skip_connect', 2), 
	('skip_connect', 2), ('avg_pool_3x3', 0)], 
	reduce_concat=[2, 3, 4, 5])
	
	
DARTS_V2 = Genotype(
	normal=[
	('sep_conv_3x3', 0), ('sep_conv_3x3', 1), 
	('sep_conv_3x3', 0), ('sep_conv_3x3', 1), 
	('sep_conv_3x3', 1), ('skip_connect', 0), 
	('skip_connect', 0), ('dil_conv_3x3', 2)], 
	normal_concat=[2, 3, 4, 5], 
	reduce=[
	('max_pool_3x3', 0), ('max_pool_3x3', 1), 
	('skip_connect', 2), ('max_pool_3x3', 1), 
	('max_pool_3x3', 0), ('skip_connect', 2), 
	('skip_connect', 2), ('max_pool_3x3', 1)], 
	reduce_concat=[2, 3, 4, 5])


SYNFLOW_oneshot_seed0 = Genotype(normal=[('sep_conv_5x5', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('dil_conv_5x5', 1), ('dil_conv_3x3', 0), ('dil_conv_3x3', 1), ('max_pool_3x3', 3), ('sep_conv_3x3', 0)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 0), ('avg_pool_3x3', 3), ('sep_conv_3x3', 2), ('dil_conv_5x5', 1), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6)) 

SYNFLOW_oneshot_seed1 = Genotype(normal=[('dil_conv_3x3', 0), ('dil_conv_5x5', 1), ('avg_pool_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('dil_conv_3x3', 4), ('sep_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('dil_conv_5x5', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 2), ('sep_conv_5x5', 3), ('dil_conv_5x5', 2), ('avg_pool_3x3', 1)], reduce_concat=range(2, 6))   
SYNFLOW_oneshot_seed2 = Genotype(normal=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), ('sep_conv_3x3', 0), ('sep_conv_5x5', 0), ('dil_conv_5x5', 2), ('sep_conv_5x5', 4), ('sep_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 3), ('sep_conv_3x3', 4), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))      
SYNFLOW_oneshot_seed3 = Genotype(normal=[('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('dil_conv_5x5', 3), ('sep_conv_3x3', 2), ('avg_pool_3x3', 1)], normal_concat=range(2, 6), reduce=[('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('sep_conv_5x5', 2), ('sep_conv_5x5', 0), ('sep_conv_5x5', 3), ('skip_connect', 0), ('sep_conv_3x3', 4), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))
    
SYNFLOW_oneshot_seed4 = Genotype(normal=[('sep_conv_5x5', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_5x5', 2), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_5x5', 3), ('sep_conv_5x5', 1)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 1), ('sep_conv_5x5', 2), ('sep_conv_3x3', 3), ('sep_conv_5x5', 2), ('sep_conv_3x3', 2), ('sep_conv_3x3', 4)], reduce_concat=range(2, 6))
    



SYNFLOW_oneshot_20cells_seed0 = Genotype(normal=[('avg_pool_3x3', 1), ('sep_conv_3x3', 0), ('dil_conv_5x5', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 1), ('dil_conv_5x5', 2), ('sep_conv_5x5', 3), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('dil_conv_5x5', 1), ('dil_conv_5x5', 0), ('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 2), ('max_pool_3x3', 3), ('dil_conv_5x5', 3), ('sep_conv_5x5', 4)], reduce_concat=range(2, 6))

SYNFLOW_oneshot_20cells_seed1 = Genotype(normal=[('avg_pool_3x3', 1), ('dil_conv_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_5x5', 1), ('skip_connect', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('avg_pool_3x3', 3)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 1), ('dil_conv_5x5', 0), ('skip_connect', 0), ('sep_conv_3x3', 1), ('avg_pool_3x3', 0), ('max_pool_3x3', 2), ('skip_connect', 0), ('sep_conv_5x5', 4)], reduce_concat=range(2, 6))


SYNFLOW_oneshot_20cells_seed2 = Genotype(normal=[('dil_conv_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 0), ('avg_pool_3x3', 2), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('sep_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 1), ('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('dil_conv_5x5', 2), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('max_pool_3x3', 4), ('sep_conv_5x5', 2)], reduce_concat=range(2, 6))
    
SYNFLOW_oneshot_20cells_seed3 = Genotype(normal=[('sep_conv_5x5', 1), ('avg_pool_3x3', 0), ('sep_conv_3x3', 2), ('skip_connect', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('max_pool_3x3', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('sep_conv_3x3', 1), ('max_pool_3x3', 2), ('dil_conv_5x5', 0), ('max_pool_3x3', 2)], reduce_concat=range(2, 6))
    
SYNFLOW_oneshot_20cells_seed4 = Genotype(normal=[('dil_conv_3x3', 1), ('skip_connect', 0), ('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 3), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 1), ('avg_pool_3x3', 0), ('max_pool_3x3', 2), ('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('dil_conv_5x5', 3), ('skip_connect', 0), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))
    

    
SYNFLOW_ImageNet_oneshot_seed0 = Genotype(normal=[('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('dil_conv_3x3', 1), ('dil_conv_3x3', 0), ('sep_conv_3x3', 2), ('dil_conv_5x5', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 2)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 0), ('max_pool_3x3', 1), ('dil_conv_3x3', 0), ('skip_connect', 1), ('sep_conv_5x5', 3), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))

SYNFLOW_ImageNet_oneshot_seed1 = Genotype(normal=[('sep_conv_5x5', 0), ('max_pool_3x3', 1), ('dil_conv_5x5', 2), ('max_pool_3x3', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('dil_conv_5x5', 1), ('avg_pool_3x3', 0), ('max_pool_3x3', 0), ('max_pool_3x3', 1), ('sep_conv_3x3', 1), ('dil_conv_5x5', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))

SYNFLOW_ImageNet_oneshot_seed2 = Genotype(normal=[('skip_connect', 0), ('sep_conv_5x5', 1), ('skip_connect', 0), ('sep_conv_5x5', 1), ('skip_connect', 0), ('sep_conv_5x5', 3), ('sep_conv_5x5', 2), ('sep_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 3), ('dil_conv_5x5', 2), ('sep_conv_5x5', 3), ('dil_conv_3x3', 2)], reduce_concat=range(2, 6))
    
SYNFLOW_ImageNet_oneshot_seed3 = Genotype(normal=[('sep_conv_3x3', 1), ('avg_pool_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_3x3', 1), ('sep_conv_5x5', 3), ('dil_conv_5x5', 0), ('sep_conv_3x3', 2), ('sep_conv_5x5', 1)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('max_pool_3x3', 0), ('max_pool_3x3', 2), ('sep_conv_5x5', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 4), ('sep_conv_3x3', 0)], reduce_concat=range(2, 6))
    
SYNFLOW_ImageNet_oneshot_seed4 = Genotype(normal=[('dil_conv_3x3', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 3), ('sep_conv_5x5', 0), ('sep_conv_5x5', 3), ('sep_conv_5x5', 1)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 2), ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 3)], reduce_concat=range(2, 6))
    


    


GraSP_oneshot_seed0 = Genotype(normal=[('sep_conv_3x3', 1), ('skip_connect', 0), ('max_pool_3x3', 2), ('sep_conv_3x3', 0), ('dil_conv_3x3', 0), ('dil_conv_3x3', 2), ('sep_conv_5x5', 1), ('max_pool_3x3', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('max_pool_3x3', 2), ('dil_conv_3x3', 0), ('dil_conv_5x5', 0), ('dil_conv_3x3', 1), ('avg_pool_3x3', 0), ('skip_connect', 1)], reduce_concat=range(2, 6))

GraSP_oneshot_seed1 = Genotype(normal=[('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('dil_conv_5x5', 2), ('dil_conv_3x3', 1), ('sep_conv_3x3', 2), ('dil_conv_5x5', 1)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('max_pool_3x3', 1), ('avg_pool_3x3', 2), ('dil_conv_3x3', 3), ('max_pool_3x3', 0), ('sep_conv_3x3', 3), ('avg_pool_3x3', 2)], reduce_concat=range(2, 6))    
GraSP_oneshot_seed2 = Genotype(normal=[('dil_conv_5x5', 1), ('max_pool_3x3', 0), ('sep_conv_3x3', 0), ('dil_conv_3x3', 2), ('max_pool_3x3', 2), ('avg_pool_3x3', 1), ('sep_conv_3x3', 3), ('dil_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('skip_connect', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 0), ('dil_conv_3x3', 2), ('dil_conv_5x5', 3), ('sep_conv_3x3', 4), ('dil_conv_5x5', 2)], reduce_concat=range(2, 6))

GraSP_oneshot_seed3 = Genotype(normal=[('dil_conv_5x5', 0), ('skip_connect', 1), ('dil_conv_5x5', 0), ('skip_connect', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 3), ('sep_conv_3x3', 2), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('avg_pool_3x3', 1), ('skip_connect', 0), ('sep_conv_5x5', 2), ('sep_conv_5x5', 3), ('max_pool_3x3', 2), ('dil_conv_5x5', 3), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))


GraSP_oneshot_seed4 =Genotype(normal=[('avg_pool_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3), ('max_pool_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('dil_conv_5x5', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 2), ('dil_conv_3x3', 1), ('avg_pool_3x3', 3), ('sep_conv_5x5', 0), ('sep_conv_3x3', 4), ('max_pool_3x3', 3)], reduce_concat=range(2, 6))


SNIP_oneshot_seed0 = Genotype(normal=[('skip_connect', 0), ('skip_connect', 1), ('dil_conv_3x3', 2), ('sep_conv_3x3', 1), ('dil_conv_3x3', 0), ('sep_conv_5x5', 1), ('dil_conv_3x3', 0), ('dil_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('dil_conv_3x3', 1), ('dil_conv_3x3', 0), ('avg_pool_3x3', 3), ('sep_conv_3x3', 2), ('sep_conv_5x5', 4), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))


SNIP_oneshot_seed1 = Genotype(normal=[('dil_conv_3x3', 0), ('dil_conv_5x5', 1), ('sep_conv_3x3', 2), ('dil_conv_5x5', 0), ('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 2), ('sep_conv_3x3', 1), ('avg_pool_3x3', 1), ('sep_conv_3x3', 4)], reduce_concat=range(2, 6))

SNIP_oneshot_seed2 = Genotype(normal=[('max_pool_3x3', 0), ('dil_conv_5x5', 1), ('dil_conv_5x5', 1), ('dil_conv_3x3', 2), ('skip_connect', 0), ('dil_conv_5x5', 1), ('dil_conv_3x3', 0), ('max_pool_3x3', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_5x5', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 2), ('avg_pool_3x3', 0), ('sep_conv_3x3', 3), ('sep_conv_5x5', 2)], reduce_concat=range(2, 6))

SNIP_oneshot_seed3 = Genotype(normal=[('max_pool_3x3', 0), ('skip_connect', 1), ('skip_connect', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 3), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('max_pool_3x3', 4)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_5x5', 2), ('avg_pool_3x3', 1), ('sep_conv_5x5', 3), ('sep_conv_3x3', 2), ('dil_conv_5x5', 4), ('skip_connect', 1)], reduce_concat=range(2, 6))

SNIP_oneshot_seed4 = Genotype(normal=[('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('sep_conv_5x5', 0), ('max_pool_3x3', 1), ('dil_conv_3x3', 3), ('avg_pool_3x3', 1), ('sep_conv_5x5', 3), ('sep_conv_5x5', 1)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('skip_connect', 0), ('sep_conv_3x3', 2), ('max_pool_3x3', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 4), ('sep_conv_5x5', 1)], reduce_concat=range(2, 6))

 
