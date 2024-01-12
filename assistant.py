import streamlit as st
import numpy as np
import pandas as pd


st.title('含章  :blue[定款小助手] :sunglasses:')

st.divider()
# art_no = st.text_input('货号')

col1, col2, col3 = st.columns(3)

col1.subheader("订货情况")
with col1:
    order_price = st.number_input('订货价')
    transportation = st.number_input('运输费',0.0,0.5,0.05)
    warehouse = st.number_input('仓库均摊费',0.0,1.0,0.5)
    x = st.text_input('订货量','2000') 
    # 货款
    a = float(order_price) * float(x)
    # 运输费+仓库费
    a_1 = (float(transportation)+float(warehouse)) * float(x)
    
    st.write('货款：', a)
    st.write('运输费+仓库费：', a_1)

col2.subheader("销售情况")
with col2:
    sell_price = st.number_input('销售价')
    freight_insurance = st.number_input('运费险')
    platform_fee = st.number_input('平台服务费')
    y = st.slider('销售量',0,int(x),200)  # 👈 this is a widget

    # 销售流水
    b = (float(sell_price)-float(freight_insurance)-float(platform_fee)) * float(y)
    b_1 = (float(sell_price)-float(freight_insurance)-float(platform_fee)-float(order_price)) * float(y)
    st.write('销售流水：', b)

    st.write('毛利：', b_1)

    # st.write('库存量：', int(x)-y)
    # st.write('压货成本：', float(order_price) * (int(x)-y))

col3.subheader("盈利情况")
with col3:
    express = st.number_input('快递费')
    service = st.number_input('客服均摊费')
    
    incidentals = st.number_input('打包 + 人工')
    

    pure_profit = float(y) * (float(sell_price)-float(order_price)-float(express)- float(service)-float(incidentals)-float(freight_insurance)-float(platform_fee)-float(transportation)-float(warehouse))
    st.write('纯利：', pure_profit)
    rate = st.number_input('提成比例',0.0,1.0,0.3)
    st.write('提成：', pure_profit*rate)

st.divider()
st.write('库存量：', int(x)-y)
st.write('压货成本：', (float(transportation)+float(warehouse)+float(order_price)) * (int(x)-y))
st.write('运营能够提现：',pure_profit*rate-(float(transportation)+float(warehouse)+float(order_price)) * (int(x)-y))