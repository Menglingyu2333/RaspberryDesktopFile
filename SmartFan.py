import RPi.GPIO as GPIO  #引入函数库
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  #设置引脚编号规则
GPIO.setup(7, GPIO.OUT)    #将12号引脚设置成输出模式
pwm=GPIO.PWM(7, 10)
GPIO.output(7, 0)
pwm.start(0)

while True:
 # 获取CPU温度 
    tmpFile = open( '/sys/class/thermal/thermal_zone0/temp' )
    cpu_temp_raw = tmpFile.read() 
    tmpFile.close() 
    cpu_temp = round(float(cpu_temp_raw)/1000, 1) 
    print (cpu_temp) 
    #如果温度大于47`C，就启动风扇 
    if cpu_temp >= 58 :
         pwm.ChangeDutyCycle(cpu_temp-10)
    #如果温度小于42`C，就关闭风扇 
    if cpu_temp <= 46 :
        #GPIO.output(12, 0)
        pwm.ChangeDutyCycle(0)
    time.sleep(10)
GPIO.cleanup()