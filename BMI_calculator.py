import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "体重过轻"
    elif bmi >= 18.5 and bmi < 25:
        return "正常体重"
    elif bmi >= 25 and bmi < 30:
        return "超重"
    else:
        return "肥胖"

# 页面标题
st.title("身体质量指数(BMI) 计算器")

# 输入体重
weight = st.number_input("请输入您的体重（单位：千克）")

# 输入身高
height  = st.number_input("请输入您的身高（单位：米）")

# 计算BMI
if st.button("计算BMI"):
    bmi = calculate_bmi(weight, height)
    st.write("您的BMI指数为： {:.2f}".format(bmi))
    interpretation = interpret_bmi(bmi)
    st.write("解释： {}".format(interpretation))
