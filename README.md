# Introduction
改写文字识别数据生成模型Synthtext，模拟数码管数字图片，解决数据集少，人工标注复杂的问题  

针对现实场景中数码管阴影残留，仪器检测位数和实际值不统一的问题，调整数据生成的方式


# Renderings
原图来自Coco数据集
<div style="display: flex; flex-wrap: wrap;">
    <img src="https://github.com/xiaoboluo6/LED_digital_display_dataset/blob/master/%E6%95%88%E6%9E%9C%E5%9B%BE/figure1.jpg" style="width: 300px; height: 300px;">
    <img src="https://github.com/xiaoboluo6/LED_digital_display_dataset/blob/master/%E6%95%88%E6%9E%9C%E5%9B%BE/figure2.jpg" style="width: 300px; height: 300px;">
    <img src="https://github.com/xiaoboluo6/LED_digital_display_dataset/blob/master/%E6%95%88%E6%9E%9C%E5%9B%BE/figure3.jpg" style="width: 300px; height: 300px;">
    <img src="https://github.com/xiaoboluo6/LED_digital_display_dataset/blob/master/%E6%95%88%E6%9E%9C%E5%9B%BE/figure4.jpg" style="width: 300px; height: 300px;">
    <img src="https://github.com/xiaoboluo6/LED_digital_display_dataset/blob/master/%E6%95%88%E6%9E%9C%E5%9B%BE/figure5.jpg" style="width: 300px; height: 300px;">
    <img src="https://github.com/xiaoboluo6/LED_digital_display_dataset/blob/master/%E6%95%88%E6%9E%9C%E5%9B%BE/figure6.jpg" style="width: 300px; height: 300px;">
</div>

# Usage
使用过程直接看源代码 [SynthText_Readme](https://github.com/ankush-me/SynthText/blob/master/README.md)  

matlab代码生成对应深度图和分割图，后续利用本仓库生成数据集.

本仓库提供了7张图片的深度图和分割图[sevenTest](https://github.com/xiaoboluo6/LED_digital_display_dataset/tree/master/PyScripts/sevenTest)，可测试生成LED数码管数据集

# Difference
实际过程中存在数码管底纹的干扰，所以生成过程分为两个阶段  

首先生成数字“8”作为数码管底纹，然后在相同位置填写数字，最终只返回填写数字的字符坐标和数字坐标  

后续根据实际要求做出调整，包括数字位数，数字颜色，LED字体差异，真实数字前多一个8的残影等情况，不多加赘述








# Other Links
源代码：[SynthText](https://github.com/ankush-me/SynthText)


