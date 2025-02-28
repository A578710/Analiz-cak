import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy.signal import TransferFunction, bode, lti

# Функція для аналізу стійкості
def analyze_stability(num, den, x_t):
    system = TransferFunction(num, den)
    
    # Частотний діапазон
    w = np.logspace(-2, 2, 1000)
    w, mag, phase = bode(system, w)
    
    # Побудова ЛАЧХ
    plt.figure(figsize=(8, 6))
    plt.semilogx(w, mag, label='ЛАЧХ')
    plt.xlabel('Частота (рад/с)')
    plt.ylabel('Амплітуда (дБ)')
    plt.title('Логарифмічна амплітудно-частотна характеристика')
    plt.grid(which='both', linestyle='--')
    st.pyplot(plt)
    
    # Побудова ЛФЧХ
    plt.figure(figsize=(8, 6))
    plt.semilogx(w, phase, label='ЛФЧХ', color='red')
    plt.xlabel('Частота (рад/с)')
    plt.ylabel('Фаза (градуси)')
    plt.title('Логарифмічна фазо-частотна характеристика')
    plt.grid(which='both', linestyle='--')
    st.pyplot(plt)
    
    # Аналіз стійкості за критерієм Найквіста
    system_lti = lti(num, den)
    w, h = system_lti.freqresp(w)
    
    plt.figure(figsize=(6, 6))
    plt.plot(h.real, h.imag, label='Контур Найквіста')
    plt.plot(h.real, -h.imag, linestyle='dashed', color='gray')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.title('Критерій Найквіста')
    plt.grid()
    st.pyplot(plt)
    
# Інтерфейс Streamlit
st.title('Аналіз стійкості динамічної системи')

# Введення коефіцієнтів передавальної функції
num_input = st.text_input('Чисельник передавальної функції (через коми)', '10')
den_input = st.text_input('Знаменник передавальної функції (через коми)', '0.05, 1.05, 1')

# Перетворення введених рядків у списки чисел
num = list(map(float, num_input.split(',')))
den = list(map(float, den_input.split(',')))

# Введення функції x(t)
x_t = st.text_input('Функція x(t)', 'sin(t)')

# Аналіз при натисканні кнопки
if st.button('Аналізувати стійкість'):
    analyze_stability(num, den, x_t)
