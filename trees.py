import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="CSV Visualization App", page_icon=":chart_with_upwards_trend:", layout="wide")

def main():
    st.title("CSV Visualization App")
    st.subheader("Upload your CSV file and select the columns to visualize")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())
        columns = st.multiselect("Select the columns to visualize", df.columns)
        if columns:
            st.subheader("Plotting the selected columns")
            plt.figure()
            for column in columns:
                plt.plot(df[column])
            st.pyplot()

if __name__=='__main__':
    main()

