import torch
import os


def download_process_data(path="colab_demo"):
    os.makedirs(path, exist_ok=True)
    print("Downloading data")
    torch.hub.download_url_to_file('https://heibox.uni-heidelberg.de/f/b95206528f384185889b/?dl=1', os.path.join(path, 'lsun_bedroom.pth'))
    torch.hub.download_url_to_file('https://heibox.uni-heidelberg.de/f/0701aac3aa69457bbe34/?dl=1', os.path.join(path, 'lsun_cat.pth'))
    torch.hub.download_url_to_file('https://heibox.uni-heidelberg.de/f/44ccb50ef3c6436db52e/?dl=1', os.path.join(path, 'lsun_church.pth'))
    print("Data downloaded")
