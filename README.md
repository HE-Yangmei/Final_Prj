# Final_Prj

## Dataset
* Download flickr images by texts, flickr.walk [flickr api usage](https://www.flickr.com/services/api/)  
[Dataset origin](https://drive.google.com/drive/folders/1q252qzRZGE5iWlCLZwn1mJfajVxk7I22?usp=sharing)  
1500 images of flower & flower in vase  
1500 images of watercolor flower   
* 自然图像和水彩画花下载下来的图像构图方面并不是很契合，自然图像很多花朵大特写，水彩画多是群花，GAN学习过程会有学习构图和局部区别？  
* 删除部分黑白、带水印和文字的图片  

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
随机分割训练集:测试集 = 9:1  
随机抽取，从Flickr下载图片的时候用了sort = relevance，数据集不能直接按顺序划分  

## CNN&CycleGAN&artGAN  
### 1. Neural style transfer  
VGG19  
paper: [A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576)  [code](https://github.com/keras-team/keras/blob/master/examples/neural_style_transfer.py)  
   
每种花需要找到对应的水彩画，不能只改变笔触、线条、晕染效果，会把原图片的颜色改变  

|  content  |  style  |  result  |
|  -------  |  -----  |  ------  |
|![google cloud](https://github.com/HE-Yangmei/Final_Prj/blob/master/cnn/content/content/peony.jpg)  |  ![google cloud](https://github.com/HE-Yangmei/Final_Prj/blob/master/cnn/style/style/peony.jpg)  |  ![google cloud](https://github.com/HE-Yangmei/Final_Prj/blob/master/cnn/output/output/peony.gif)  |


### 2. CycleGAN  
paper & code: [Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://junyanz.github.io/CycleGAN/)  
tensorflow  
* train  
保存模型：flower2watercolor.pb,watercolor2flower.pb
* test  

### 3. artGAN


