# -*- UTF-8-*- 
# Author : David Vane

import streamlit as st
from transformers import pipeline

# 加载聊天模型
chatbot = pipeline("conversational")

# Streamlit 应用程序的标题和描述
st.title("简单聊天机器人")
st.markdown("这是一个基于GPT的简单聊天机器人应用程序。输入您的问题并观察回答！")

# 聊天机器人的主要交互逻辑
def chat(user_input):
    response = chatbot(user_input)
    return response[0]['generated_text']

# 用户输入框和“发送”按钮
user_input = st.text_input("您的问题:")
submit_button = st.button("发送")

# 处理用户输入并显示聊天回答
if submit_button:
    st.write("用户: " + user_input)
    response = chat(user_input)
    st.write("聊天机器人: " + response)

