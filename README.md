# Final_Prj  
  
[终稿0.pdf](https://drive.google.com/open?id=11U0hXojYDwIRsc56sy3qLSyqZJIJxXLR)  
[深度有趣](https://zhuanlan.zhihu.com/DeepInterests)  
[colab, google cloud](https://drive.google.com/drive/folders/1SWKWTHqA1hC1k4adu6R4U1gLErqcvPJV?usp=sharing)  
[dataset download](https://colab.research.google.com/drive/1PvuLIFw3bk-PPBIsWoe9Vu498T9uGf_E?usp=sharing)  
[main work:CNN](https://drive.google.com/open?id=1u_lOXBtz0mE2xNNU3nYKcxXhqeWzTBWs)  
[main work:cycleGAN](https://colab.research.google.com/drive/1KciyG8rX-lXj-OSchO6sZ5OzUGDWthRG)  

## Dataset
* Download flickr images by texts, flickr.walk [flickr api usage](https://www.flickr.com/services/api/)  
[Dataset origin](https://drive.google.com/drive/folders/1q252qzRZGE5iWlCLZwn1mJfajVxk7I22?usp=sharing)  
1500 images of flower & flower in vase  
1500 images of watercolor flower   
[How to](https://github.com/harrysha1029/flickr_download_images)  
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
```  
import os, random, shutil
def moveFile(fileDir):
        pathDir = os.listdir(fileDir)    #取图片的原始路径
        filenumber=len(pathDir)
        rate=0.9    #自定义抽取图片的比例
        picknumber=int(filenumber*rate) #按照rate比例从文件夹中取一定数量图片
        sample = random.sample(pathDir, picknumber)  #随机选取picknumber数量的样本图片
        print (sample)
        for name in sample:
                shutil.move(fileDir+name, tarDir+name)
        return
```  
```  
if __name__ == '__main__':
	fileDir = "flower/"    #源图片文件夹路径
	tarDir = "flower/train/"    #移动到新的文件夹路径
	moveFile(fileDir)  
```  

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
* test  
  
### 3. CycleGAN-qp  
paper & code: [Artist Style Transfer Via Quadratic Potential](https://github.com/rahulbhalley/cyclegan-qp)

### 4. artGAN  
## Experiment  
### 1. Comparison between CNN&cycleGAN-qp  
![comparison](https://github.com/HE-Yangmei/Final_Prj/blob/master/experiment/CNN%26cycleGAN-qp.png)  
### 2. FID-Score  
![FID-Score](https://github.com/HE-Yangmei/Final_Prj/blob/master/experiment/FID.png)  
### 3. Ablation experiment  
![ablation](https://github.com/HE-Yangmei/Final_Prj/blob/master/experiment/ablation.png)  
### 4. Tuning  
![tuning](https://github.com/HE-Yangmei/Final_Prj/blob/master/experiment/Adabound.png)  

### 5. Failure  
![failure](https://github.com/HE-Yangmei/Final_Prj/blob/master/experiment/failure.png)  




