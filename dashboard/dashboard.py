import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def func():
    return st.title('TESTING')

def func2():
    day = pd.read_csv('data/day.csv')  # Correcting the path separator for cross-platform compatibility
    data_hari = day.groupby('workingday')['cnt'].mean()

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the bar chart
    ax.bar(data_hari.index, data_hari.values)

    # Set labels and title
    ax.set_xlabel('Tipe hari')
    ax.set_ylabel('Rata-rata Peminjaman Sepeda')
    ax.set_title('Rata-rata Peminjaman Sepeda di Hari Kerja dan Libur')

    # Set the x-ticks
    ax.set_xticks(range(2))
    ax.set_xticklabels(['Libur', 'Kerja'])

    # Display the plot in Streamlit
    st.pyplot(fig)

func()
func2()