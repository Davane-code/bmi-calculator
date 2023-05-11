# -*- UTF-8-*- 
# Author : David Vane

import os
import streamlit as st
import openai
import numpy as np

# 获取 OpenAI API 访问密钥

# openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = "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"

# 定义 GPT-3 模型参数
model_engine = "davinci"
temperature = 0.7
max_tokens = 1024

# 用于提取生成的摘要的函数
def extract_summary(output_text, summary_length):
    output_text = output_text.replace("\n", " ")
    summary = output_text[:summary_length]
    last_period_index = summary.rfind(".")
    summary = summary[:last_period_index + 1]
    return summary

# 应用程序界面布局和功能
def app():
    st.title("生成求职信")
    st.write("请在下面填写您的个人资料和工作描述：")

    # 获取用户输入
    name = st.text_input("姓名")
    email = st.text_input("电子邮件")
    phone = st.text_input("电话号码")
    company = st.text_input("公司名称")
    job_title = st.text_input("职位名称")
    job_description = st.text_area("工作描述", height=200)

    # 生成摘要和设置参数
    summary_length = st.slider("输出摘要的字数", 50, 500, 100, step=10)
    tone = st.selectbox("输出语气", ("友好", "正式"))
    if tone == "友好":
        prompt = f"写一封求职信，介绍一下您的自我，以及您对 {company} 公司的工作岗位的兴趣。"
    else:
        prompt = f"尊敬的招聘经理，我想申请 {job_title} 职位。我是 {name}，我的经历使我非常适合这个职位。"

    # 使用 OpenAI API 生成文本
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    output_text = response.choices[0].text.strip()

    # 提取摘要
    summary = extract_summary(output_text, summary_length)

    # 显示生成的摘要
    st.write("生成的求职信：")
    st.write(summary)

    # 下载生成的摘要
    file_name = f"{name}_求职信.txt"
    if st.button("保存到本地"):
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(summary)
        st.write("文件已保存！")

# 运行应用程序
if __name__ == "__main__":
    app()

