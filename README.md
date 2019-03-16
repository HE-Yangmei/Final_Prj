# Final_Prj

## Dataset
Download flickr images by texts, flickr.walk [flickr api usage](https://www.flickr.com/services/api/)
[google cloud](https://drive.google.com/drive/folders/1q252qzRZGE5iWlCLZwn1mJfajVxk7I22?usp=sharing)  
natural flower & flower in vase 1500  
watercolor flower 1500  
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

### 2. CycleGAN  
### 3. artGAN

