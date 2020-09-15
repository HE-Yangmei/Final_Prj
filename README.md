# Final_Prj  
  
[终稿0.pdf](https://drive.google.com/open?id=11U0hXojYDwIRsc56sy3qLSyqZJIJxXLR)  
[深度有趣](https://zhuanlan.zhihu.com/DeepInterests)  
[colab, google cloud](https://drive.google.com/drive/folders/1SWKWTHqA1hC1k4adu6R4U1gLErqcvPJV?usp=sharing)  
[main work:cycleGAN](https://colab.research.google.com/drive/1KciyG8rX-lXj-OSchO6sZ5OzUGDWthRG)  
[main work:CNN](https://drive.google.com/open?id=1u_lOXBtz0mE2xNNU3nYKcxXhqeWzTBWs)

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

```
# 例题2-1-----------------------------------------------------------------
# 2-1.1
print((6 + 10) % 7)
# 2-1.2
seconds = eval(input("请输入一个整数秒："))
minutes = seconds // 60 # 获取分钟数
remainingSeconds = seconds % 60 # 获取除去分钟后的秒数
print(seconds, "秒是", minutes, "分", remainingSeconds, "秒")
-----------------------------------------------------------------------------
# 类型转换int()函数
# 没有进位，只取整数部分
print(int(2.6))
# 作用于变量，但不会改变变量的值
x = 3.3
print(int(x))
print(x)
# 将整数字符串转换为整数
print(int('11') + 2)
print(eval('11') + 2)
print('11' + 2) # 会报错

# 类型转换float()函数
print(float(3))
print(float('4'))
# ------------------------------------------------------------------------------------
# 例题2-2
# 获取销售额
sales = eval(input("请输入销售额："))
# 计算增值税
tax = sales * 0.13
# 输出带两位小数的销售额
print("增值税是：", int(tax * 100) / 100.0)
# ------------------------------------------------------------------------------------
# 例题2-3
# 类型转换
print(int(True))
print(int(False))
print(float(True))
print(float(False))

# 比较运算符的使用
x = 12
print(x == 12)
print(x != 12)
print(x >= 20)

# 比较运算符在if条件语句中的使用
x = eval(input("请输入一个整数："))
y = x % 2 # 取2的余数，偶数取2的余数总是0，奇数取2的余数总是1
if y == 0:
    print(x, '是一个偶数')
# --------------------------------------------------------------------------------------
# 例题2-4
a = 1
a += 8
a -= 8
a *= 8
a /= 8
a //= 8
a %= 8
# ------------------------------------------------------------------------------------------
# 例题2-5
x = 1
y = 5
print((x == 1) and (y == 5)) # 与
print((x == 1) or (y > 9))   # 或
print(not (x != 1))          # 非
# 判断闰年
# 获取年份输入
year = eval(input("请输入一个年份："))
# 用布尔表达式判断是否是闰年
isLeapYear = ((year % 4) == 0)
isLeapYear = isLeapYear and ((year % 100) != 0)
isLeapYear = isLeapYear or ((year % 400) == 0)
# 输出判断结果
print(year, "是闰年吗？", isLeapYear)

math, chinese = eval(input('请以英文逗号为间隔依次输入数学和语文成绩：'))
if (math >= 60) and (chinese >= 60):
    print('成绩合格')


# -------------------------------------------------------------------------------------
# 四舍五入，函数定义、字符串处理、选择语句
def new_round(_float, _len):
    if isinstance(_float, float):
        if str(_float)[::-1].find('.') <= _len:
            return(_float)
        if str(_float)[-1] == '5':
            return(round(float(str(_float)[:-1]+'6'), _len))
        else:
            return(round(_float, _len))
    else:
        return(round(_float, _len))
print(new_round(4.5,0))

```




