# Authors: Akshay (github.com/aksh-ai) and GitHub Copilot

def binary_search(arr, key):
    '''
    Perform binary search over the given array using the key and return the index of the element
    '''
    if len(arr) == 0:
        return -1
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def create_vgg16_model_using_pytorch():
    '''
    Create VGG16 model using pytorch
    '''
    import torch.nn as nn
    from torchvision import models
    model = models.vgg16(pretrained=True)
    model.classifier = nn.Sequential(
        nn.Linear(512 * 7 * 7, 4096),
        nn.ReLU(True),
        nn.Dropout(),
        nn.Linear(4096, 4096),
        nn.ReLU(True),
        nn.Dropout(),
        nn.Linear(4096, 2),
    )
    return model

if __name__ == '__main__':
    # print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 7))
    print(create_vgg16_model_using_pytorch())
    exit()