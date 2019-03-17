# Final_Prj

## Dataset
Download flickr images by texts, flickr.walk [flickr api usage](https://www.flickr.com/services/api/)  
[google cloud](https://drive.google.com/drive/folders/1q252qzRZGE5iWlCLZwn1mJfajVxk7I22?usp=sharing)  
flower & flower in vase 1500  
watercolor flower 1500  
自然图像和水彩画花下载下来的图像构图方面并不是很契合，自然图像很多花朵大特写，水彩画多是群花，GAN学习过程会有学习构图和局部区别？  
删除部分黑白、带水印和文字的图片  

## resize photos
scaling images to 256X256 pixels  
[process.py](https://github.com/affinelayer/pix2pix-tensorflow.git)  

```  
! python pix2pix-tensorflow/tools/process.py \
  --input_dir Dataset/vase_origin/flower_in_vase \
  --operation resize \
  --output_dir Dataset/vase  
```  
## train&test
9:1  
## CNN&CycleGAN&artGAN  
### 1. Neural style transfer  
using CNN  
paper: [A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576)  
[code](https://github.com/keras-team/keras/blob/master/examples/neural_style_transfer.py)  
Experiments  
每种花需要找到对应的水彩画  

|  content  |  style  |  result  |
|  -------  |  -----  |  ------  |
|![google cloud](https://github.com/HE-Yangmei/Final_Prj/blob/master/cnn/content/content/peony.jpg)  |  ![google cloud](https://github.com/HE-Yangmei/Final_Prj/blob/master/cnn/style/style/peony.jpg)  |  ![google cloud](https://github.com/HE-Yangmei/Final_Prj/blob/master/cnn/jssc__at_iteration_9.png)  
![google cloud]()|


### 2. CycleGAN  
### 3. artGAN


