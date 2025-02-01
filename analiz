import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

st.set_page_config(page_title="Симулятор замкнутої системи", layout="wide")
st.title("Симулятор замкнутої системи на 3 елементи")
st.write("Введіть коефіцієнти для кожного елемента (чисельник та знаменник через пробіл)")

# Елементи системи – поля вводу коефіцієнтів
with st.form(key="elements_form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Елемент 1")
        e1_num = st.text_input("Чисельник", "2")
        e1_den = st.text_input("Знаменник", "0.5 1")
        
    with col2:
        st.subheader("Елемент 2")
        e2_num = st.text_input("Чисельник", "3")
        e2_den = st.text_input("Знаменник", "1 2")
        
    with col3:
        st.subheader("Елемент 3")
        e3_num = st.text_input("Чисельник", "1")
        e3_den = st.text_input("Знаменник", "0.2 1")
        
    sim_time = st.number_input("Кінцевий час симуляції (сек)", min_value=1.0, value=10.0, step=1.0)
    submit_button = st.form_submit_button(label="Симулювати")

def parse_coeffs(text):
    try:
        return [float(x) for x in text.split()]
    except Exception as e:
        st.error(f"Помилка перетворення коефіцієнтів: {e}")
        return None

if submit_button:
    # Перетворення введених значень
    num1 = parse_coeffs(e1_num)
    den1 = parse_coeffs(e1_den)
    num2 = parse_coeffs(e2_num)
    den2 = parse_coeffs(e2_den)
    num3 = parse_coeffs(e3_num)
    den3 = parse_coeffs(e3_den)

    if None in [num1, den1, num2, den2, num3, den3]:
        st.error("Перевірте правильність введених коефіцієнтів.")
    else:
        try:
            # Побудова передавальних функцій для кожного елемента
            G1 = ctrl.tf(num1, den1)
            G2 = ctrl.tf(num2, den2)
            G3 = ctrl.tf(num3, den3)

            # Загальна передавальна функція відкритої системи (послідовне з'єднання)
            open_loop = G1 * G2 * G3

            # Формування замкнутої системи з одиничним зворотним зв’язком
            closed_loop = ctrl.feedback(open_loop, 1)

            # Обчислення відповіді на одиничний скачок
            t = np.linspace(0, sim_time, 500)
            t, y = ctrl.step_response(closed_loop, T=t)

            # Побудова графіка за допомогою matplotlib
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(t, y, label="Відповідь системи", linewidth=2)
            ax.set_title("Перехідна характеристика замкнутої системи")
            ax.set_xlabel("Час (сек)")
            ax.set_ylabel("Відповідь системи")
            ax.grid(True)
            ax.legend()
            st.pyplot(fig)

            st.subheader("Замкнута передавальна функція системи")
            st.text(closed_loop)
        except Exception as ex:
            st.error(f"Виникла помилка під час розрахунків: {ex}")
