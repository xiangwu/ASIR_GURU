<h1 style="text-align:center; font-family:Times New Roman; color:balck;">
  绘画机器人的控制<span style="font-family:SimSun;"></span>
</h1>


- [一、使用刷有GRBL的主控板控制绘画机](#一使用刷有grbl的主控板控制绘画机)
- [二、令绘画机实现绘画功能 视频教程](#二令绘画机实现绘画功能-视频教程)
  - [预览网站](#预览网站)
- [stm32控制绘画机的简单运动（需要学习一点stm32的基础）](#stm32控制绘画机的简单运动需要学习一点stm32的基础)
 



##  一、使用刷有GRBL的主控板控制绘画机
  [这里用到的主板（点击）](https://item.taobao.com/item.htm?abbucket=2&id=753430651908&mi_id=00002i3sosQcbKISXqzQVDgfO1JRoMr3p2XzNHvJcPj4RIw&ns=1&priceTId=2150472917608573690802435e11bd&skuId=5467926203629&spm=a21n57.sem.item.5.51193903NtvlWL&utparam=%7B%22aplus_abtest%22%3A%22296aff1721c22e033894fbb45138b0c3%22%7D&xxc=taobaoSearch)
   [这里用到的绘画机（点击）](https://www.bilibili.com/video/BV1gw411h7PQ?spm_id_from=333.788.videopod.episodes&vd_source=a5f38014ef46f3bb620874341e8af6d6&p=2)


 - 与绘画机的步进电机连接，供电后主板上的wifi模块启动
 - 用手机或者电脑连接上绘画机的wifi即可为绘画机配置网络，实现网络控制绘画机器的运动
  
 [![pVLsxDx.png](https://s21.ax1x.com/2025/10/19/pVLsxDx.png)](https://imgchr.com/i/pVLsxDx)
 
## 二、令绘画机实现绘画功能 [视频教程](https://www.bilibili.com/video/BV1ka4y1w7Wv/?spm_id_from=333.337.search-card.all.click&vd_source=a5f38014ef46f3bb620874341e8af6d6)
使用软件将想要绘制的图像转化为Gcode代码就能控制绘画机自动绘画
这里使用的是inscape

 >- 1、先将所选图片进行二值化处理然后导入

[![pVLyVKI.png](https://s21.ax1x.com/2025/10/19/pVLyVKI.png)](https://imgchr.com/i/pVLyVKI)
 
 >- 2、转换为白描位图（点击应用选中图片移开，将原图片删除）

  [![pVLyQPg.png](https://s21.ax1x.com/2025/10/19/pVLyQPg.png)](https://imgchr.com/i/pVLyQPg)
  
 >- 3、再将图片对象转化为路径

  [![pVLy3xs.png](https://s21.ax1x.com/2025/10/19/pVLy3xs.png)](https://imgchr.com/i/pVLy3xs)

 >- 4、使用工具配置刀具的参数（速度等）

 [![pVL6rtS.png](https://s21.ax1x.com/2025/10/19/pVL6rtS.png)](https://imgchr.com/i/pVL6rtS)

 >- 5、设置定向点（z轴是设置笔到原点的距离），并拖拽红框设定远点位置

 [![pVLy0G4.png](https://s21.ax1x.com/2025/10/19/pVLy0G4.png)](https://imgchr.com/i/pVLy0G4)
 [![pVLyoQA.png](https://s21.ax1x.com/2025/10/19/pVLyoQA.png)](https://imgchr.com/i/pVLyoQA)

 >- 6、使用Gcode工具生成Gcode

 [![image.png](https://pic1.imgdb.cn/item/68f4ab913203f7be007dfa47.png)](https://pic1.imgdb.cn/item/68f4ab913203f7be007dfa47.png)

 >- 7、生成Gcode到指定路径

在弹出的首选项一栏填写路径和名称，然后返回第一栏点击应用，就得到了Gcode文件



### 预览网站
如果想查看文件的展示效果，可以将生成的Gcode文件上传到这个网站预览
 [网站](https://ncviewer.com/)



## stm32控制绘画机的简单运动（需要学习一点stm32的基础）


 准备工作（参考）
- 准备stm32f103c8t6板子，降压模块，A4988电机驱动模块，蓝牙模块，OLED显示屏，PCB板子
  
- 安装stm32cubemax和keil软件
- 烧录程序






