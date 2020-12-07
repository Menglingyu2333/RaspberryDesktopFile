import RPi.GPIO as GPIO  #引入函数库
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  #设置引脚编号规则
GPIO.setup(12, GPIO.OUT)    #将12号引脚设置成输出模式
#pwm=GPIO.PWM(12, 2)
while True:
 # 获取CPU温度 
    tmpFile = open( '/sys/class/thermal/thermal_zone0/temp' )
    cpu_temp_raw = tmpFile.read() 
    tmpFile.close() 
    cpu_temp = round(float(cpu_temp_raw)/1000, 1) 
    print (cpu_temp) 
    #如果温度大于47`C，就启动风扇 
    if cpu_temp >= 55 :
        GPIO.output(12, 1)   #将引脚的状态设置为高电平，此时LED亮了
        #time.sleep(10)
        #pwm.start(50)
    #如果温度小于42`C，就关闭风扇 
    if cpu_temp <= 48 : 
        GPIO.output(12, 0)
        #pwm.stop();
    time.sleep(10)
GPIO.cleanup()