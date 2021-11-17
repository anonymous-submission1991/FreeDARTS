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

all_none = Genotype(
	normal=[
	('none', 1), ('none', 0), 
	('none', 0), ('none', 1),
	('none', 0), ('none', 1),
	('none', 0), ('none', 2)], 
	normal_concat=[2, 3, 4, 5], 
	reduce=[
	('none', 0), ('none', 1), 
	('none', 2), ('none', 0), 
	('none', 0), ('none', 2), 
	('none', 2), ('none', 0)], 
	reduce_concat=[2, 3, 4, 5])


all_max_pool_3x3 = Genotype(
	normal=[
	('max_pool_3x3', 1), ('max_pool_3x3', 0), 
	('max_pool_3x3', 0), ('max_pool_3x3', 1),
	('max_pool_3x3', 0), ('max_pool_3x3', 1),
	('max_pool_3x3', 0), ('max_pool_3x3', 2)], 
	normal_concat=[2, 3, 4, 5], 
	reduce=[
	('max_pool_3x3', 0), ('max_pool_3x3', 1), 
	('max_pool_3x3', 2), ('max_pool_3x3', 0), 
	('max_pool_3x3', 0), ('max_pool_3x3', 2), 
	('max_pool_3x3', 2), ('max_pool_3x3', 0)], 
	reduce_concat=[2, 3, 4, 5])

all_skip_connect = Genotype(
	normal=[
	('skip_connect', 1), ('skip_connect', 0), 
	('skip_connect', 0), ('skip_connect', 1),
	('skip_connect', 0), ('skip_connect', 1),
	('skip_connect', 0), ('skip_connect', 2)], 
	normal_concat=[2, 3, 4, 5], 
	reduce=[
	('skip_connect', 0), ('skip_connect', 1), 
	('skip_connect', 2), ('skip_connect', 0), 
	('skip_connect', 0), ('skip_connect', 2), 
	('skip_connect', 2), ('skip_connect', 0)], 
	reduce_concat=[2, 3, 4, 5])

all_avg_pool_3x3 = Genotype(
	normal=[
	('avg_pool_3x3', 1), ('avg_pool_3x3', 0), 
	('avg_pool_3x3', 0), ('avg_pool_3x3', 1),
	('avg_pool_3x3', 0), ('avg_pool_3x3', 1),
	('avg_pool_3x3', 0), ('avg_pool_3x3', 2)], 
	normal_concat=[2, 3, 4, 5], 
	reduce=[
	('avg_pool_3x3', 0), ('avg_pool_3x3', 1), 
	('avg_pool_3x3', 2), ('avg_pool_3x3', 0), 
	('avg_pool_3x3', 0), ('avg_pool_3x3', 2), 
	('avg_pool_3x3', 2), ('avg_pool_3x3', 0)], 
	reduce_concat=[2, 3, 4, 5])

all_sep_conv_3x3 = Genotype(
	normal=[
	('sep_conv_3x3', 1), ('sep_conv_3x3', 0), 
	('sep_conv_3x3', 0), ('sep_conv_3x3', 1),
	('sep_conv_3x3', 0), ('sep_conv_3x3', 1),
	('sep_conv_3x3', 0), ('sep_conv_3x3', 2)], 
	normal_concat=[2, 3, 4, 5], 
	reduce=[
	('sep_conv_3x3', 0), ('sep_conv_3x3', 1), 
	('sep_conv_3x3', 2), ('sep_conv_3x3', 0), 
	('sep_conv_3x3', 0), ('sep_conv_3x3', 2), 
	('sep_conv_3x3', 2), ('sep_conv_3x3', 0)], 
	reduce_concat=[2, 3, 4, 5])

all_sep_conv_5x5 = Genotype(
	normal=[
	('sep_conv_5x5', 1), ('sep_conv_5x5', 0), 
	('sep_conv_5x5', 0), ('sep_conv_5x5', 2),
	('sep_conv_5x5', 0), ('sep_conv_5x5', 3),
	('sep_conv_5x5', 0), ('sep_conv_5x5', 4)], 
	normal_concat=[2, 3, 4, 5], 
	reduce=[
	('sep_conv_5x5', 0), ('sep_conv_5x5', 1), 
	('sep_conv_5x5', 2), ('sep_conv_5x5', 0), 
	('sep_conv_5x5', 0), ('sep_conv_5x5', 3), 
	('sep_conv_5x5', 4), ('sep_conv_5x5', 0)], 
	reduce_concat=[2, 3, 4, 5])

all_dil_conv_3x3 = Genotype(
	normal=[
	('dil_conv_3x3', 1), ('dil_conv_3x3', 0), 
	('dil_conv_3x3', 0), ('dil_conv_3x3', 1),
	('dil_conv_3x3', 0), ('dil_conv_3x3', 1),
	('dil_conv_3x3', 0), ('dil_conv_3x3', 2)], 
	normal_concat=[2, 3, 4, 5], 
	reduce=[
	('dil_conv_3x3', 0), ('dil_conv_3x3', 1), 
	('dil_conv_3x3', 2), ('dil_conv_3x3', 0), 
	('dil_conv_3x3', 0), ('dil_conv_3x3', 2), 
	('dil_conv_3x3', 2), ('dil_conv_3x3', 0)], 
	reduce_concat=[2, 3, 4, 5])

all_dil_conv_5x5 = Genotype(
	normal=[
	('dil_conv_5x5', 1), ('sep_conv_5x5', 0), 
	('dil_conv_5x5', 0), ('sep_conv_5x5', 2),
	('dil_conv_5x5', 0), ('dil_conv_5x5', 3),
	('dil_conv_5x5', 0), ('dil_conv_5x5', 4)], 
	normal_concat=[2, 3, 4, 5], 
	reduce=[
	('dil_conv_5x5', 0), ('dil_conv_5x5', 1), 
	('dil_conv_5x5', 2), ('dil_conv_5x5', 0), 
	('dil_conv_5x5', 0), ('dil_conv_5x5', 3), 
	('dil_conv_5x5', 4), ('dil_conv_5x5', 0)], 
	reduce_concat=[2, 3, 4, 5])
	
    
    

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
    
SYNFLOW_oneshot_seed5 = Genotype(normal=[('dil_conv_3x3', 0), ('dil_conv_5x5', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 1), ('dil_conv_5x5', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 4), ('dil_conv_3x3', 0)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 2), ('sep_conv_3x3', 1), ('sep_conv_5x5', 2), ('sep_conv_3x3', 3), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2)], reduce_concat=range(2, 6))    
SYNFLOW_oneshot_seed6 = Genotype(normal=[('dil_conv_5x5', 1), ('sep_conv_3x3', 0), ('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 1), ('max_pool_3x3', 0), ('avg_pool_3x3', 3), ('skip_connect', 0)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('avg_pool_3x3', 0), ('max_pool_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_5x5', 3), ('dil_conv_5x5', 2), ('sep_conv_5x5', 1)], reduce_concat=range(2, 6))    
SYNFLOW_oneshot_seed7 = Genotype(normal=[('avg_pool_3x3', 1), ('dil_conv_3x3', 0), ('max_pool_3x3', 2), ('sep_conv_3x3', 0), ('avg_pool_3x3', 0), ('skip_connect', 1), ('sep_conv_3x3', 4), ('sep_conv_5x5', 1)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 0), ('avg_pool_3x3', 3), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2), ('sep_conv_5x5', 4)], reduce_concat=range(2, 6))

SYNFLOW_oneshot_seed8 = Genotype(normal=[('dil_conv_3x3', 1), ('max_pool_3x3', 0), ('sep_conv_3x3', 0), ('dil_conv_5x5', 1), ('dil_conv_3x3', 0), ('dil_conv_3x3', 3), ('sep_conv_3x3', 0), ('dil_conv_3x3', 1)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('avg_pool_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 3), ('sep_conv_3x3', 0), ('max_pool_3x3', 2), ('max_pool_3x3', 0)], reduce_concat=range(2, 6))


SYNFLOW_oneshot_seed9 =Genotype(normal=[('max_pool_3x3', 0), ('max_pool_3x3', 1), ('sep_conv_3x3', 2), ('dil_conv_3x3', 1), ('sep_conv_5x5', 3), ('sep_conv_3x3', 2), ('sep_conv_5x5', 4), ('sep_conv_5x5', 0)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 1), ('skip_connect', 0), ('sep_conv_3x3', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 1), ('dil_conv_3x3', 0), ('sep_conv_5x5', 3), ('skip_connect', 1)], reduce_concat=range(2, 6))




SYNFLOW_oneshot_20cells_seed0 = Genotype(normal=[('avg_pool_3x3', 1), ('sep_conv_3x3', 0), ('dil_conv_5x5', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 1), ('dil_conv_5x5', 2), ('sep_conv_5x5', 3), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('dil_conv_5x5', 1), ('dil_conv_5x5', 0), ('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 2), ('max_pool_3x3', 3), ('dil_conv_5x5', 3), ('sep_conv_5x5', 4)], reduce_concat=range(2, 6))

SYNFLOW_oneshot_20cells_seed1 = Genotype(normal=[('avg_pool_3x3', 1), ('dil_conv_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_5x5', 1), ('skip_connect', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('avg_pool_3x3', 3)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 1), ('dil_conv_5x5', 0), ('skip_connect', 0), ('sep_conv_3x3', 1), ('avg_pool_3x3', 0), ('max_pool_3x3', 2), ('skip_connect', 0), ('sep_conv_5x5', 4)], reduce_concat=range(2, 6))


SYNFLOW_oneshot_20cells_seed2 = Genotype(normal=[('dil_conv_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 0), ('avg_pool_3x3', 2), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('sep_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 1), ('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('dil_conv_5x5', 2), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('max_pool_3x3', 4), ('sep_conv_5x5', 2)], reduce_concat=range(2, 6))
    
SYNFLOW_oneshot_20cells_seed3 = Genotype(normal=[('sep_conv_5x5', 1), ('avg_pool_3x3', 0), ('sep_conv_3x3', 2), ('skip_connect', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('max_pool_3x3', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('sep_conv_3x3', 1), ('max_pool_3x3', 2), ('dil_conv_5x5', 0), ('max_pool_3x3', 2)], reduce_concat=range(2, 6))
    
SYNFLOW_oneshot_20cells_seed4 = Genotype(normal=[('dil_conv_3x3', 1), ('skip_connect', 0), ('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 3), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 1), ('avg_pool_3x3', 0), ('max_pool_3x3', 2), ('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('dil_conv_5x5', 3), ('skip_connect', 0), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))
    
SYNFLOW_oneshot_20cells_seed5 = Genotype(normal=[('dil_conv_3x3', 1), ('skip_connect', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 2), ('max_pool_3x3', 0), ('max_pool_3x3', 3), ('max_pool_3x3', 3), ('max_pool_3x3', 4)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 0), ('skip_connect', 1), ('max_pool_3x3', 2), ('sep_conv_5x5', 1), ('sep_conv_3x3', 3), ('dil_conv_5x5', 2), ('skip_connect', 1), ('dil_conv_3x3', 2)], reduce_concat=range(2, 6))


SYNFLOW_oneshot_20cells_seed6 = Genotype(normal=[('max_pool_3x3', 1), ('dil_conv_3x3', 0), ('dil_conv_5x5', 2), ('dil_conv_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_5x5', 1), ('max_pool_3x3', 4), ('max_pool_3x3', 0)], normal_concat=range(2, 6), reduce=[('skip_connect', 1), ('sep_conv_5x5', 0), ('skip_connect', 1), ('avg_pool_3x3', 2), ('skip_connect', 1), ('dil_conv_5x5', 2), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3)], reduce_concat=range(2, 6))

SYNFLOW_oneshot_20cells_seed7 = Genotype(normal=[('dil_conv_5x5', 1), ('skip_connect', 0), ('max_pool_3x3', 0), ('skip_connect', 1), ('avg_pool_3x3', 2), ('dil_conv_3x3', 1), ('sep_conv_3x3', 4), ('sep_conv_3x3', 1)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 0), ('avg_pool_3x3', 1), ('sep_conv_5x5', 2), ('skip_connect', 1), ('sep_conv_5x5', 2), ('sep_conv_5x5', 0), ('sep_conv_5x5', 4), ('avg_pool_3x3', 1)], reduce_concat=range(2, 6))

SYNFLOW_oneshot_20cells_seed8 = Genotype(normal=[('dil_conv_3x3', 0), ('dil_conv_5x5', 1), ('dil_conv_5x5', 1), ('sep_conv_3x3', 2), ('dil_conv_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_3x3', 3), ('sep_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 0), ('dil_conv_5x5', 2), ('sep_conv_5x5', 0), ('sep_conv_3x3', 3), ('skip_connect', 1), ('dil_conv_5x5', 0)], reduce_concat=range(2, 6))


SYNFLOW_oneshot_20cells_seed9 =Genotype(normal=[('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), ('sep_conv_3x3', 3), ('sep_conv_5x5', 0), ('dil_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('skip_connect', 1), ('dil_conv_3x3', 1), ('avg_pool_3x3', 2), ('dil_conv_3x3', 0), ('avg_pool_3x3', 2), ('skip_connect', 1), ('dil_conv_5x5', 0)], reduce_concat=range(2, 6))







GraSP_oneshot_seed0 = Genotype(normal=[('sep_conv_3x3', 1), ('skip_connect', 0), ('max_pool_3x3', 2), ('sep_conv_3x3', 0), ('dil_conv_3x3', 0), ('dil_conv_3x3', 2), ('sep_conv_5x5', 1), ('max_pool_3x3', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('max_pool_3x3', 2), ('dil_conv_3x3', 0), ('dil_conv_5x5', 0), ('dil_conv_3x3', 1), ('avg_pool_3x3', 0), ('skip_connect', 1)], reduce_concat=range(2, 6))

GraSP_oneshot_seed1 = Genotype(normal=[('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('dil_conv_5x5', 2), ('dil_conv_3x3', 1), ('sep_conv_3x3', 2), ('dil_conv_5x5', 1)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('max_pool_3x3', 1), ('avg_pool_3x3', 2), ('dil_conv_3x3', 3), ('max_pool_3x3', 0), ('sep_conv_3x3', 3), ('avg_pool_3x3', 2)], reduce_concat=range(2, 6))    
GraSP_oneshot_seed2 = Genotype(normal=[('dil_conv_5x5', 1), ('max_pool_3x3', 0), ('sep_conv_3x3', 0), ('dil_conv_3x3', 2), ('max_pool_3x3', 2), ('avg_pool_3x3', 1), ('sep_conv_3x3', 3), ('dil_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('skip_connect', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 0), ('dil_conv_3x3', 2), ('dil_conv_5x5', 3), ('sep_conv_3x3', 4), ('dil_conv_5x5', 2)], reduce_concat=range(2, 6))

GraSP_oneshot_seed3 = Genotype(normal=[('dil_conv_5x5', 0), ('skip_connect', 1), ('dil_conv_5x5', 0), ('skip_connect', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 3), ('sep_conv_3x3', 2), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('avg_pool_3x3', 1), ('skip_connect', 0), ('sep_conv_5x5', 2), ('sep_conv_5x5', 3), ('max_pool_3x3', 2), ('dil_conv_5x5', 3), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))


GraSP_oneshot_seed4 =Genotype(normal=[('avg_pool_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3), ('max_pool_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('dil_conv_5x5', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 2), ('dil_conv_3x3', 1), ('avg_pool_3x3', 3), ('sep_conv_5x5', 0), ('sep_conv_3x3', 4), ('max_pool_3x3', 3)], reduce_concat=range(2, 6))

GraSP_oneshot_seed5 = Genotype(normal=[('dil_conv_5x5', 1), ('dil_conv_3x3', 0), ('sep_conv_3x3', 2), ('dil_conv_5x5', 1), ('sep_conv_5x5', 3), ('dil_conv_5x5', 1), ('sep_conv_5x5', 3), ('sep_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 1), ('avg_pool_3x3', 0), ('sep_conv_3x3', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 0), ('sep_conv_5x5', 3)], reduce_concat=range(2, 6))   
GraSP_oneshot_seed6 =Genotype(normal=[('skip_connect', 1), ('avg_pool_3x3', 0), ('avg_pool_3x3', 2), ('max_pool_3x3', 0), ('sep_conv_5x5', 3), ('avg_pool_3x3', 1), ('sep_conv_5x5', 3), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 2), ('sep_conv_3x3', 2), ('sep_conv_5x5', 3), ('avg_pool_3x3', 3), ('sep_conv_5x5', 1)], reduce_concat=range(2, 6))
    
GraSP_oneshot_seed7 =Genotype(normal=[('skip_connect', 1), ('avg_pool_3x3', 0), ('avg_pool_3x3', 2), ('max_pool_3x3', 0), ('sep_conv_5x5', 3), ('avg_pool_3x3', 1), ('sep_conv_5x5', 3), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 2), ('sep_conv_3x3', 2), ('sep_conv_5x5', 3), ('avg_pool_3x3', 3), ('sep_conv_5x5', 1)], reduce_concat=range(2, 6))
    
GraSP_oneshot_seed8 = Genotype(normal=[('dil_conv_3x3', 1), ('skip_connect', 0), ('dil_conv_5x5', 1), ('dil_conv_5x5', 2), ('dil_conv_3x3', 0), ('dil_conv_5x5', 2), ('dil_conv_3x3', 4), ('avg_pool_3x3', 2)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 1), ('skip_connect', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 3), ('sep_conv_5x5', 2), ('avg_pool_3x3', 3)], reduce_concat=range(2, 6))

GraSP_oneshot_seed9 = Genotype(normal=[('max_pool_3x3', 1), ('dil_conv_5x5', 0), ('sep_conv_3x3', 0), ('max_pool_3x3', 1), ('sep_conv_3x3', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 4), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_5x5', 2), ('dil_conv_3x3', 0), ('dil_conv_5x5', 2), ('sep_conv_5x5', 0), ('skip_connect', 1)], reduce_concat=range(2, 6))
    

SNIP_oneshot_seed0 = Genotype(normal=[('skip_connect', 0), ('skip_connect', 1), ('dil_conv_3x3', 2), ('sep_conv_3x3', 1), ('dil_conv_3x3', 0), ('sep_conv_5x5', 1), ('dil_conv_3x3', 0), ('dil_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('dil_conv_3x3', 1), ('dil_conv_3x3', 0), ('avg_pool_3x3', 3), ('sep_conv_3x3', 2), ('sep_conv_5x5', 4), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))


SNIP_oneshot_seed1 = Genotype(normal=[('dil_conv_3x3', 0), ('dil_conv_5x5', 1), ('sep_conv_3x3', 2), ('dil_conv_5x5', 0), ('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 2), ('sep_conv_3x3', 1), ('avg_pool_3x3', 1), ('sep_conv_3x3', 4)], reduce_concat=range(2, 6))

SNIP_oneshot_seed2 = Genotype(normal=[('max_pool_3x3', 0), ('dil_conv_5x5', 1), ('dil_conv_5x5', 1), ('dil_conv_3x3', 2), ('skip_connect', 0), ('dil_conv_5x5', 1), ('dil_conv_3x3', 0), ('max_pool_3x3', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_5x5', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 2), ('avg_pool_3x3', 0), ('sep_conv_3x3', 3), ('sep_conv_5x5', 2)], reduce_concat=range(2, 6))

SNIP_oneshot_seed3 = Genotype(normal=[('max_pool_3x3', 0), ('skip_connect', 1), ('skip_connect', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 3), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('max_pool_3x3', 4)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_5x5', 2), ('avg_pool_3x3', 1), ('sep_conv_5x5', 3), ('sep_conv_3x3', 2), ('dil_conv_5x5', 4), ('skip_connect', 1)], reduce_concat=range(2, 6))

SNIP_oneshot_seed4 = Genotype(normal=[('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('sep_conv_5x5', 0), ('max_pool_3x3', 1), ('dil_conv_3x3', 3), ('avg_pool_3x3', 1), ('sep_conv_5x5', 3), ('sep_conv_5x5', 1)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('skip_connect', 0), ('sep_conv_3x3', 2), ('max_pool_3x3', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 4), ('sep_conv_5x5', 1)], reduce_concat=range(2, 6))

SNIP_oneshot_seed5 = Genotype(normal=[('avg_pool_3x3', 1), ('skip_connect', 0), ('dil_conv_5x5', 2), ('dil_conv_5x5', 1), ('max_pool_3x3', 1), ('skip_connect', 0), ('sep_conv_3x3', 4), ('avg_pool_3x3', 0)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2), ('avg_pool_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 0), ('sep_conv_5x5', 3)], reduce_concat=range(2, 6))

SNIP_oneshot_seed6 = Genotype(normal=[('sep_conv_3x3', 1), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_5x5', 3), ('skip_connect', 0), ('sep_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 1), ('dil_conv_5x5', 0), ('dil_conv_5x5', 2), ('avg_pool_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 3), ('avg_pool_3x3', 3), ('skip_connect', 0)], reduce_concat=range(2, 6))

SNIP_oneshot_seed7 = Genotype(normal=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 0), ('max_pool_3x3', 2), ('sep_conv_3x3', 3), ('skip_connect', 1), ('dil_conv_5x5', 1), ('sep_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 1), ('max_pool_3x3', 0), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('dil_conv_5x5', 3), ('dil_conv_5x5', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 0)], reduce_concat=range(2, 6))

SNIP_oneshot_seed8 = Genotype(normal=[('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('dil_conv_5x5', 1), ('avg_pool_3x3', 2), ('dil_conv_3x3', 3), ('dil_conv_5x5', 2), ('dil_conv_3x3', 0), ('dil_conv_3x3', 1)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 1), ('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 3), ('sep_conv_5x5', 0), ('dil_conv_3x3', 3), ('dil_conv_5x5', 2)], reduce_concat=range(2, 6))

SNIP_oneshot_seed9 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 3), ('sep_conv_5x5', 3), ('avg_pool_3x3', 4)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_5x5', 2), ('dil_conv_5x5', 1), ('dil_conv_5x5', 2), ('sep_conv_5x5', 3), ('sep_conv_5x5', 0)], reduce_concat=range(2, 6))
    
 


SYNFLOW_ImageNet_oneshot_seed0 = Genotype(normal=[('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('dil_conv_3x3', 1), ('dil_conv_3x3', 0), ('sep_conv_3x3', 2), ('dil_conv_5x5', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 2)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 0), ('max_pool_3x3', 1), ('dil_conv_3x3', 0), ('skip_connect', 1), ('sep_conv_5x5', 3), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))

SYNFLOW_ImageNet_oneshot_seed1 = Genotype(normal=[('sep_conv_5x5', 0), ('max_pool_3x3', 1), ('dil_conv_5x5', 2), ('max_pool_3x3', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('dil_conv_5x5', 1), ('avg_pool_3x3', 0), ('max_pool_3x3', 0), ('max_pool_3x3', 1), ('sep_conv_3x3', 1), ('dil_conv_5x5', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))

SYNFLOW_ImageNet_oneshot_seed2 = Genotype(normal=[('skip_connect', 0), ('sep_conv_5x5', 1), ('skip_connect', 0), ('sep_conv_5x5', 1), ('skip_connect', 0), ('sep_conv_5x5', 3), ('sep_conv_5x5', 2), ('sep_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 3), ('dil_conv_5x5', 2), ('sep_conv_5x5', 3), ('dil_conv_3x3', 2)], reduce_concat=range(2, 6))
    
SYNFLOW_ImageNet_oneshot_seed3 = Genotype(normal=[('sep_conv_3x3', 1), ('avg_pool_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_3x3', 1), ('sep_conv_5x5', 3), ('dil_conv_5x5', 0), ('sep_conv_3x3', 2), ('sep_conv_5x5', 1)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('max_pool_3x3', 0), ('max_pool_3x3', 2), ('sep_conv_5x5', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 4), ('sep_conv_3x3', 0)], reduce_concat=range(2, 6))
    
SYNFLOW_ImageNet_oneshot_seed4 = Genotype(normal=[('dil_conv_3x3', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 3), ('sep_conv_5x5', 0), ('sep_conv_5x5', 3), ('sep_conv_5x5', 1)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 2), ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 3)], reduce_concat=range(2, 6))
    
SYNFLOW_ImageNet_oneshot_seed5 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 3), ('avg_pool_3x3', 1), ('sep_conv_5x5', 3), ('sep_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 0), ('dil_conv_3x3', 1), ('dil_conv_5x5', 1), ('max_pool_3x3', 2), ('sep_conv_5x5', 0), ('sep_conv_3x3', 2), ('sep_conv_3x3', 2), ('sep_conv_5x5', 3)], reduce_concat=range(2, 6))

SYNFLOW_ImageNet_oneshot_seed6 = Genotype(normal=[('skip_connect', 0), ('dil_conv_5x5', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 0), ('sep_conv_5x5', 3), ('dil_conv_5x5', 1)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('avg_pool_3x3', 0), ('max_pool_3x3', 1), ('sep_conv_5x5', 3), ('avg_pool_3x3', 1), ('sep_conv_5x5', 4), ('dil_conv_3x3', 1)], reduce_concat=range(2, 6))

SYNFLOW_ImageNet_oneshot_seed7 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2), ('sep_conv_5x5', 3), ('avg_pool_3x3', 1), ('sep_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 0), ('skip_connect', 1), ('sep_conv_3x3', 1), ('dil_conv_3x3', 2), ('avg_pool_3x3', 0), ('max_pool_3x3', 1), ('dil_conv_5x5', 3), ('skip_connect', 1)], reduce_concat=range(2, 6))

SYNFLOW_ImageNet_oneshot_seed8 = Genotype(normal=[('sep_conv_5x5', 0), ('dil_conv_3x3', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 0), ('dil_conv_5x5', 3), ('avg_pool_3x3', 0), ('sep_conv_5x5', 3), ('dil_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 2), ('skip_connect', 0), ('dil_conv_3x3', 2), ('max_pool_3x3', 0), ('dil_conv_3x3', 0), ('max_pool_3x3', 3)], reduce_concat=range(2, 6))

SYNFLOW_ImageNet_oneshot_seed9 =Genotype(normal=[('avg_pool_3x3', 1), ('sep_conv_3x3', 0), ('avg_pool_3x3', 1), ('dil_conv_3x3', 0), ('sep_conv_5x5', 2), ('skip_connect', 1), ('dil_conv_5x5', 4), ('sep_conv_5x5', 0)], normal_concat=range(2, 6), reduce=[('dil_conv_5x5', 0), ('sep_conv_5x5', 1), ('skip_connect', 1), ('sep_conv_5x5', 2), ('sep_conv_3x3', 3), ('max_pool_3x3', 2), ('dil_conv_5x5', 4), ('sep_conv_5x5', 3)], reduce_concat=range(2, 6))





    
    
SYNFLOW_seed22 = Genotype(
	normal=[
	('sep_conv_3x3', 0), ('skip_connect', 1), 
	('dil_conv_5x5', 0), ('skip_connect', 1), 
	('skip_connect', 0), ('max_pool_3x3', 1), 
	('sep_conv_3x3', 0), ('sep_conv_3x3', 3)], 
	normal_concat=[2, 3, 4, 5], 
	reduce=[
	('sep_conv_3x3', 0), ('max_pool_3x3', 1), 
	('dil_conv_5x5', 0), ('sep_conv_3x3', 1), 
	('sep_conv_5x5', 0), ('sep_conv_3x3', 1), 
	('dil_conv_3x3', 0), ('sep_conv_5x5', 3)], 
	reduce_concat=[2, 3, 4, 5])



SYNFLOW_seed0 = Genotype(
	normal=[
	('max_pool_3x3', 0), ('skip_connect', 1), 
	('sep_conv_5x5', 0), ('max_pool_3x3', 2), 
	('sep_conv_5x5', 1), ('dil_conv_3x3', 3), 
	('sep_conv_5x5', 1), ('sep_conv_3x3', 4)], 
	normal_concat=range(2, 6), reduce=[
	('skip_connect', 0), ('avg_pool_3x3', 1), 
	('sep_conv_3x3', 0), ('sep_conv_3x3', 2), 
	('max_pool_3x3', 1), ('avg_pool_3x3', 2), 
	('avg_pool_3x3', 2), ('sep_conv_3x3', 4)], 
	reduce_concat=range(2, 6))
#########initial chanel 50 for imagenet



SYNFLOW_seed1 = Genotype(
	normal=[
	('sep_conv_5x5', 0), ('dil_conv_5x5', 1), 
	('sep_conv_3x3', 0), ('sep_conv_5x5', 2), 
	('max_pool_3x3', 0), ('dil_conv_5x5', 1), 
	('sep_conv_3x3', 2), ('dil_conv_5x5', 3)], 
	normal_concat=range(2, 6), reduce=[
	('dil_conv_3x3', 0), ('max_pool_3x3', 1), 
	('dil_conv_3x3', 1), ('avg_pool_3x3', 2), 
	('avg_pool_3x3', 0), ('sep_conv_5x5', 3), 
	('skip_connect', 0), ('sep_conv_5x5', 2)], 
reduce_concat=range(2, 6))
########initial chanel 48 for imagenet


SYNFLOW_seed2 = Genotype(
	normal=[
	('sep_conv_3x3', 0), ('skip_connect', 1), 
	('dil_conv_5x5', 0), ('skip_connect', 1), 
	('skip_connect', 0), ('max_pool_3x3', 1), 
	('sep_conv_3x3', 0), ('sep_conv_3x3', 3)], 
	normal_concat=range(2, 6), 
	reduce=[
	('sep_conv_3x3', 0), ('max_pool_3x3', 1), 
	('dil_conv_5x5', 0), ('max_pool_3x3', 2), 
	('max_pool_3x3', 2), ('max_pool_3x3', 3), 
	('sep_conv_3x3', 1), ('sep_conv_5x5', 3)], 
	reduce_concat=range(2, 6))#########initial chanel 54 for imagenet
	
	
SYNFLOW_seed3 = Genotype(
	normal=[
	('sep_conv_5x5', 0), ('dil_conv_3x3', 1), 
	('dil_conv_5x5', 0), ('sep_conv_3x3', 2), 
	('max_pool_3x3', 2), ('dil_conv_3x3', 3), 
	('avg_pool_3x3', 0), ('avg_pool_3x3', 3)], 
	normal_concat=range(2, 6), reduce=[
	('dil_conv_5x5', 0), ('dil_conv_3x3', 1), 
	('dil_conv_3x3', 1), ('sep_conv_5x5', 2), 
	('sep_conv_5x5', 2), ('sep_conv_5x5', 3), 
	('dil_conv_3x3', 0), ('sep_conv_5x5', 2)], 
	reduce_concat=range(2, 6))
#####initial chanel 52 for imagenet

SYNFLOW_seed4 = Genotype(
	normal=[
	('sep_conv_5x5', 0), ('dil_conv_3x3', 1), 
	('sep_conv_5x5', 1), ('sep_conv_5x5', 2), 
	('avg_pool_3x3', 0), ('none', 1), 
	('max_pool_3x3', 1), ('dil_conv_5x5', 3)], 
	normal_concat=range(2, 6), reduce=[
	('max_pool_3x3', 0), ('sep_conv_5x5', 1), 
	('skip_connect', 0), ('sep_conv_5x5', 2), 
	('skip_connect', 0), ('avg_pool_3x3', 3), 
	('dil_conv_5x5', 2), ('sep_conv_3x3', 4)], 
	reduce_concat=range(2, 6))
#####initial chanel 52 for imagenet, 617

SYNFLOW_seed5 = Genotype(
	normal=[
	('sep_conv_3x3', 0), ('sep_conv_5x5', 1), 
	('sep_conv_3x3', 0), ('dil_conv_3x3', 1), 
	('skip_connect', 0), ('avg_pool_3x3', 3), 
	('dil_conv_5x5', 0), ('avg_pool_3x3', 3)], 
	normal_concat=range(2, 6), reduce=[
	('max_pool_3x3', 0), ('skip_connect', 1), 
	('avg_pool_3x3', 0), ('dil_conv_3x3', 2), 
	('max_pool_3x3', 0), ('avg_pool_3x3', 3), 
	('skip_connect', 0), ('sep_conv_3x3', 2)], 
	reduce_concat=range(2, 6))
#####initial chanel 52 for imagenet

SYNFLOW_seed6 = Genotype(normal=[('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('dil_conv_5x5', 1), ('max_pool_3x3', 2), ('avg_pool_3x3', 3), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_5x5', 1), ('max_pool_3x3', 2), ('sep_conv_3x3', 1), ('sep_conv_5x5', 2), ('sep_conv_3x3', 2), ('sep_conv_3x3', 4)], reduce_concat=range(2, 6))
##44,3.8
SYNFLOW_seed7 = Genotype(normal=[('avg_pool_3x3', 0), ('dil_conv_5x5', 1), ('dil_conv_3x3', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 2), ('none', 4)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 1), ('sep_conv_5x5', 2), ('skip_connect', 0), ('avg_pool_3x3', 1), ('avg_pool_3x3', 2), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))
##38,3.7

SYNFLOW_seed8 = Genotype(normal=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 1), ('sep_conv_5x5', 2), ('dil_conv_3x3', 0), ('dil_conv_3x3', 2), ('dil_conv_3x3', 0), ('sep_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('avg_pool_3x3', 1), ('avg_pool_3x3', 2), ('dil_conv_3x3', 2), ('max_pool_3x3', 3), ('max_pool_3x3', 2), ('sep_conv_3x3', 4)], reduce_concat=range(2, 6))
###36,3.5, 38,3.9

SYNFLOW_seed9 = Genotype(normal=[('dil_conv_5x5', 0), ('sep_conv_3x3', 1), ('avg_pool_3x3', 1), ('dil_conv_5x5', 2), ('sep_conv_3x3', 0), ('max_pool_3x3', 2), ('sep_conv_3x3', 2), ('avg_pool_3x3', 4)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 0), ('dil_conv_3x3', 1), ('avg_pool_3x3', 0), ('max_pool_3x3', 2), ('sep_conv_5x5', 0), ('dil_conv_5x5', 3), ('skip_connect', 1), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))
###40,3.8, 38,3.4


SYNFLOW_seed10 = Genotype(
	normal=[
	('avg_pool_3x3', 0), ('skip_connect', 1), 
	('dil_conv_5x5', 1), ('sep_conv_3x3', 2), 
	('dil_conv_3x3', 0), ('dil_conv_5x5', 2), 
	('dil_conv_3x3', 1), ('dil_conv_3x3', 3)], 
	normal_concat=range(2, 6), reduce=[
	('skip_connect', 0), ('sep_conv_3x3', 1), 
	('sep_conv_3x3', 0), ('avg_pool_3x3', 2), 
	('sep_conv_3x3', 2), ('avg_pool_3x3', 3), 
	('sep_conv_5x5', 0), ('sep_conv_3x3', 4)], 
	reduce_concat=range(2, 6))
####40, 3.67


SYNFLOW_seed0_imagenet = Genotype(
	normal=[
	('sep_conv_3x3', 0), ('sep_conv_3x3', 1), 
	('sep_conv_5x5', 0), ('max_pool_3x3', 2), 
	('dil_conv_5x5', 1), ('max_pool_3x3', 3), 
	('dil_conv_5x5', 1), ('sep_conv_5x5', 4)], 
	normal_concat=range(2, 6), reduce=[
	('dil_conv_3x3', 0), ('max_pool_3x3', 1), 
	('dil_conv_3x3', 0), ('avg_pool_3x3', 2), 
	('sep_conv_5x5', 1), ('dil_conv_3x3', 2), 
	('avg_pool_3x3', 2), ('max_pool_3x3', 4)], 
reduce_concat=range(2, 6))
##50 595/604

SYNFLOW_seed1_imagenet = Genotype(
	normal=[
	('sep_conv_3x3', 0), ('skip_connect', 1), 
	('sep_conv_3x3', 0), ('sep_conv_3x3', 2), 
	('sep_conv_3x3', 0), ('dil_conv_3x3', 1), 
	('avg_pool_3x3', 2), ('avg_pool_3x3', 3)], 
	normal_concat=range(2, 6), reduce=[
	('dil_conv_3x3', 0), ('max_pool_3x3', 1), 
	('dil_conv_5x5', 1), ('avg_pool_3x3', 2), 
	('max_pool_3x3', 0), ('max_pool_3x3', 3), 
	('avg_pool_3x3', 0), ('max_pool_3x3', 2)], reduce_concat=range(2, 6))
#52   580

SYNFLOW_seed2_imagenet = Genotype(
    normal=[
    ('dil_conv_3x3', 0), ('sep_conv_5x5', 1), 
    ('sep_conv_5x5', 0), ('sep_conv_3x3', 1), 
    ('sep_conv_5x5', 0), ('dil_conv_5x5', 1), 
    ('max_pool_3x3', 0), ('dil_conv_5x5', 3)], 
    normal_concat=range(2, 6), reduce=[
    ('avg_pool_3x3', 0), ('sep_conv_5x5', 1), 
    ('avg_pool_3x3', 0), ('sep_conv_3x3', 2), 
    ('max_pool_3x3', 2), ('sep_conv_3x3', 3), 
    ('dil_conv_3x3', 1), ('sep_conv_5x5', 3)], 
    reduce_concat=range(2, 6))
#48   609

SYNFLOW_seed3_imagenet = Genotype(
    normal=[
    ('dil_conv_5x5', 0), ('max_pool_3x3', 1), 
    ('sep_conv_3x3', 0), ('dil_conv_5x5', 2), 
    ('dil_conv_3x3', 2), ('skip_connect', 3), 
    ('sep_conv_5x5', 0), ('sep_conv_3x3', 3)], 
    normal_concat=range(2, 6), reduce=[
    ('avg_pool_3x3', 0), ('sep_conv_5x5', 1), 
    ('dil_conv_5x5', 1), ('sep_conv_3x3', 2), 
    ('sep_conv_3x3', 2), ('dil_conv_3x3', 3), 
    ('dil_conv_5x5', 0), ('sep_conv_3x3', 2)], 
    reduce_concat=range(2, 6))
#50   595

SYNFLOW_seed4_imagenet = Genotype(
    normal=[
    ('dil_conv_5x5', 0), ('sep_conv_3x3', 1), 
    ('sep_conv_3x3', 1), ('sep_conv_5x5', 2), 
    ('dil_conv_5x5', 0), ('avg_pool_3x3', 1), 
    ('sep_conv_5x5', 1), ('sep_conv_5x5', 3)], 
    normal_concat=range(2, 6), reduce=[
    ('max_pool_3x3', 0), ('skip_connect', 1), 
    ('sep_conv_3x3', 0), ('max_pool_3x3', 2), 
    ('dil_conv_5x5', 0), ('sep_conv_5x5', 3), 
    ('sep_conv_3x3', 2), ('avg_pool_3x3', 4)], 
    reduce_concat=range(2, 6))
#48   629

SYNFLOW_seed5_imagenet = Genotype(
    normal=[
    ('dil_conv_5x5', 0), ('avg_pool_3x3', 1), 
    ('dil_conv_5x5', 0), ('dil_conv_5x5', 1), 
    ('dil_conv_3x3', 0), ('sep_conv_5x5', 3), 
    ('dil_conv_3x3', 0), ('sep_conv_3x3', 3)], 
    normal_concat=range(2, 6), reduce=[
    ('skip_connect', 0), ('dil_conv_5x5', 1), 
    ('sep_conv_3x3', 0), ('sep_conv_5x5', 2), 
    ('dil_conv_5x5', 0), ('sep_conv_5x5', 3), 
    ('skip_connect', 0), ('dil_conv_3x3', 2)], 
    reduce_concat=range(2, 6))
#50 600

SYNFLOW_seed6_imagenet = Genotype(
    normal=[
    ('skip_connect', 0), ('sep_conv_5x5', 1), 
    ('dil_conv_5x5', 0), ('skip_connect', 1), 
    ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), 
    ('sep_conv_3x3', 3), ('sep_conv_3x3', 4)], 
    normal_concat=range(2, 6), reduce=[
    ('dil_conv_3x3', 0), ('dil_conv_5x5', 1), 
    ('sep_conv_5x5', 1), ('max_pool_3x3', 2), 
    ('skip_connect', 1), ('sep_conv_3x3', 2), 
    ('max_pool_3x3', 2), ('max_pool_3x3', 4)], 
    reduce_concat=range(2, 6))
#48   596

SYNFLOW_seed7_imagenet = Genotype(
    normal=[
    ('dil_conv_3x3', 0), ('sep_conv_5x5', 1), 
    ('dil_conv_5x5', 0), ('avg_pool_3x3', 2), 
    ('skip_connect', 0), ('dil_conv_3x3', 3), 
    ('dil_conv_5x5', 2), ('max_pool_3x3', 4)], 
    normal_concat=range(2, 6), reduce=[
    ('sep_conv_3x3', 0), ('sep_conv_5x5', 1), 
    ('sep_conv_3x3', 1), ('none', 2), 
    ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), 
    ('max_pool_3x3', 2), ('dil_conv_3x3', 3)], 
    reduce_concat=range(2, 6))
#54   596

SYNFLOW_seed8_imagenet = Genotype(
    normal=[
    ('skip_connect', 0), ('dil_conv_5x5', 1), 
    ('avg_pool_3x3', 1), ('sep_conv_3x3', 2), 
    ('dil_conv_3x3', 0), ('sep_conv_5x5', 2), 
    ('sep_conv_5x5', 0), ('sep_conv_3x3', 2)], 
    normal_concat=range(2, 6), reduce=[
    ('max_pool_3x3', 0), ('dil_conv_3x3', 1), 
    ('sep_conv_5x5', 1), ('max_pool_3x3', 2), 
    ('sep_conv_5x5', 2), ('sep_conv_5x5', 3), 
    ('sep_conv_5x5', 2), ('dil_conv_5x5', 4)], 
    reduce_concat=range(2, 6))
#48   578

SYNFLOW_seed9_imagenet = Genotype(
    normal=[
    ('sep_conv_5x5', 0), ('dil_conv_5x5', 1), 
    ('skip_connect', 1), ('sep_conv_3x3', 2), 
    ('sep_conv_3x3', 0), ('none', 2), 
    ('sep_conv_5x5', 2), ('sep_conv_5x5', 4)], 
    normal_concat=range(2, 6), reduce=[
    ('dil_conv_5x5', 0), ('skip_connect', 1), 
    ('dil_conv_3x3', 0), ('avg_pool_3x3', 2), 
    ('sep_conv_3x3', 0), ('sep_conv_5x5', 3), 
    ('dil_conv_5x5', 1), ('dil_conv_3x3', 3)], 
    reduce_concat=range(2, 6))
#48   604

SYNFLOW_seed10_imagenet = Genotype(normal=[('sep_conv_3x3', 0), ('dil_conv_3x3', 1), ('dil_conv_5x5', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('sep_conv_5x5', 2), ('avg_pool_3x3', 1), ('sep_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_5x5', 2), ('dil_conv_3x3', 2), ('sep_conv_5x5', 3), ('max_pool_3x3', 0), ('sep_conv_5x5', 4)], reduce_concat=range(2, 6))
#48   621







SYNFLOW_ABS_seed0=Genotype(normal=[('skip_connect', 0), ('skip_connect', 1), ('dil_conv_3x3', 0), ('max_pool_3x3', 2), ('sep_conv_5x5', 1), ('dil_conv_3x3', 3), ('skip_connect', 1), ('dil_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 2), ('sep_conv_5x5', 1), ('dil_conv_5x5', 2), ('dil_conv_3x3', 2), ('max_pool_3x3', 4)], reduce_concat=range(2, 6))
###44

SYNFLOW_ABS_seed1=Genotype(normal=[('dil_conv_3x3', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('sep_conv_3x3', 2), ('sep_conv_5x5', 0), ('sep_conv_3x3', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('max_pool_3x3', 1), ('avg_pool_3x3', 2), ('dil_conv_3x3', 0), ('max_pool_3x3', 3), ('dil_conv_3x3', 0), ('dil_conv_5x5', 2)], reduce_concat=range(2, 6))
##36
SYNFLOW_ABS_seed2=Genotype(normal=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 0), ('avg_pool_3x3', 1), ('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('dil_conv_5x5', 0), ('sep_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 0), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3), ('max_pool_3x3', 1), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
##38
SYNFLOW_ABS_seed3=Genotype(normal=[('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2), ('max_pool_3x3', 2), ('sep_conv_5x5', 3), ('dil_conv_3x3', 0), ('avg_pool_3x3', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('max_pool_3x3', 1), ('avg_pool_3x3', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3), ('skip_connect', 0), ('dil_conv_5x5', 2)], reduce_concat=range(2, 6))
##40
SYNFLOW_ABS_seed4=Genotype(normal=[('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('dil_conv_5x5', 1), ('avg_pool_3x3', 2), ('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('dil_conv_5x5', 1), ('max_pool_3x3', 3)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('skip_connect', 0), ('dil_conv_5x5', 2), ('max_pool_3x3', 0), ('dil_conv_5x5', 3), ('dil_conv_5x5', 2), ('sep_conv_3x3', 4)], reduce_concat=range(2, 6))
##46
SYNFLOW_ABS_seed5=Genotype(normal=[('dil_conv_3x3', 0), ('dil_conv_5x5', 1), ('sep_conv_3x3', 0), ('dil_conv_5x5', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 3), ('dil_conv_5x5', 0), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 2), ('max_pool_3x3', 0), ('dil_conv_5x5', 3), ('dil_conv_5x5', 0), ('max_pool_3x3', 2)], reduce_concat=range(2, 6))
##36
SYNFLOW_ABS_seed6=Genotype(normal=[('dil_conv_5x5', 0), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('avg_pool_3x3', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 3), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('max_pool_3x3', 1), ('dil_conv_5x5', 2), ('max_pool_3x3', 1), ('dil_conv_3x3', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
###42
SYNFLOW_ABS_seed7=Genotype(normal=[('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_3x3', 0), ('max_pool_3x3', 2), ('dil_conv_5x5', 0), ('dil_conv_5x5', 3), ('dil_conv_5x5', 2), ('sep_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('skip_connect', 1), ('max_pool_3x3', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
##42
SYNFLOW_ABS_seed8=Genotype(normal=[('skip_connect', 0), ('dil_conv_3x3', 1), ('dil_conv_5x5', 1), ('dil_conv_5x5', 2), ('dil_conv_3x3', 0), ('dil_conv_5x5', 2), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 0), ('sep_conv_3x3', 1), ('dil_conv_3x3', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3), ('dil_conv_5x5', 2), ('sep_conv_3x3', 4)], reduce_concat=range(2, 6))
##40
SYNFLOW_ABS_seed9=Genotype(normal=[('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('dil_conv_3x3', 1), ('sep_conv_3x3', 2), ('dil_conv_5x5', 0), ('dil_conv_5x5', 2), ('sep_conv_5x5', 2), ('sep_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_3x3', 0), ('dil_conv_5x5', 2), ('dil_conv_3x3', 0), ('dil_conv_5x5', 3), ('skip_connect', 1), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
##36
SYNFLOW_ABS_seedX=Genotype(normal=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('dil_conv_5x5', 0), ('sep_conv_5x5', 3), ('dil_conv_5x5', 0), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('max_pool_3x3', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
###normal cell 2th,6th, reduct cell, 1
##1 5 9

SYNFLOW_ABS_FULL_seed0=Genotype(normal=[('skip_connect', 0), ('dil_conv_5x5', 1), ('dil_conv_3x3', 0), ('sep_conv_5x5', 2), ('sep_conv_5x5', 1), ('avg_pool_3x3', 3), ('dil_conv_5x5', 1), ('sep_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('sep_conv_5x5', 1), ('skip_connect', 0), ('max_pool_3x3', 2), ('sep_conv_3x3', 1), ('dil_conv_5x5', 2), ('max_pool_3x3', 2), ('max_pool_3x3', 4)], reduce_concat=range(2, 6))
SYNFLOW_ABS_FULL_seed1=Genotype(normal=[('sep_conv_3x3', 0), ('max_pool_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_5x5', 2), ('sep_conv_3x3', 0), ('max_pool_3x3', 1), ('sep_conv_5x5', 2), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('dil_conv_5x5', 0), ('sep_conv_3x3', 1), ('skip_connect', 1), ('avg_pool_3x3', 2), ('max_pool_3x3', 0), ('max_pool_3x3', 3), ('max_pool_3x3', 0), ('dil_conv_5x5', 2)], reduce_concat=range(2, 6))
SYNFLOW_ABS_FULL_seed2=Genotype(normal=[('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('skip_connect', 0), ('max_pool_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 0), ('skip_connect', 1), ('dil_conv_5x5', 0), ('dil_conv_5x5', 2), ('sep_conv_3x3', 2), ('dil_conv_5x5', 3), ('skip_connect', 1), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
SYNFLOW_ABS_FULL_seed3=Genotype(normal=[('dil_conv_3x3', 0), ('max_pool_3x3', 1), ('dil_conv_3x3', 0), ('dil_conv_5x5', 2), ('sep_conv_5x5', 2), ('sep_conv_5x5', 3), ('max_pool_3x3', 0), ('max_pool_3x3', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 1), ('dil_conv_3x3', 2), ('dil_conv_5x5', 2), ('max_pool_3x3', 3), ('max_pool_3x3', 0), ('dil_conv_5x5', 2)], reduce_concat=range(2, 6))
SYNFLOW_ABS_FULL_seed4=Genotype(normal=[('dil_conv_5x5', 0), ('avg_pool_3x3', 1), ('skip_connect', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 0), ('sep_conv_3x3', 1), ('max_pool_3x3', 1), ('sep_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('dil_conv_5x5', 1), ('sep_conv_5x5', 0), ('max_pool_3x3', 2), ('skip_connect', 0), ('dil_conv_5x5', 3), ('dil_conv_5x5', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
SYNFLOW_ABS_FULL_seed5=Genotype(normal=[('avg_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 0), ('avg_pool_3x3', 1), ('dil_conv_3x3', 0), ('avg_pool_3x3', 3), ('sep_conv_5x5', 0), ('sep_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 0), ('sep_conv_3x3', 2), ('skip_connect', 0), ('dil_conv_3x3', 3), ('skip_connect', 0), ('max_pool_3x3', 2)], reduce_concat=range(2, 6))
SYNFLOW_ABS_FULL_seed6=Genotype(normal=[('avg_pool_3x3', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('max_pool_3x3', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), ('sep_conv_3x3', 3), ('avg_pool_3x3', 4)], normal_concat=range(2, 6), reduce=[('dil_conv_5x5', 0), ('skip_connect', 1), ('skip_connect', 1), ('dil_conv_3x3', 2), ('skip_connect', 1), ('dil_conv_5x5', 2), ('sep_conv_3x3', 2), ('dil_conv_3x3', 4)], reduce_concat=range(2, 6))
SYNFLOW_ABS_FULL_seed7=Genotype(normal=[('avg_pool_3x3', 0), ('dil_conv_5x5', 1), ('max_pool_3x3', 0), ('dil_conv_3x3', 2), ('dil_conv_5x5', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 2), ('dil_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 0), ('sep_conv_3x3', 1), ('dil_conv_3x3', 1), ('sep_conv_5x5', 2), ('dil_conv_3x3', 0), ('skip_connect', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
SYNFLOW_ABS_FULL_seed8=Genotype(normal=[('dil_conv_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 1), ('max_pool_3x3', 2), ('max_pool_3x3', 0), ('dil_conv_5x5', 2), ('dil_conv_5x5', 0), ('max_pool_3x3', 2)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 1), ('avg_pool_3x3', 2), ('sep_conv_3x3', 2), ('dil_conv_3x3', 3), ('sep_conv_5x5', 2), ('dil_conv_3x3', 4)], reduce_concat=range(2, 6))
SYNFLOW_ABS_FULL_seed9=Genotype(normal=[('skip_connect', 0), ('dil_conv_5x5', 1), ('dil_conv_3x3', 1), ('sep_conv_3x3', 2), ('max_pool_3x3', 0), ('sep_conv_5x5', 2), ('sep_conv_3x3', 2), ('max_pool_3x3', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('avg_pool_3x3', 0), ('sep_conv_3x3', 2), ('skip_connect', 0), ('sep_conv_5x5', 3), ('sep_conv_3x3', 1), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
SYNFLOW_ABS_FULL_seedX=Genotype(normal=[('avg_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 0), ('sep_conv_5x5', 2), ('max_pool_3x3', 0), ('sep_conv_5x5', 2), ('sep_conv_3x3', 2), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 0), ('sep_conv_3x3', 2), ('skip_connect', 0), ('dil_conv_5x5', 3), ('dil_conv_5x5', 1), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
SYNFLOW_ABS_FULL_seedXI=Genotype(normal=[('avg_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2), ('sep_conv_3x3', 2), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 0), ('sep_conv_3x3', 2), ('skip_connect', 0), ('dil_conv_5x5', 3), ('dil_conv_5x5', 1), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
#
###normal cell 2th,5th,6th reduct cell, 4, 6, 7



SYNFLOW_ABS_imagenet_seed0=Genotype(normal=[('dil_conv_5x5', 0), ('max_pool_3x3', 1), ('dil_conv_5x5', 0), ('dil_conv_3x3', 2), ('sep_conv_5x5', 1), ('dil_conv_5x5', 3), ('dil_conv_3x3', 1), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 0), ('dil_conv_5x5', 2), ('skip_connect', 1), ('dil_conv_3x3', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
##40
SYNFLOW_ABS_imagenet_seed1=Genotype(normal=[('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('dil_conv_5x5', 0), ('dil_conv_3x3', 2), ('sep_conv_5x5', 0), ('dil_conv_5x5', 1), ('max_pool_3x3', 2), ('sep_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('dil_conv_5x5', 0), ('skip_connect', 1), ('skip_connect', 1), ('dil_conv_5x5', 2), ('skip_connect', 0), ('sep_conv_3x3', 3), ('avg_pool_3x3', 0), ('dil_conv_5x5', 2)], reduce_concat=range(2, 6))
##38
SYNFLOW_ABS_imagenet_seed2=Genotype(normal=[('dil_conv_5x5', 0), ('skip_connect', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('dil_conv_5x5', 0), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 0), ('dil_conv_3x3', 2), ('sep_conv_3x3', 2), ('dil_conv_5x5', 3), ('dil_conv_3x3', 1), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
##40
SYNFLOW_ABS_imagenet_seed3=Genotype(normal=[('avg_pool_3x3', 0), ('sep_conv_3x3', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3), ('dil_conv_5x5', 0), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('dil_conv_3x3', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3), ('avg_pool_3x3', 0), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))
##38
SYNFLOW_ABS_imagenet_seed4=Genotype(normal=[('dil_conv_3x3', 0), ('max_pool_3x3', 1), ('sep_conv_5x5', 1), ('max_pool_3x3', 2), ('dil_conv_5x5', 0), ('dil_conv_3x3', 1), ('sep_conv_5x5', 1), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('dil_conv_3x3', 0), ('dil_conv_3x3', 2), ('skip_connect', 0), ('dil_conv_5x5', 3), ('dil_conv_3x3', 2), ('avg_pool_3x3', 4)], reduce_concat=range(2, 6))
##40
SYNFLOW_ABS_imagenet_seed5=Genotype(normal=[('dil_conv_5x5', 0), ('avg_pool_3x3', 1), ('dil_conv_5x5', 0), ('max_pool_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_5x5', 3), ('sep_conv_5x5', 0), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 0), ('dil_conv_5x5', 2), ('skip_connect', 0), ('dil_conv_5x5', 3), ('skip_connect', 0), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))
##40
SYNFLOW_ABS_imagenet_seed6=Genotype(normal=[('dil_conv_5x5', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 3), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('dil_conv_3x3', 1), ('dil_conv_5x5', 2), ('avg_pool_3x3', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
##36
SYNFLOW_ABS_imagenet_seed7=Genotype(normal=[('dil_conv_3x3', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('sep_conv_3x3', 2), ('dil_conv_5x5', 0), ('sep_conv_5x5', 3), ('dil_conv_5x5', 2), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('sep_conv_3x3', 1), ('dil_conv_5x5', 2), ('skip_connect', 0), ('sep_conv_3x3', 1), ('dil_conv_5x5', 2), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))
##36
SYNFLOW_ABS_imagenet_seed8=Genotype(normal=[('sep_conv_5x5', 0), ('dil_conv_5x5', 1), ('avg_pool_3x3', 1), ('sep_conv_5x5', 2), ('dil_conv_3x3', 0), ('max_pool_3x3', 2), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('sep_conv_5x5', 1), ('dil_conv_5x5', 2), ('sep_conv_5x5', 2), ('dil_conv_5x5', 3), ('dil_conv_5x5', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
##38
SYNFLOW_ABS_imagenet_seed9=Genotype(normal=[('dil_conv_5x5', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 1), ('max_pool_3x3', 2), ('dil_conv_5x5', 0), ('max_pool_3x3', 2), ('sep_conv_5x5', 2), ('sep_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 0), ('dil_conv_5x5', 2), ('skip_connect', 0), ('dil_conv_5x5', 3), ('dil_conv_5x5', 1), ('dil_conv_3x3', 3)], reduce_concat=range(2, 6))
##36
SYNFLOW_ABS_imagenet_seedX=Genotype(normal=[('dil_conv_5x5', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 0), ('dil_conv_5x5', 3), ('dil_conv_5x5', 0), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 0), ('dil_conv_5x5', 2), ('skip_connect', 0), ('dil_conv_5x5', 3), ('dil_conv_5x5', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
###normal cell 4th,
##679


SYNFLOW_ABS_IMAGENET_FULL_seed0=Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 0), ('dil_conv_5x5', 2), ('sep_conv_5x5', 1), ('sep_conv_5x5', 3), ('sep_conv_3x3', 1), ('sep_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('dil_conv_3x3', 0), ('dil_conv_5x5', 2), ('sep_conv_5x5', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
SYNFLOW_ABS_IMAGENET_FULL_seed1=Genotype(normal=[('dil_conv_5x5', 0), ('max_pool_3x3', 1), ('sep_conv_5x5', 0), ('max_pool_3x3', 2), ('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 1), ('dil_conv_5x5', 2), ('skip_connect', 0), ('dil_conv_5x5', 3), ('skip_connect', 0), ('dil_conv_5x5', 2)], reduce_concat=range(2, 6))
SYNFLOW_ABS_IMAGENET_FULL_seed2=Genotype(normal=[('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('sep_conv_3x3', 1), ('dil_conv_5x5', 0), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('skip_connect', 1), ('dil_conv_3x3', 0), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3), ('skip_connect', 1), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
SYNFLOW_ABS_IMAGENET_FULL_seed3=Genotype(normal=[('avg_pool_3x3', 0), ('sep_conv_3x3', 1), ('dil_conv_3x3', 0), ('sep_conv_3x3', 2), ('dil_conv_3x3', 2), ('sep_conv_5x5', 3), ('skip_connect', 0), ('sep_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3), ('sep_conv_3x3', 0), ('dil_conv_3x3', 2)], reduce_concat=range(2, 6))
SYNFLOW_ABS_IMAGENET_FULL_seed4=Genotype(normal=[('avg_pool_3x3', 0), ('sep_conv_5x5', 1), ('avg_pool_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 0), ('max_pool_3x3', 2), ('sep_conv_5x5', 0), ('dil_conv_5x5', 3), ('max_pool_3x3', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
SYNFLOW_ABS_IMAGENET_FULL_seed5=Genotype(normal=[('dil_conv_3x3', 0), ('sep_conv_5x5', 1), ('max_pool_3x3', 0), ('dil_conv_5x5', 1), ('sep_conv_5x5', 0), ('dil_conv_5x5', 3), ('sep_conv_3x3', 0), ('max_pool_3x3', 3)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 0), ('skip_connect', 1), ('skip_connect', 0), ('dil_conv_5x5', 2), ('sep_conv_5x5', 0), ('dil_conv_5x5', 3), ('skip_connect', 0), ('dil_conv_5x5', 2)], reduce_concat=range(2, 6))
SYNFLOW_ABS_IMAGENET_FULL_seed6=Genotype(normal=[('sep_conv_5x5', 0), ('max_pool_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('skip_connect', 1), ('sep_conv_5x5', 2), ('sep_conv_5x5', 3), ('max_pool_3x3', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 1), ('dil_conv_5x5', 2), ('skip_connect', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
SYNFLOW_ABS_IMAGENET_FULL_seed7=Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2), ('sep_conv_3x3', 0), ('sep_conv_5x5', 3), ('sep_conv_5x5', 2), ('dil_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('sep_conv_3x3', 1), ('dil_conv_5x5', 2), ('skip_connect', 0), ('skip_connect', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
SYNFLOW_ABS_IMAGENET_FULL_seed8=Genotype(normal=[('sep_conv_5x5', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), ('sep_conv_5x5', 0), ('max_pool_3x3', 2), ('dil_conv_3x3', 0), ('max_pool_3x3', 2)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('avg_pool_3x3', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3), ('dil_conv_5x5', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
SYNFLOW_ABS_IMAGENET_FULL_seed9=Genotype(normal=[('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('avg_pool_3x3', 1), ('max_pool_3x3', 2), ('max_pool_3x3', 0), ('dil_conv_5x5', 2), ('sep_conv_5x5', 2), ('sep_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 0), ('dil_conv_5x5', 2), ('skip_connect', 0), ('dil_conv_5x5', 3), ('skip_connect', 1), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
SYNFLOW_ABS_IMAGENET_FULL_seedX=Genotype(normal=[('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 2), ('sep_conv_5x5', 0), ('sep_conv_5x5', 3), ('skip_connect', 0), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))

###normal cell 4th,7
##68





####test

SYNFLOW_full_imagenet_seed0=Genotype(
    normal=[
    ('dil_conv_5x5', 0), ('sep_conv_5x5', 1), 
    ('avg_pool_3x3', 0), ('max_pool_3x3', 2), 
    ('sep_conv_5x5', 1), ('sep_conv_5x5', 3), 
    ('sep_conv_5x5', 1), ('sep_conv_3x3', 4)], 
    normal_concat=range(2, 6), reduce=[
    ('dil_conv_3x3', 0), ('max_pool_3x3', 1), 
    ('dil_conv_5x5', 0), ('max_pool_3x3', 2), 
    ('sep_conv_3x3', 1), ('sep_conv_5x5', 2), 
    ('dil_conv_3x3', 2), ('sep_conv_3x3', 4)], 
    reduce_concat=range(2, 6))

SYNFLOW_full_imagenet_seed1=Genotype(
    normal=[
    ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), 
    ('sep_conv_5x5', 0), ('max_pool_3x3', 2), 
    ('avg_pool_3x3', 0), ('sep_conv_5x5', 1), 
    ('avg_pool_3x3', 2), ('max_pool_3x3', 3)], 
    normal_concat=range(2, 6), reduce=[
    ('sep_conv_5x5', 0), ('sep_conv_5x5', 1), 
    ('avg_pool_3x3', 1), ('skip_connect', 2), 
    ('sep_conv_5x5', 0), ('avg_pool_3x3', 3), 
    ('sep_conv_5x5', 0), ('sep_conv_3x3', 2)], 
    reduce_concat=range(2, 6))


SYNFLOW_full_imagenet_seed2=Genotype(
    normal=[
    ('sep_conv_3x3', 0), ('skip_connect', 1), 
    ('sep_conv_5x5', 0), ('dil_conv_3x3', 1), 
    ('dil_conv_5x5', 0), ('dil_conv_3x3', 1), 
    ('dil_conv_3x3', 0), ('sep_conv_5x5', 3)], 
    normal_concat=range(2, 6), reduce=[
    ('sep_conv_3x3', 0), ('avg_pool_3x3', 1), 
    ('sep_conv_3x3', 0), ('dil_conv_3x3', 2), 
    ('max_pool_3x3', 2), ('avg_pool_3x3', 3), 
    ('dil_conv_3x3', 1), ('avg_pool_3x3', 3)], 
    reduce_concat=range(2, 6))

SYNFLOW_full_imagenet_seed3=Genotype(
    normal=[
    ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), 
    ('skip_connect', 0), ('sep_conv_3x3', 2), 
    ('avg_pool_3x3', 2), ('avg_pool_3x3', 3), 
    ('sep_conv_5x5', 0), ('sep_conv_3x3', 3)], 
    normal_concat=range(2, 6), reduce=[
    ('avg_pool_3x3', 0), ('dil_conv_3x3', 1), 
    ('sep_conv_5x5', 1), ('max_pool_3x3', 2), 
    ('dil_conv_5x5', 2), ('max_pool_3x3', 3), 
    ('max_pool_3x3', 0), ('max_pool_3x3', 2)], 
    reduce_concat=range(2, 6))

SYNFLOW_full_imagenet_seed4=Genotype(
    normal=[
    ('sep_conv_3x3', 0), ('dil_conv_5x5', 1), 
    ('avg_pool_3x3', 1), ('dil_conv_5x5', 2), 
    ('max_pool_3x3', 0), ('dil_conv_5x5', 1), 
    ('dil_conv_3x3', 1), ('sep_conv_5x5', 3)], 
    normal_concat=range(2, 6), reduce=[
    ('dil_conv_3x3', 0), ('dil_conv_3x3', 1), 
    ('dil_conv_3x3', 0), ('avg_pool_3x3', 2), 
    ('avg_pool_3x3', 0), ('dil_conv_5x5', 3), 
    ('avg_pool_3x3', 2), ('avg_pool_3x3', 4)], 
    reduce_concat=range(2, 6))

SYNFLOW_full_imagenet_seed5=Genotype(
    normal=[
    ('dil_conv_5x5', 0), ('max_pool_3x3', 1), 
    ('avg_pool_3x3', 0), ('max_pool_3x3', 1), 
    ('sep_conv_5x5', 0), ('dil_conv_5x5', 3), 
    ('dil_conv_5x5', 0), ('sep_conv_5x5', 3)], 
    normal_concat=range(2, 6), reduce=[
    ('sep_conv_5x5', 0), ('dil_conv_5x5', 1), 
    ('dil_conv_3x3', 0), ('avg_pool_3x3', 2), 
    ('sep_conv_5x5', 0), ('sep_conv_3x3', 3), 
    ('sep_conv_5x5', 0), ('max_pool_3x3', 2)], 
    reduce_concat=range(2, 6))

SYNFLOW_full_imagenet_seed6=Genotype(
    normal=[
    ('dil_conv_5x5', 0), ('sep_conv_5x5', 1), 
    ('max_pool_3x3', 0), ('sep_conv_5x5', 1), 
    ('max_pool_3x3', 1), ('sep_conv_5x5', 2), 
    ('sep_conv_5x5', 3), ('sep_conv_5x5', 4)], 
    normal_concat=range(2, 6), reduce=[
    ('sep_conv_5x5', 0), ('none', 1), 
    ('dil_conv_3x3', 1), ('max_pool_3x3', 2), 
    ('dil_conv_3x3', 1), ('avg_pool_3x3', 2), 
    ('sep_conv_5x5', 2), ('sep_conv_5x5', 4)], 
    reduce_concat=range(2, 6))

SYNFLOW_full_imagenet_seed7=Genotype(
    normal=[
    ('skip_connect', 0), ('sep_conv_3x3', 1), 
    ('dil_conv_5x5', 0), ('avg_pool_3x3', 2), 
    ('sep_conv_3x3', 0), ('max_pool_3x3', 3), 
    ('avg_pool_3x3', 2), ('max_pool_3x3', 4)], 
    normal_concat=range(2, 6), reduce=[
    ('sep_conv_3x3', 0), ('avg_pool_3x3', 1), 
    ('sep_conv_3x3', 1), ('dil_conv_3x3', 2), 
    ('dil_conv_5x5', 0), ('sep_conv_3x3', 1), 
    ('avg_pool_3x3', 2), ('max_pool_3x3', 3)], 
    reduce_concat=range(2, 6))

SYNFLOW_full_imagenet_seed8=Genotype(
    normal=[
    ('sep_conv_5x5', 0), ('sep_conv_5x5', 1), 
    ('max_pool_3x3', 1), ('sep_conv_5x5', 2), 
    ('max_pool_3x3', 0), ('dil_conv_3x3', 2), 
    ('dil_conv_3x3', 0), ('sep_conv_3x3', 2)], 
    normal_concat=range(2, 6), reduce=[
    ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), 
    ('skip_connect', 1), ('dil_conv_5x5', 2), 
    ('sep_conv_3x3', 2), ('sep_conv_5x5', 3), 
    ('dil_conv_5x5', 2), ('max_pool_3x3', 4)], 
    reduce_concat=range(2, 6))

SYNFLOW_full_imagenet_seed9=Genotype(
    normal=[
    ('dil_conv_5x5', 0), ('dil_conv_3x3', 1), 
    ('dil_conv_5x5', 1), ('sep_conv_5x5', 2), 
    ('max_pool_3x3', 0), ('sep_conv_3x3', 2), 
    ('sep_conv_3x3', 2), ('sep_conv_3x3', 4)], 
    normal_concat=range(2, 6), reduce=[
    ('sep_conv_5x5', 0), ('avg_pool_3x3', 1), 
    ('sep_conv_5x5', 0), ('dil_conv_3x3', 2), 
    ('max_pool_3x3', 0), ('max_pool_3x3', 3), 
    ('sep_conv_5x5', 1), ('avg_pool_3x3', 3)], 
    reduce_concat=range(2, 6))



SYNFLOW_seed0 = Genotype(
	normal=[
	('max_pool_3x3', 0), ('skip_connect', 1), 
	('sep_conv_5x5', 0), ('max_pool_3x3', 2), 
	('sep_conv_5x5', 1), ('dil_conv_3x3', 3), 
	('sep_conv_5x5', 1), ('sep_conv_3x3', 4)], 
	normal_concat=range(2, 6), reduce=[
	('skip_connect', 0), ('avg_pool_3x3', 1), 
	('sep_conv_3x3', 0), ('sep_conv_3x3', 2), 
	('max_pool_3x3', 1), ('avg_pool_3x3', 2), 
	('avg_pool_3x3', 2), ('sep_conv_3x3', 4)], 
	reduce_concat=range(2, 6))
#########initial chanel 50 for imagenet



SYNFLOW_seed1 = Genotype(
	normal=[
	('sep_conv_5x5', 0), ('dil_conv_5x5', 1), 
	('sep_conv_3x3', 0), ('sep_conv_5x5', 2), 
	('max_pool_3x3', 0), ('dil_conv_5x5', 1), 
	('sep_conv_3x3', 2), ('dil_conv_5x5', 3)], 
	normal_concat=range(2, 6), reduce=[
	('dil_conv_3x3', 0), ('max_pool_3x3', 1), 
	('dil_conv_3x3', 1), ('avg_pool_3x3', 2), 
	('avg_pool_3x3', 0), ('sep_conv_5x5', 3), 
	('skip_connect', 0), ('sep_conv_5x5', 2)], 
reduce_concat=range(2, 6))
########initial chanel 48 for imagenet


SYNFLOW_seed2 = Genotype(
	normal=[
	('sep_conv_3x3', 0), ('skip_connect', 1), 
	('dil_conv_5x5', 0), ('skip_connect', 1), 
	('skip_connect', 0), ('max_pool_3x3', 1), 
	('sep_conv_3x3', 0), ('sep_conv_3x3', 3)], 
	normal_concat=range(2, 6), 
	reduce=[
	('sep_conv_3x3', 0), ('max_pool_3x3', 1), 
	('dil_conv_5x5', 0), ('max_pool_3x3', 2), 
	('max_pool_3x3', 2), ('max_pool_3x3', 3), 
	('sep_conv_3x3', 1), ('sep_conv_5x5', 3)], 
	reduce_concat=range(2, 6))#########initial chanel 54 for imagenet
	
	
SYNFLOW_seed3 = Genotype(
	normal=[
	('sep_conv_5x5', 0), ('dil_conv_3x3', 1), 
	('dil_conv_5x5', 0), ('sep_conv_3x3', 2), 
	('max_pool_3x3', 2), ('dil_conv_3x3', 3), 
	('avg_pool_3x3', 0), ('avg_pool_3x3', 3)], 
	normal_concat=range(2, 6), reduce=[
	('dil_conv_5x5', 0), ('dil_conv_3x3', 1), 
	('dil_conv_3x3', 1), ('sep_conv_5x5', 2), 
	('sep_conv_5x5', 2), ('sep_conv_5x5', 3), 
	('dil_conv_3x3', 0), ('sep_conv_5x5', 2)], 
	reduce_concat=range(2, 6))
#####initial chanel 52 for imagenet

SYNFLOW_seed4 = Genotype(
	normal=[
	('sep_conv_5x5', 0), ('dil_conv_3x3', 1), 
	('sep_conv_5x5', 1), ('sep_conv_5x5', 2), 
	('avg_pool_3x3', 0), ('none', 1), 
	('max_pool_3x3', 1), ('dil_conv_5x5', 3)], 
	normal_concat=range(2, 6), reduce=[
	('max_pool_3x3', 0), ('sep_conv_5x5', 1), 
	('skip_connect', 0), ('sep_conv_5x5', 2), 
	('skip_connect', 0), ('avg_pool_3x3', 3), 
	('dil_conv_5x5', 2), ('sep_conv_3x3', 4)], 
	reduce_concat=range(2, 6))
#####initial chanel 52 for imagenet, 617

SYNFLOW_seed5 = Genotype(
	normal=[
	('sep_conv_3x3', 0), ('sep_conv_5x5', 1), 
	('sep_conv_3x3', 0), ('dil_conv_3x3', 1), 
	('skip_connect', 0), ('avg_pool_3x3', 3), 
	('dil_conv_5x5', 0), ('avg_pool_3x3', 3)], 
	normal_concat=range(2, 6), reduce=[
	('max_pool_3x3', 0), ('skip_connect', 1), 
	('avg_pool_3x3', 0), ('dil_conv_3x3', 2), 
	('max_pool_3x3', 0), ('avg_pool_3x3', 3), 
	('skip_connect', 0), ('sep_conv_3x3', 2)], 
	reduce_concat=range(2, 6))
#####initial chanel 52 for imagenet

SYNFLOW_seed6 = Genotype(
    normal=[
    ('max_pool_3x3', 0), ('sep_conv_3x3', 1), 
    ('max_pool_3x3', 0), ('dil_conv_3x3', 1), 
    ('dil_conv_5x5', 1), ('max_pool_3x3', 2), 
    ('avg_pool_3x3', 3), ('dil_conv_3x3', 4)], 
    normal_concat=range(2, 6), reduce=[
    ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), 
    ('sep_conv_5x5', 1), ('max_pool_3x3', 2), 
    ('sep_conv_3x3', 1), ('sep_conv_5x5', 2), 
    ('sep_conv_3x3', 2), ('sep_conv_3x3', 4)], 
    reduce_concat=range(2, 6))
##44,3.8
SYNFLOW_seed7 = Genotype(
    normal=[
    ('avg_pool_3x3', 0), ('dil_conv_5x5', 1), 
    ('dil_conv_3x3', 0), ('sep_conv_5x5', 2), 
    ('dil_conv_5x5', 0), ('sep_conv_3x3', 3), 
    ('sep_conv_3x3', 2), ('none', 4)], 
    normal_concat=range(2, 6), reduce=[
    ('dil_conv_3x3', 0), ('dil_conv_3x3', 1), 
    ('sep_conv_3x3', 1), ('sep_conv_5x5', 2), 
    ('skip_connect', 0), ('avg_pool_3x3', 1), 
    ('avg_pool_3x3', 2), ('sep_conv_3x3', 3)], 
    reduce_concat=range(2, 6))
##38,3.7

SYNFLOW_seed8 = Genotype(
    normal=[
    ('max_pool_3x3', 0), ('sep_conv_5x5', 1), 
    ('dil_conv_5x5', 1), ('sep_conv_5x5', 2), 
    ('dil_conv_3x3', 0), ('dil_conv_3x3', 2), 
    ('dil_conv_3x3', 0), ('sep_conv_5x5', 2)], 
    normal_concat=range(2, 6), reduce=[
    ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), 
    ('avg_pool_3x3', 1), ('avg_pool_3x3', 2), 
    ('dil_conv_3x3', 2), ('max_pool_3x3', 3), 
    ('max_pool_3x3', 2), ('sep_conv_3x3', 4)], 
    reduce_concat=range(2, 6))
###36,3.5, 38,3.9

SYNFLOW_seed9 = Genotype(normal=[
    ('dil_conv_5x5', 0), ('sep_conv_3x3', 1), 
    ('avg_pool_3x3', 1), ('dil_conv_5x5', 2), 
    ('sep_conv_3x3', 0), ('max_pool_3x3', 2), 
    ('sep_conv_3x3', 2), ('avg_pool_3x3', 4)], 
    normal_concat=range(2, 6), reduce=[
    ('dil_conv_3x3', 0), ('dil_conv_3x3', 1), 
    ('avg_pool_3x3', 0), ('max_pool_3x3', 2), 
    ('sep_conv_5x5', 0), ('dil_conv_5x5', 3), 
    ('skip_connect', 1), ('sep_conv_3x3', 3)], 
    reduce_concat=range(2, 6))
###40,3.8, 38,3.4


SYNFLOW_new_seed0 = Genotype(normal=[
    ('max_pool_3x3', 0), ('skip_connect', 1), 
    ('sep_conv_3x3', 0), ('max_pool_3x3', 2), 
    ('dil_conv_5x5', 1), ('dil_conv_3x3', 3), 
    ('sep_conv_5x5', 1), ('sep_conv_3x3', 4)], 
    normal_concat=range(2, 6), reduce=[
    ('max_pool_3x3', 0), ('sep_conv_3x3', 1), 
    ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), 
    ('max_pool_3x3', 1), ('max_pool_3x3', 2), 
    ('avg_pool_3x3', 2), ('sep_conv_3x3', 4)], 
    reduce_concat=range(2, 6))

SYNFLOW_new_seed1 = Genotype(normal=[
    ('sep_conv_5x5', 0), ('skip_connect', 1), 
    ('sep_conv_3x3', 0), ('dil_conv_5x5', 2), 
    ('max_pool_3x3', 0), ('dil_conv_3x3', 1), 
    ('sep_conv_3x3', 2), ('dil_conv_5x5', 3)], 
    normal_concat=range(2, 6), reduce=[
    ('sep_conv_5x5', 0), ('max_pool_3x3', 1), 
    ('dil_conv_3x3', 1), ('avg_pool_3x3', 2), 
    ('avg_pool_3x3', 0), ('skip_connect', 3), 
    ('skip_connect', 0), ('sep_conv_5x5', 2)], 
    reduce_concat=range(2, 6))

SYNFLOW_new_seed2 = Genotype(normal=[
    ('sep_conv_3x3', 0), ('skip_connect', 1), 
    ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), 
    ('skip_connect', 0), ('avg_pool_3x3', 1), 
    ('sep_conv_3x3', 0), ('sep_conv_3x3', 3)], 
    normal_concat=range(2, 6), reduce=[
    ('sep_conv_5x5', 0), ('max_pool_3x3', 1), 
    ('dil_conv_5x5', 0), ('sep_conv_5x5', 2), 
    ('max_pool_3x3', 2), ('max_pool_3x3', 3), 
    ('sep_conv_3x3', 1), ('sep_conv_5x5', 3)], 
    reduce_concat=range(2, 6))

SYNFLOW_new_seed3 = Genotype(normal=[
    ('sep_conv_5x5', 0), ('dil_conv_3x3', 1), 
    ('dil_conv_5x5', 0), ('sep_conv_3x3', 2), 
    ('max_pool_3x3', 2), ('dil_conv_3x3', 3), 
    ('avg_pool_3x3', 0), ('avg_pool_3x3', 3)], 
    normal_concat=range(2, 6), reduce=[
    ('dil_conv_5x5', 0), ('avg_pool_3x3', 1), 
    ('avg_pool_3x3', 1), ('sep_conv_5x5', 2), 
    ('sep_conv_5x5', 2), ('avg_pool_3x3', 3), 
    ('avg_pool_3x3', 0), ('max_pool_3x3', 2)], 
    reduce_concat=range(2, 6))

SYNFLOW_new_seed4 = Genotype(normal=[
    ('sep_conv_5x5', 0), ('dil_conv_3x3', 1), 
    ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), 
    ('avg_pool_3x3', 0), ('none', 1), 
    ('sep_conv_3x3', 1), ('sep_conv_5x5', 3)], 
    normal_concat=range(2, 6), reduce=[
    ('max_pool_3x3', 0), ('sep_conv_5x5', 1), 
    ('skip_connect', 0), ('sep_conv_5x5', 2), 
    ('max_pool_3x3', 0), ('avg_pool_3x3', 3), 
    ('dil_conv_5x5', 2), ('sep_conv_3x3', 4)], 
    reduce_concat=range(2, 6))

SYNFLOW_new_seed5 = Genotype(normal=[
    ('sep_conv_3x3', 0), ('sep_conv_5x5', 1), 
    ('sep_conv_5x5', 0), ('dil_conv_3x3', 1), 
    ('avg_pool_3x3', 0), ('sep_conv_5x5', 3), 
    ('avg_pool_3x3', 0), ('dil_conv_5x5', 3)], 
    normal_concat=range(2, 6), reduce=[
    ('sep_conv_3x3', 0), ('skip_connect', 1), 
    ('avg_pool_3x3', 0), ('avg_pool_3x3', 2), 
    ('skip_connect', 0), ('avg_pool_3x3', 3), 
    ('skip_connect', 0), ('sep_conv_3x3', 2)], 
    reduce_concat=range(2, 6))

SYNFLOW_new_seed6 = Genotype(normal=[
    ('max_pool_3x3', 0), ('sep_conv_3x3', 1), 
    ('max_pool_3x3', 0), ('avg_pool_3x3', 1), 
    ('dil_conv_3x3', 1), ('max_pool_3x3', 2), 
    ('avg_pool_3x3', 3), ('dil_conv_3x3', 4)], 
    normal_concat=range(2, 6), reduce=[
    ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), 
    ('sep_conv_5x5', 1), ('avg_pool_3x3', 2), 
    ('avg_pool_3x3', 1), ('sep_conv_5x5', 2), 
    ('sep_conv_3x3', 2), ('sep_conv_3x3', 4)], 
    reduce_concat=range(2, 6))

SYNFLOW_new_seed7 = Genotype(normal=[
    ('max_pool_3x3', 0), ('sep_conv_5x5', 1), 
    ('dil_conv_3x3', 0), ('max_pool_3x3', 2), 
    ('dil_conv_3x3', 0), ('sep_conv_3x3', 3), 
    ('sep_conv_3x3', 2), ('dil_conv_3x3', 4)], 
    normal_concat=range(2, 6), reduce=[
    ('max_pool_3x3', 0), ('skip_connect', 1), 
    ('dil_conv_5x5', 1), ('sep_conv_5x5', 2), 
    ('dil_conv_5x5', 0), ('dil_conv_5x5', 1), 
    ('dil_conv_3x3', 2), ('sep_conv_3x3', 3)], 
    reduce_concat=range(2, 6))

SYNFLOW_new_seed8 = Genotype(normal=[
    ('max_pool_3x3', 0), ('sep_conv_5x5', 1), 
    ('dil_conv_3x3', 1), ('sep_conv_3x3', 2), 
    ('dil_conv_3x3', 0), ('sep_conv_5x5', 2), 
    ('dil_conv_3x3', 0), ('max_pool_3x3', 2)], 
    normal_concat=range(2, 6), reduce=[
    ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), 
    ('avg_pool_3x3', 1), ('sep_conv_5x5', 2), 
    ('dil_conv_3x3', 2), ('max_pool_3x3', 3), 
    ('sep_conv_5x5', 2), ('sep_conv_3x3', 4)], 
    reduce_concat=range(2, 6))
###38,50



SYNFLOW_new_seed9 = Genotype(normal=[
    ('dil_conv_5x5', 0), ('dil_conv_5x5', 1), 
    ('sep_conv_5x5', 1), ('avg_pool_3x3', 2), 
    ('sep_conv_3x3', 0), ('max_pool_3x3', 2), 
    ('sep_conv_3x3', 2), ('avg_pool_3x3', 4)], 
    normal_concat=range(2, 6), reduce=[
    ('max_pool_3x3', 0), ('dil_conv_3x3', 1), 
    ('avg_pool_3x3', 0), ('sep_conv_3x3', 2), 
    ('sep_conv_5x5', 0), ('dil_conv_5x5', 3), 
    ('sep_conv_3x3', 1), ('sep_conv_5x5', 3)], 
    reduce_concat=range(2, 6))
#######trade-off 6e-4
SYNFLOW_abs_imagenet_seed0=Genotype(normal=[('dil_conv_5x5', 0), ('avg_pool_3x3', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2), ('sep_conv_3x3', 1), ('sep_conv_5x5', 3), ('sep_conv_3x3', 1), ('dil_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 0), ('dil_conv_5x5', 2), ('avg_pool_3x3', 1), ('dil_conv_3x3', 2), ('dil_conv_5x5', 2), ('dil_conv_3x3', 4)], reduce_concat=range(2, 6))
##36,48
SYNFLOW_abs_imagenet_seed1=Genotype(normal=[('dil_conv_5x5', 0), ('dil_conv_3x3', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2), ('sep_conv_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_5x5', 2), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('dil_conv_3x3', 1), ('dil_conv_5x5', 2), ('skip_connect', 0), ('dil_conv_5x5', 3), ('dil_conv_3x3', 0), ('dil_conv_5x5', 2)], reduce_concat=range(2, 6))
##36,48
SYNFLOW_abs_imagenet_seed2=Genotype(normal=[('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('avg_pool_3x3', 1), ('dil_conv_5x5', 0), ('sep_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 0), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3), ('sep_conv_5x5', 1), ('dil_conv_3x3', 3)], reduce_concat=range(2, 6))
##36,48
SYNFLOW_abs_imagenet_seed3=Genotype(normal=[('dil_conv_5x5', 0), ('dil_conv_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 2), ('sep_conv_5x5', 2), ('dil_conv_3x3', 3), ('dil_conv_5x5', 0), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3), ('dil_conv_3x3', 0), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))
##36,48
SYNFLOW_abs_imagenet_seed4=Genotype(normal=[('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('dil_conv_3x3', 1), ('sep_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 2), ('sep_conv_3x3', 0), ('dil_conv_5x5', 3), ('dil_conv_5x5', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
##34,46
SYNFLOW_abs_imagenet_seed5=Genotype(normal=[('dil_conv_5x5', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 0), ('dil_conv_3x3', 3), ('sep_conv_3x3', 0), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('skip_connect', 1), ('skip_connect', 0), ('dil_conv_3x3', 2), ('sep_conv_5x5', 0), ('dil_conv_5x5', 3), ('dil_conv_3x3', 0), ('dil_conv_5x5', 2)], reduce_concat=range(2, 6))
##36,48
SYNFLOW_abs_imagenet_seed6=Genotype(normal=[('dil_conv_5x5', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 0), ('dil_conv_3x3', 1), ('dil_conv_3x3', 1), ('sep_conv_5x5', 2), ('sep_conv_5x5', 3), ('max_pool_3x3', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 1), ('dil_conv_5x5', 2), ('skip_connect', 1), ('dil_conv_3x3', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
##36,48
SYNFLOW_abs_imagenet_seed7=Genotype(normal=[('sep_conv_3x3', 0), ('dil_conv_5x5', 1), ('dil_conv_3x3', 0), ('dil_conv_5x5', 2), ('dil_conv_5x5', 0), ('dil_conv_5x5', 3), ('sep_conv_3x3', 2), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 1), ('dil_conv_5x5', 2), ('skip_connect', 0), ('sep_conv_3x3', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
##38,50
SYNFLOW_abs_imagenet_seed8=Genotype(normal=[('dil_conv_5x5', 0), ('dil_conv_5x5', 1), ('max_pool_3x3', 1), ('sep_conv_3x3', 2), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2), ('sep_conv_5x5', 0), ('max_pool_3x3', 2)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('avg_pool_3x3', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_3x3', 3), ('dil_conv_5x5', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
##38,50
SYNFLOW_new_abs_imagenet_seed9=Genotype(normal=[('dil_conv_5x5', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 1), ('max_pool_3x3', 2), ('dil_conv_5x5', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 2), ('sep_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('max_pool_3x3', 0), ('dil_conv_5x5', 2), ('skip_connect', 0), ('dil_conv_5x5', 3), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3)], reduce_concat=range(2, 6))
##36,48
