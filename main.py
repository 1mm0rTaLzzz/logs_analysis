import numpy as np
import matplotlib.pyplot as plt


def parse_line(line):
    values = line.split(';')[:-1]
    voltage = list(map(float, values[0].split(',')))

    odometry = [float(val) if val else 0 for val in values[1].split(',') if val.strip()]

    cam = [float(val) if val else 0 for val in values[2].split(',') if val.strip()]

    time = float(values[3])
    return voltage, odometry, cam, time


def parse_file(file_path):
    parsed_data = []
    with open(file_path, 'r') as file:
        for line in file:
            voltage, odometry, cam, time = parse_line(line)
            parsed_data.append((voltage, odometry, cam, time))
    return parsed_data


file_path = "logs_KUKA.crash"
parsed_data = parse_file(file_path)
vol = []
odom = []
camm = []
time_ = []

for voltage, odometry, cam, time in parsed_data:
    vol.append(voltage)
    odom.append(odometry)
    camm.append(cam)
    time_.append(time)

vol = np.array(vol)
odom = np.array(odom)
camm = np.array(camm)
time_ = np.array(time_)

plt.scatter(time_, vol[:, 0], label='Voltage x')
plt.scatter(time_, vol[:, 1], label='Voltage y')
plt.scatter(time_, vol[:, 2], label='Voltage z')
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.legend()
plt.title('Voltage Data')
plt.show()

plt.scatter(time_, odom[:, 0], label='Odometry x')
plt.scatter(time_, odom[:, 1], label='Odometry y')
plt.scatter(time_, odom[:, 2], label='Odometry z')
plt.xlabel('Time')
plt.ylabel('Odometry')
plt.legend()
plt.title('Odometry Data')
plt.show()

plt.scatter(time_, camm[:, 0], label='Camera x')
plt.scatter(time_, camm[:, 1], label='Camera y')
plt.scatter(time_, camm[:, 2], label='Camera z')
plt.xlabel('Time')
plt.ylabel('Camera')
plt.legend()
plt.title('Camera Data')
plt.show()

delta = abs(camm - odom)
plt.scatter(time_, delta[:, 0], label='Delta x')
plt.scatter(time_, delta[:, 1], label='Delta y')
plt.scatter(time_, delta[:, 2], label='Delta z')
plt.xlabel('Time')
plt.ylabel('Delta')
plt.legend()
plt.title('Delta between Camera and Odometry Data')
plt.show()
print('Average delta ', np.mean(delta))
print(sum(time_)/60)
