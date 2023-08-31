from cv2 import VideoCapture
from cv2 import imwrite
 
# 定义保存图片函数
# image:要保存的图片名字
# addr；图片地址与相片名字的前部分
# num: 相片，名字的后缀。int 类型
def save_image(image, addr, num):
    address = addr + str(num) + '.jpg'
    imwrite(address, image)
 
if __name__ == '__main__':
 
    video_path = "/home/xiaoyu/myData/mower/omni_outdoor.mp4" #视频路径
    out_path = "/home/xiaoyu/myData/mower/img_" #保存图片路径+名字
 
    is_all_frame = False #是否取所有的帧
    sta_frame = 1 #开始帧
    end_frame = 40 #结束帧
 
    ######
    time_interval = 1 #时间间隔
 
    # 读取视频文件
    videoCapture = VideoCapture(video_path)
 
    # 读帧
    success, frame = videoCapture.read()
    print(success)
 
    i = 0
    j = 0
    if is_all_frame:
        time_interval = 1
 
    while success:
        i = i + 1
        if (i % time_interval == 0):
            if is_all_frame == False:
                if i >= sta_frame and i <= end_frame:
                    j = j + 1
                    print('save frame:', i)
                    save_image(frame, out_path, j)
                elif i > end_frame:
                    break
            else:
                j = j + 1
                print('save frame:', i)
                save_image(frame, out_path, j)
 
        success, frame = videoCapture.read()
