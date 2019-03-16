# Final_Prj

## Dataset
flickr.walk  
[google cloud](https://drive.google.com/drive/folders/1q252qzRZGE5iWlCLZwn1mJfajVxk7I22?usp=sharing)  
natural flower & flower in vase 1500  
watercolor flower 1500  
删除部分黑白和不适合的图片  

## resize photos
scaling to 256X256 pixels  
[process.py](https://github.com/affinelayer/pix2pix-tensorflow.git)  

'''  
! python pix2pix-tensorflow/tools/process.py \
  --input_dir Dataset/vase_origin/flower_in_vase \
  --operation resize \
  --output_dir Dataset/vase
'''  

