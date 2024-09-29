## SETUP enviroment local

- pastikan semua library sudah terinstall pada enviroment python anda
- jika tidak, silahkan masukan commands berikut ke dalam terminal sesuai dengan enviroment yang anda gunakan:
    * setup enviroment anaconda:
        !conda create --name main-ds python=3.12
        !conda activate main-ds
        !pip install -r requirements.txt

    * setup enviroment terminal:
        !mkdir proyek_analisis_data
        !cd proyek_analisis_data
        !pipenv install
        !pipenv shell
        !pip install -r requirements.txt

- untuk menjalankan dashboard, masukan perintah 'streamlit run dashboard/dashboard.py' dalam terminal
- jika tidak berhasil, coba masukan perintah 'python -m streamlit run dashboard/dashboard.py'

## mengakses dashboard
- dashboard bisa diakses melalui streamlit cloud melalui link yang disediakan di url.txt