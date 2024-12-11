import streamlit as st
import pandas as pd

# ファイルアップロード
uploaded_file = st.file_uploader("Excelファイルを選択してください", type=["xlsx"])

if uploaded_file is not None:
    # Excelファイルを読み込む
    df = pd.read_excel(uploaded_file)

    # データフレームをHTMLに変換する
    html = df.to_html()

    # HTMLを表示する
    st.write(html)

    # HTMLファイルとして保存する
    with open("ExcelToHTML.html", "w") as file:
        file.write(html)
    st.success("HTMLファイルに変換されました。")
