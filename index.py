import numpy as np 
import matplotlib.pyplot as pl
from matplotlib.animation import FuncAnimation



# Data acak
jumlah_data = 80
x = np.array([i * 0.1 for i in range(jumlah_data)])
y = np.array([i * 0.1 + np.random.randn() for i in range(jumlah_data)])

# Fungsi linear
def linear(x, m, b):
    return m * x + b

# Inisialisasi
m = 5
b = 2
learning_rate = 0.01
x_prediksi = np.array([0, 10])

# Untuk animasi
m_list_prediksi = []
x_list_prediksi = []
y_list_prediksi = []

for i in range(jumlah_data):
    y_prediksi2 = linear(x[i], m, b)
    y_actual = y[i]
    error = y_actual - y_prediksi2

    # Update m dan b
    m = m + learning_rate * error * x[i]
    b = b + learning_rate * error

    # Hindari pembagian dengan nol
    if x[i] != 0:
        delta_m = learning_rate * error / x[i]
    else:
        delta_m = 0

    m_prediksi = m + delta_m
    m_list_prediksi.append(m_prediksi)
    x_list_prediksi.append(x_prediksi)
    y_list_prediksi.append(linear(x_prediksi, m_prediksi, b))

# Visualisasi
fig = pl.figure(figsize=(5, 5))
line, = pl.plot([], [], "r")

def animate(frame_num):
    x_line = x_list_prediksi[frame_num]
    y_line = y_list_prediksi[frame_num]
    line.set_data(x_line, y_line)
    return line,

pl.scatter(x, y, color='red')
pl.axis([0, 10, 0, 10])
anime = FuncAnimation(fig, animate, frames=len(x_list_prediksi), interval=100, repeat=False)
pl.show()
