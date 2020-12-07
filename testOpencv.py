
import numpy as np
import cv2 as cv
cnt = 0
while True:
    center = (300, 300)
    # img = np.ones((12000, 12000, 3), np.uint8)  # 生成一个空RGB图像
    img = np.ones((600, 600), np.uint8)  # 生成一个空灰度图像

    # point_color = (255, cnt, cnt)  # BGR （blue, green, red)
    point_color = 180  # gray 单通道灰度图

    # 线型，生成线条的算法不同，都是实线
    lineType = cv.LINE_8
    # lineType = cv2.LINE_4
    # lineType = cv2.LINE_AA

    thickness = 1
    # 画圆    所在图像 位置    半径     颜色          宽度       线型
    cv.circle(img, center, 10+cnt, point_color, thickness, lineType)

    # 画点，即实心圆，通过控制size（半径）和thickness来控制是否是实心
    point_size = 1
    thickness = 1
    # 要画的点列表
    points_list = [(160+cnt, 155), (100, 160+cnt), (150+cnt, 200+cnt), (200, 180), (120, 150), (145, 180)]
    for point in points_list:
        cv.circle(img, point, point_size, point_color, thickness)

    # 画矩形
    ptLeftTop = (100, 100)
    ptRightBottom = (500, 500)
    #                 左上角点     右下角点
    cv.rectangle(img, ptLeftTop, ptRightBottom, point_color, thickness, lineType)

    # 画直线
    ptStart = (400, 200)
    ptEnd = (200, 400)
    cv.line(img, ptStart, ptEnd, point_color, thickness, lineType)

    # 画椭圆
    axesSize = (90, 60)  # 长轴半径为 90，短轴半径为 60
    rotateAngle = 30  # 旋转角度为 30
    startAngle = 0
    endAngle = 270
    cv.ellipse(img, center, axesSize, rotateAngle, startAngle, endAngle, point_color, thickness, lineType)

    text = 'testOpencv'
    org = (50, 50)
    fontFace = cv.FONT_HERSHEY_COMPLEX
    fontScale = 1.5
    thickness = 0
    lineType = 8
    bottomLeftOrigin = False
    # bottomLeftOrigin = True
    cv.putText(img, text, org, fontFace, fontScale, point_color, thickness, lineType, bottomLeftOrigin)
    # cv.putText(img, text, org, fontFace, fontScale, fontcolor, thickness, lineType)

    cv.namedWindow("image")
    cv.imshow('image', img)
    cnt += 1
    key = cv.waitKey(50)
    if key == ord('1'):   # 判断是哪一个键按下
        break
cv.destroyAllWindows()