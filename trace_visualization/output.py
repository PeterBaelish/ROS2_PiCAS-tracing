import sys
import matplotlib

import matplotlib.pyplot as plt
import numpy as np
import os

y1 = []
y2 = []

filehandler = open('../picas_evaluation/one_chain_one_executor/baseline/trace_normal.txt', "r")
while True:
    line = filehandler.readline()
    if not line:
        break;
    attr = line.split()
    if attr[0] == 'Regular_callback3_latency':
        y1.append(float(attr[1]))
    if attr[0] == 'Regular_callback6_latency':
        y2.append(float(attr[1]))
filehandler.close()

ypoints = np.array(y1)
plt.plot(ypoints, marker = 'o', linestyle = '-', color = 'r', ms = '3', label = 'ROS2 with Linux baseline')


y1 = []
y2 = []

filehandler = open('../picas_evaluation/one_chain_one_executor/baseline/trace_picas.txt', "r")
while True:
    line = filehandler.readline()
    if not line:
        break;
    attr = line.split()
    if attr[0] == 'Regular_callback3_latency':
        y1.append(float(attr[1]))
    if attr[0] == 'Regular_callback6_latency':
        y2.append(float(attr[1]))
filehandler.close()

ypoints = np.array(y1)
plt.plot(ypoints, marker = 'o', linestyle = '-', color = 'b', ms = '3', label = 'ROS2_PiCAS with Linux baseline')


y1 = []
y2 = []

filehandler = open('../picas_evaluation/one_chain_one_executor/RT/trace_picas.txt', "r")
while True:
    line = filehandler.readline()
    if not line:
        break;
    attr = line.split()
    if attr[0] == 'Regular_callback3_latency':
        y1.append(float(attr[1]))
    if attr[0] == 'Regular_callback6_latency':
        y2.append(float(attr[1]))
filehandler.close()

ypoints = np.array(y1)
plt.plot(ypoints, marker = 'o', linestyle = '-', color = 'y', ms = '3', label = 'ROS2_PiCAS with RT Linux')


plt.xlabel("tracing count")
plt.ylabel("latency(ms)")
plt.legend()

plt.show()