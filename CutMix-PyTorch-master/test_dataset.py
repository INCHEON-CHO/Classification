import torchvision
import torch

#cifar = torchvision.datasets.CIFAR10('../data',train=True,download=False)
#print(cifar.__getitem__(1))

imagenet = torchvision.datasets.ImageNet('../imagenet/train',split='train',download=True)
