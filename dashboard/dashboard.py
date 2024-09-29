import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

def pendahuluan():
    title = 'Pendahuluan:sparkles:'
    cap = 'Dataset yang digunakan pada analisis ini adalah Bike-Sharing-Dataset. \nDataset ini berisi informasi tentang\npeminjaman sepeda di Washington D.C. pada tahun 2011 dan 2012.\nData ini mencatat jumlah sepeda yang dipinjam setiap jam dan hari, \nserta beberapa faktor lain.\nDataset ini mencakup:\n\nwaktu: mencatat update data peminjaman.\nCuaca: Kondisi cuaca seperti cerah, mendung, gerimis, atau hujan.\nHari kerja vs libur: Apakah peminjaman terjadi pada hari kerja atau hari libur.\nJumlah peminjaman: jumlah sepeda yang dipinjam pada rentang waktu tertentu.\n\nTujuan utama dari analisis dataset ini adalah untuk menganalisis pengaruh\nberbagai faktor terhadap jumlah peminjaman sepeda'
    return st.title(title),st.text(cap)

# def func2():
#     day = pd.read_csv('data/day.csv')  # Correcting the path separator for cross-platform compatibility
#     data_hari = day.groupby('workingday')['cnt'].mean()

#     # Create a figure and axis
#     fig, ax = plt.subplots()

#     # Plot the bar chart
#     ax.bar(data_hari.index, data_hari.values)

#     # Set labels and title
#     ax.set_xlabel('Tipe hari')
#     ax.set_ylabel('Rata-rata Peminjaman Sepeda')
#     ax.set_title('Rata-rata Peminjaman Sepeda di Hari Kerja dan Libur')

#     # Set the x-ticks
#     ax.set_xticks(range(2))
#     ax.set_xticklabels(['Libur', 'Kerja'])

#     # Display the plot in Streamlit
#     st.pyplot(fig)

pendahuluan()
# func2()