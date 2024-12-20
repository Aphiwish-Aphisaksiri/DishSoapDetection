# DishSoapDetection
This repository is created for the dish soap detection project. The project is a part of the course "Deep Learning for Computer Vision" at the Mahidol university. The goal of the project is to detect the dish soap bottle in the supermarket. The project is implemented using the YOLOv11 object detection model. 

The Requirements for the project are:
- Python 3.11.10
- Pytorch 2.0.0+cu118
- torchvision 0.15.1+cu118
- Ultralytics 8.3.33

Conda is highly recommended for the installation of the requirements. The following command can be used to create a new conda environment with the required packages:
```
conda create -n dish_soap_detection python=3.11.10
conda activate dish_soap_detection
pip install torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.0+cu118 --index-url https://download.pytorch.org/whl/cu118
pip install ultralytics
```

The dataset used for this project is stored in https://app.roboflow.com/image-processing-egbi/image-processing-class/models

