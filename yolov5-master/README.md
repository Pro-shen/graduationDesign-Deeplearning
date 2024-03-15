## 深度学习部分

>深度学习部分使用yolov5开源项目，以yolov5项目为基础，添加了flask模块负责与外网通讯。



### main.py

>main.py文件是拿来切帧的，把拍好的视频放到自定义的路径下面，改一下源码中的视频路径，保存路径，就可以将视频切帧成图片保存。



### Flaskserver.py

>一个简单的flask网络框架搭建，外界通过访问
>
>```shel
>127.0.0.1:5555/upload
>```
>
>路由
>
>##### 入参为
>
>```python
>data = {
>        "imgName": image_path,
>        "base64": encode_str,
>        "objectList": object_list
>    }
>```
>
>imgName就是图片名字，base64为图片转为base64加密格式的字符串（这里建议使用Post方法访问，get方法一是有安全隐患容易被截留，二是get方法的url后面也跟不了那么长的字符串），objectList和输入没关系，带不带都没所谓，
>
>##### 入参后
>
>会将base64的字符串转化为图片进行验证，验证玩会将识别出来的物体的种类数量存在
>
>```python
>objectList
>```
>
>中，格式为：
>
>```python
>{
>  "object": str_object,
>  "number": str_number,
>  "dictValue": int(c)
>}
>```
>
> object为识别出来的物体名字，number为物体数量，dictValue为物体在yaml配置文件中的物体序号。这里的yaml配置文件在
>
>```python
>/data/graduationDesign.yaml
>```
>
>中。

