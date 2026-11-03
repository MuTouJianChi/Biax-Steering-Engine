import serial
from pynput import keyboard

SERIAL_PORT = 'COM3'
BAUD_RATE = 115200

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"串口 {SERIAL_PORT} 连接成功，波特率 {BAUD_RATE}")
    print("请按下 W/A/S/D 控制云台，按下 ESC 退出。")
except Exception as e:
    print(f"串口连接失败: {e}")
    exit()

def on_press(key):
    """键盘按下时调用，按住会重复触发"""
    try:
        k = key.char.lower()
        if k in ['w', 'a', 's', 'd']:
            ser.write(k.encode())
            print(f"按下: {k}")
    except AttributeError:
        pass

def on_release(key):
    """键盘松开时调用"""
    try:
        k = key.char.lower()
        if k in ['w', 'a', 's', 'd']:
            print(f"松开: {k}")
    except AttributeError:
        pass

    if key == keyboard.Key.esc:
        print("退出控制程序。")
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

ser.close()