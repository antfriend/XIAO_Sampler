import board
import pwmio
import wifi
#import adafruit_ble
#from adafruit_ble.advertising import Advertisement

print("Whoa here Python!")

# Calculate the duty cycle for 3 ms on time in a 25 ms period
on_time = 0.003        # 3 milliseconds
total_period = 0.025   # 25 milliseconds (3 ms on + 22 ms off)
duty_cycle_percentage = on_time / total_period  # 0.003 / 0.025 = 0.12 (12%)

# Convert the duty cycle percentage to a value between 0 and 65535
max_duty = 65535
duty_cycle_value = int(max_duty * duty_cycle_percentage)  # Approximately 7864

# Create a PWMOut object on pin D3 with a frequency of 40 Hz
led = pwmio.PWMOut(board.D3, frequency=40, duty_cycle=0)
piez00 = pwmio.PWMOut(board.D0, frequency=40, duty_cycle=0)
piez01 = pwmio.PWMOut(board.D1, frequency=40, duty_cycle=0)

# Set the duty cycle to achieve 3 ms on time
led.duty_cycle = duty_cycle_value
piez00.duty_cycle = duty_cycle_value
piez01.duty_cycle = duty_cycle_value

# wifi
for network in wifi.radio.start_scanning_networks():
    print(" ")
    print("SSID:", network.ssid)
    print("Signal Strength:", network.rssi)
wifi.radio.stop_scanning_networks()

print(" ")

# ble = adafruit_ble.BLERadio()

# found = set()
# for advertisement in ble.start_scan(Advertisement, timeout=5):
#     addr = advertisement.address
#     if addr not in found:
#         found.add(addr)
#         print("Found BLE device:", addr)
# ble.stop_scan()

while True:
    for network in wifi.radio.start_scanning_networks():
        piez00.duty_cycle = 0
        print(" ")
        ssid = network.ssid
        print("SSID:", ssid)
        signal_strength = network.rssi
        print("Signal Strength:", signal_strength)
        piez01.duty_cycle = duty_cycle_value + signal_strength
    wifi.radio.stop_scanning_networks()

    piez00.duty_cycle = duty_cycle_value
    
    pass
 