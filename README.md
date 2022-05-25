>📋  A README.md for code accompanying paper

# Differentiable Architecture Search Meets Network Pruning at Initialization: A More Reliable, Efficient, and Flexible Framework

This repository is the implementation of Differentiable Architecture Search Meets Network Pruning at Initialization: A More Reliable, Efficient, and Flexible Framework. 


## Requirements

To install requirements:

```setup
Following DARTS and NAS-Bench-201 install requirements, download NAS-Bench-201-v1_1-096897.pth from https://drive.google.com/file/d/16Y0UwGisiouVRxW-W5hEtbxmcHw_0hF_/view
```


## Search on NAS-Bench-201

The reproducible codes could be found in NAS_Bench201/exps/algos/FreeDARTS_Synflow_oneshot.ipynb


## Search on DARTS space

The codes for FreeDARTS could be found in DARTS_CNN/FreeDARTS_Synflow_oneshot.ipynb

The codes FOR FreeDARTS$\dagger$ could be found in DARTS_CNN/FreeDARTS_Synflow_oneshot_20cells.ipynb

The codes FOR FreeDARTS$\ddagger$ could be found in DARTS_CNN/FreeDARTS_Synflow_ImageNet_oneshot.ipynb


## Searched architectures

The searched architectures with 5 different seeds can be found in the DARTS_CNN/genotypes.py


## Pre-trained Models

You can get pretrained models and log files in DARTS_CNN/trained_models


## Results on DARTS space

Our model achieves the following performance on :

### Image Classification on CIFAR

| Model name         | CIFAR-10 Error  | CIFAR-100 Error|
| ------------------ |---------------- | -------------- |
| FreeDARTS          |     2.73%       |      18.03%    |
| ------------------ |---------------- | -------------- |
| FreeDARTS$\dagger$ |     2.45%       |      17.08%    |
| ------------------ |---------------- | -------------- |
| FreeDARTS$\ddagger$|     2.64%       |      16.35%    |



### Image Classification on ImageNet

| Model name         | Top 1 Error     | Top 5 Error    |
| ------------------ |---------------- | -------------- |
| FreeDARTS          |     26.1%       |       8.2%     |
| ------------------ |---------------- | -------------- |
| FreeDARTS$\dagger$ |     25.4%       |       7.8%     |
| ------------------ |---------------- | -------------- |
| FreeDARTS$\ddagger$|     24.4%       |       7.3%     |


## Results on MobileNet space

The retrained results of the seached architecture can be found in mobilenet_space/mobilenet/retrain_architecture/eval-eval_models/logs

| Model name         | Top 1 Error     | Top 5 Error    |
| ------------------ |---------------- | -------------- |
| FreeDARTS$\ddagger$|     23.6%       |       6.9%     |
