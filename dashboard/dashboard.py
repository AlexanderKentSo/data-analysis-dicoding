import streamlit as st
import pandas as pd

def func():
    return st.title('TESTING')

def func2():
    return st.dataframe(data=pd.read_csv('data\day.csv'))

func()
func2()