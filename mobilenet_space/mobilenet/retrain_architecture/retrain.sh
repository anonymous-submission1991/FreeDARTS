#!/bin/bash
python -m torch.distributed.launch --nproc_per_node=1 retrain.py --save='eval_models' --model_id='-1 3 1 3 3 1 3 2 1 3 2 1 3 3 1 2 1 3 -1 3 1'

python -m torch.distributed.launch --nproc_per_node=1 retrain.py --save='eval_models' --model_id='0 2 0 4 2 3 3 4 4 3 4 4 3 3 5 1 0 4 3 0 2'

python -m torch.distributed.launch --nproc_per_node=1 retrain.py --save='eval_models' --model_id='5 4 0 1 2 5 3 0 0 3 0 4 4 0 4 2 4 5 4 0 1'


python -m torch.distributed.launch --nproc_per_node=1 retrain.py --save='eval_models' --model_id='0 2 0 4 2 3 -1 4 4 3 4 4 -1 3 5 1 0 4 3 0 2'
