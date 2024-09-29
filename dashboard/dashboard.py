import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def pendahuluan():
    title = 'Pendahuluan:sparkles:'
    cap = '''
    Dataset yang digunakan dalam analisis ini adalah Bike-Sharing-Dataset.
    Dataset ini berisi informasi tentang peminjaman sepeda di Washington D.C.
    pada tahun 2011 dan 2012. Dataset ini mencakup:

    - Waktu: Catatan peminjaman berdasarkan pembaruan data.
    - Cuaca: Kondisi cuaca seperti cerah, mendung, gerimis, atau hujan.
    - Hari kerja vs libur: Membedakan apakah peminjaman terjadi pada hari kerja atau hari libur.
    - Jumlah peminjaman: Jumlah sepeda yang dipinjam dalam periode waktu tertentu.

    Tujuan utama dari analisis dataset ini adalah untuk mengevaluasi pengaruh
    berbagai faktor terhadap jumlah peminjaman sepeda.
    '''
    st.title(title)
    st.text(cap)

def fokus():
    title = 'Fokus analisis:notebook:'
    cap = '''
    Beberapa hal yang akan dianalisis pada kesempatan ini adalah:

    - Bagaimana pengaruh hari libur terhadap peminjaman sepeda?
    - Pada jam berapa sepeda paling banyak dipinjam?
    - Bagaimana pengaruh cuaca terhadap peminjaman sepeda?
    '''
    st.title(title)
    st.text(cap)

def data_hari():
    day = pd.read_csv('data/day.csv')
    data_hari = day.groupby('workingday')['cnt'].mean()

    fig, ax = plt.subplots()

    ax.bar(data_hari.index, data_hari.values)
    ax.set_xlabel('Tipe hari')
    ax.set_ylabel('Rata-rata Peminjaman Sepeda')
    ax.set_title('Rata-rata Peminjaman Sepeda di Hari Kerja dan Libur')

    ax.set_xticks(range(2))
    ax.set_xticklabels(['Libur', 'Kerja'])

    cap= '''
    Hari libur tidak mempengaruhi jumlah peminjaman sepeda secara signifikan dan 
    hanya menyebabkan sedikit penurunan jumlah peminjaman sepeda dibanding hari kerja.
    '''

    st.title(':calendar: Pengaruh hari kerja dan hari libur pada jumlah peminjaman sepeda')
    st.pyplot(fig)
    st.text(cap)
    
def data_jam():
    hour = pd.read_csv('data/hour.csv')
    data_jam = hour.groupby('hr')['cnt'].mean()

    fig, ax = plt.subplots()

    ax.bar(data_jam.index, data_jam.values)
    ax.set_xlabel('jam')
    ax.set_ylabel('rata-rata peminjaman sepeda')
    ax.set_title('rata-rata peminjaman sepeda per jamnya')
    ax.set_xticks(ticks=range(0,24,2))

    cap= '''
    Sepeda paling banyak dipinjam pada jam 5 sore. 
    Jika dilihat dari grafiknya mungkin bisa diambil kesimpulan bahwa 
    kebanyakan orang mulai beraktivitas dari jam 8 pagi dan pulang jam 5 sore.
    '''

    st.title(':clock5: Pengaruh jam pada jumlah peminjaman sepeda')
    st.pyplot(fig)
    st.text(cap)

def data_cuaca():
    hour = pd.read_csv('data/hour.csv')
    data_cuaca = hour.groupby('weathersit')['cnt'].mean()

    fig, ax = plt.subplots()

    ax.bar(data_cuaca.index, data_cuaca.values)
    ax.set_xlabel('cuaca')
    ax.set_ylabel('rata-rata peminjaman sepeda')
    ax.set_title('rata-rata peminjaman sepeda berdasarkan cuaca')
    ax.set_xticks(ticks=range(1,5),labels=['cerah','mendung', 'gerimis', 'hujan lebat'])

    cap= '''
    Cuaca sangat berpengaruh signifikan dalam jumlah peminjaman sepeda. 
    Semakin buruk cuacanya, semakin sedikit jumlah peminjaman sepeda.
    '''

    st.title(':sun_behind_cloud: Pengaruh cuaca pada jumlah peminjaman sepeda')
    st.pyplot(fig)
    st.text(cap)

pendahuluan()
fokus()
data_hari()
data_jam()
data_cuaca()