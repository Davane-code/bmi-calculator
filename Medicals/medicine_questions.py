import streamlit as st

questions = {
    '1': {
        'text': '《中华人民共和国药典》最早于何年颁布',
        'options': {
            'A': '1950年',
            'B': '1951年',
            'C': '1952年',
            'D': '1953年',
            'E': '1954年'
        },
        'answer': 'D',
        'answer_text': '1953年'
    },
    '2': {
        'text': '药师审查处方时发现处方有涂改处，应采取的正确措施是',
        'options': {
            'A': '让患者与处方医师联系写清',
            'B': '药师只要看清可予调配',
            'C': '药师向处方医师问明情况可予调配',
            'D': '药师与处方医师联系，让处方医师在涂改处签字后方可调配',
            'E': '药师向上级药师请示批准后，在涂改处签字后即可调配'
        },
        'answer': 'D',
        'answer_text': '药师与处方医师联系，让处方医师在涂改处签字后方可调配'
    },
    '3': {
        'text': '《中华人民共和国药典》是由',
        'options': {
            'A': '国家颁布的药品集',
            'B': '国家药品监督管理局制定的药品标准',
            'C': '国家药品委员会制定的药品手册',
            'D': '国家药品监督管理局制定的药品法典',
            'E': '国家编纂的药品规格标准的法典'
        },
        'answer': 'E',
        'answer_text': '国家编纂的药品规格标准的法典'
    },
    '4': {
        'text': '将液体制剂分为胶体溶液．混悬液．乳浊液等属于',
        'options': {
            'A': '按照分散系统分类',
            'B': '按照性状分类',
            'C': '按照物态分类',
            'D': '按照制备方法分类',
            'E': '按照给药途径分类'
        },
        'answer': 'A',
        'answer_text': '按照分散系统分类'
    },
    '5': {
        'text': '下列哪种药物可发生变旋反应',
        'options': {
            'A': '肾上腺素',
            'B': '丁卡因',
            'C': '后马托品',
            'D': '氯霉素',
            'E': '抗坏血酸'
        },
        'answer': 'A',
        'answer_text': '肾上腺素'
    },
    '6': {
        'text': '下列叙述种哪一条是正确的',
        'options': {
            'A': '氨基酸在酸性溶液中称为酸性氨基酸',
            'B': '氨基酸在碱性溶液中称为碱性氨基酸',
            'C': '氨基酸在中性溶液中称为中性氨基酸',
            'D': '以上叙述都对',
            'E': '以上叙述都错'
        },
        'answer': 'D',
        'answer_text': '以上叙述都对'
    },
    '7': {
        'text': '光加速实验一般在光加速实验橱中进行，光橱的照度及光照时间要求为',
        'options': {
            'A': '2000-4000LX，10天',
            'B': '4000-5000LX，10天',
            'C': '1000-3000LX，10天',
            'D': '1000-3000LX，15天',
            'E': '3000-4000LX，15天'
        },
        'answer': 'B',
        'answer_text': '4000-5000LX，10天'
    },
    '8': {
        'text': '以下关于加速试验法的描述哪一种是正确的',
        'options': {
            'A': '以Arrhenius指数方程为基础的加速实验法，只有热分解反应，且活化能在418-1254Kj/mol时才适用',
            'B': '经典恒温法应用于均相系统一般得出较满意的结果，对于非均相系统（如混悬液，乳浊液等）通常误差较大',
            'C': 'Arrhenius指数方程式假设活化能不随温度变化提出的，只考虑温度对反应速度的影响。因此，在加速实验中，其他条件（如溶液的pH）应保持恒定',
            'D': '加速实验测出的有效期为预测有效期，应与留样观察的结果对照，才能得出产品实质的有效期',
            'E': '以上叙述都正确'
        },
        'answer': 'D',
        'answer_text': '加速实验测出的有效期为预测有效期，应与留样观察的结果对照，才能得出产品实质的有效期'
    },
    '9': {
        'text': '下列各项中哪一项用pKb表示',
        'options': {
            'A': '酸的pH值',
            'B': '酸的电离常数',
            'C': '酸式盐的水解平衡常数的负对数',
            'D': '碱的pH值',
            'E': '碱的电离常数'
        },
        'answer': 'E',
        'answer_text': '碱的电离常数'
    },
    '10': {
        'text': '制备下列溶液时，哪个可应用加热溶解法',
        'options': {
            'A': '氢氧化钙',
            'B': '氯化铵',
            'C': '碳酸氢钠',
            'D': '氯化钙（CaCl2·2H2O）',
            'E': '氢氧化钠'
        },
        'answer': 'B',
        'answer_text': '氯化铵'
    },
    '11': {
        'text': '碘化钾有使碘助溶和稳定的作用，下列哪个碘化物有助溶和稳定的作用',
        'options': {
            'A': '碘奥酮（碘吡啦啥）',
            'B': '碘化钙',
            'C': '碘化银',
            'D': '碘化油',
            'E': '碘仿'
        },
        'answer': 'B',
        'answer_text': '碘化钙'
    },
    '12': {
        'text': '下面是关于注射剂稳定性的叙述，指出哪一条是错误的',
        'options': {
            'A': '注射剂的氧化主要是由于某些药物的分子结构中某些基团与空气中的氧相互作用所致。为了防止氧化变色，可加入适量焦亚硫酸钠、亚硫酸钠、硫代硫酸钠、硫脲、抗坏血酸等。',
            'B': '抗坏血酸、盐酸肾上腺素、盐酸普鲁卡因、水杨酸钠、盐酸多巴胺等，在有微量金属离子存在下，可加速变色或分解。实际工作中，为了避免金属离子对药物的催化作用，常加入一定浓度的依地酸二钠或依地酸钙钠。',
            'C': '在注射液中通入惰性气体，也是防止主药氧化变色的有效措施之一。',
            'D': '磺胺嘧啶钠注射液通入二氧化碳气体，以排除药液中溶解的及容器空间的氧，从而使药液稳定。',
            'E': '有些注射液，为了防止氧化、变质，常常是在加入抗氧剂的同时也通入惰性气体。'
        },
        'answer': 'D',
        'answer_text': '磺胺嘧啶钠注射液通入二氧化碳气体，以排除药液中溶解的及容器空间的氧，从而使药液稳定。'
    },
    '13': {
        'text': '下列有关化学动力学的描述哪个是错误的',
        'options': {
            'A': '化学动力学是制剂稳定性加速实验的理论依据，药物制剂降解的规律，生产工艺过程的制定，处方设计及有效期的确定等均与之有关。',
            'B': '化学动力学是研究化学反应的速度以及影响速度的因素的科学。',
            'C': '反应速度系指单位时间，单位体积中反应物下降的量或产物生成量。',
            'D': '在药物制剂的降解反应中，多数药物可按零级、一级反应处理。',
            'E': '对于零级降解的药物制剂，其反应速度积公式为lgC=(-K/2.303)*t+lgC0。'
        },
        'answer': 'E',
        'answer_text': '对于零级降解的药物制剂，其反应速度积公式为lgC=(-K/2.303)*t+lgC0。'
    },
    '14': {
        'text': '下列各种药物中哪个不能发生水解反应',
        'options': {
            'A': '盐酸普鲁卡因',
            'B': '乙酰水杨酸',
            'C': '青霉素和头孢菌素等',
            'D': '巴比妥类',
            'E': '维生素C'
        },
        'answer': 'E',
        'answer_text': '维生素C'
    },
    '15': {
        'text': '药物稳定与否的根本原因在于自身的化学结构，外界因素则是引起变化的条件，影响药物制剂降解的外界因素主要有',
        'options': {
            'A': 'pH值与温度',
            'B': '溶剂介电常数及电子强度',
            'C': '赋型剂或附加剂的影响',
            'D': '水分、氧、金属离子和光线',
            'E': '以上都对'
        },
        'answer': 'E',
        'answer_text': '以上都对'
    },
    '16': {
        'text': '对于液体制剂，为了延缓药物降解可采用下述那种措施',
        'options': {
            'A': '调节pH值或改变溶质组成',
            'B': '充入惰性气体',
            'C': '加入附加剂如抗氧剂、螯合剂、抗光解剂等',
            'D': '改变剂型',
            'E': '以上措施均可采用'
        },
        'answer': 'E',
        'answer_text': '以上措施均可采用'
    },
    '17': {
        'text': '对于固体制剂，延缓药物降解措施有',
        'options': {
            'A': '加入干燥剂或（和）改善包装',
            'B': '改变生产工艺和直接压片、包衣等',
            'C': '改变剂型',
            'D': '制定稳定的衍生物',
            'E': '以上措施均可采用'
        },
        'answer': 'E',
        'answer_text': '以上措施均可采用'
    },
    '18': {
        'text': '下列有关药物稳定性正确的叙述是',
        'options': {
            'A': '亚稳定型晶型属于热力学不稳定晶型，制剂中应避免使用。',
            'B': '乳剂的分层是不可逆现象。',
            'C': '为增加混悬液稳定性，加入的能降低Zeta电位、粒子絮凝程度增加的电解质称为絮凝剂。',
            'D': '乳剂破裂后，加以震摇，能重新分散，恢复成原来状态的乳剂。',
            'E': '凡给出质子或接受质子的物质的催化反应称特殊酸碱催化反应。'
        },
        'answer': 'C',
        'answer_text': '为增加混悬液稳定性，加入的能降低Zeta电位、粒子絮凝程度增加的电解质称为絮凝剂。'
    },
    '19': {
        'text': '关于药物稳定性的正确叙述是',
        'options': {
            'A': '盐酸普鲁卡因溶液的稳定性受温度影响，与pH值无关。',
            'B': '药物的降解速度与粒子强度无关。',
            'C': '固体制剂的赋型剂不影响药物稳定性。',
            'D': '药物的降解速度与溶剂无关。',
            'E': '零级反应的反应速度与反应溶度无关。'
        },
        'answer': 'E',
        'answer_text': '零级反应的反应速度与反应溶度无关。'
    },
    '20': {
        'text': '下列不属于表面活性剂类别的是',
        'options': {
            'A': '脱水山梨醇脂肪酸脂类',
            'B': '聚氧乙烯去水山梨醇脂肪酸脂类',
            'C': '聚氧乙烯脂肪酸脂类',
            'D': '聚氧乙烯脂肪醇醚类',
            'E': '聚氧乙烯脂肪酸醇类'
        },
        'answer': 'E',
        'answer_text': '聚氧乙烯脂肪酸醇类'
    },
    '21': {
        'text': '不同HLB值的表面活性剂用途不同，下列错误者为',
        'options': {
            'A': '增溶剂最适范围为15-18以上',
            'B': '去污剂最适范围为13-16',
            'C': '润湿剂与铺展剂最适范围为7-9',
            'D': '大部分消泡剂最适范围为5-8',
            'E': 'O/W乳化剂最适范围为8-16'
        },
        'answer': 'D',
        'answer_text': '大部分消泡剂最适范围为5-8'
    },
    '22': {
        'text': '天然高分子助悬剂阿拉伯胶(或胶浆)一般用量是',
        'options': {
            'A': '1%-2%',
            'B': '1%-5%',
            'C': '5%-15%',
            'D': '10%-15%',
            'E': '12%-15%'
        },
        'answer': 'C',
        'answer_text': '5%-15%'
    },
    '23': {
        'text': '下列与表面活性剂特性无关的是',
        'options': {
            'A': '适宜的粘稠度',
            'B': '克氏点和昙点',
            'C': '亲水亲油平衡值',
            'D': '临界胶团浓度',
            'E': '表面活性'
        },
        'answer': 'A',
        'answer_text': '适宜的粘稠度'
    },
    '24': {
        'text': '下属哪种方法不能增加药物溶解度',
        'options': {
            'A': '加入助溶剂',
            'B': '加入非离子型表面活性剂',
            'C': '制成盐类',
            'D': '应用潜溶剂',
            'E': '加入助悬剂'
        },
        'answer': 'E',
        'answer_text': '加入助悬剂'
    },
    '25': {
        'text': '下列关于表面活性剂性质的叙述中正确的是',
        'options': {
            'A': '有亲水基团，无疏水基团',
            'B': '有疏水基团，无亲水基团',
            'C': '疏水基团、亲水基团均有',
            'D': '有中等极性基团',
            'E': '无极性基团'
        },
        'answer': 'C',
        'answer_text': '疏水基团、亲水基团均有'
    },
    '26': {
        'text': '下列表面活性剂有起昙现象的主要是哪一类',
        'options': {
            'A': '肥皂',
            'B': '硫酸化物',
            'C': '磺酸化物',
            'D': '季铵化物',
            'E': '吐温'
        },
        'answer': 'E',
        'answer_text': '吐温'
    }
}

def display_questions(start, end):
    st.title('试卷展示')
    st.header('选择题')
    st.subheader('[A型题]')

    for question_id, question in questions.items():
        if start <= int(question_id) <= end:
            st.write(f'{question_id}. {question["text"]}')
            for option_key, option_value in question['options'].items():
                st.write(f'{option_key}. {option_value}')
            st.write('---')

def display_question(question_number, question_data):
    st.subheader(f"题目 {question_number}:")
    st.write(question_data['text'])

def search_question(keyword):
    results = []
    for question_number, question_data in questions.items():
        if keyword in question_data['text']:
            results.append(question_number)
    return results

def main():
    st.title("试卷展示应用")
    # display_questions(1,7)
    # 搜索框
    search_keyword = st.text_input('输入关键字搜索题目：')

    # 搜索按钮
    search_button = st.button('搜索')

    if search_button:
        # 执行搜索
        search_results = search_question(search_keyword)

        # 显示搜索结果
        if search_results:
            st.markdown('### 搜索结果：')
            for question_num in search_results:
                # Retrieve question data based on the question number
                question_data = questions.get(str(question_num))
                # Display the question and options
                if question_data:
                    st.markdown(f"**{question_num}.{question_data['text']}**")
                    for option, text in question_data['options'].items():
                        st.markdown(f'- {option}. {text}')
                    st.markdown(f'答案：{question_data["answer"]} - <span style="background-color: yellow;">{question_data["answer_text"]}</span>', unsafe_allow_html=True)
                    st.markdown('---')
                else:
                    st.error("Question not found!")
        else:
            st.markdown('### 搜索结果：无匹配题目')

    # 显示所有题目
    st.markdown('### 所有题目：')
    for question_num, question_data in questions.items():
        st.markdown(f'**题目 {question_num}:** {question_data["text"]}')
        for option, text in question_data['options'].items():
            st.markdown(f'- {option}. {text}')
        st.markdown('---')


if __name__ == '__main__':
    main()
