# -*- UTF-8-*-
# Author : David Vane

import streamlit as st

questions = {
    "1-1": {
        "text": "药物是指用于预防、治疗、诊断疾病，并规定有适应症的物质。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-2": {
        "text": "药物分析是收载药品质量标准的典籍。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-3": {
        "text": "药品标准是对药品质量、规格及检验方法所作的技术规定。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-4": {
        "text": "药品标准的制定必须坚持“科学性、先进性、规范性、权威性”的原则。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-5": {
        "text": "钠离子的焰色反应显黄色。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-6": {
        "text": "钾离子的焰色反应显蓝色。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-7": {
        "text": "比旋度是反映手性药物特性及其纯度的主要指标。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-8": {
        "text": "重氮化偶合反应可用于芳香第一胺的鉴别。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-9": {
        "text": "物理常数包括相对密度、馏程、熔点、凝点等；其测定结果不仅对药品具有鉴别意义，也可反映药品的纯度，是评价药品质量的主要指标之一。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-10": {
        "text": "药物中的杂质的检查，一般要求测定其准确含量。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-11": {
        "text": "药物的干燥失重测定法是属于药物的特殊杂质的检查法。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-12": {
        "text": "药物的干燥失重测定法主要控制药物中的水分，也包括其它挥发性物质如乙醇等。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-13": {
        "text": "药物检查中不要求检查的杂质，说明药物中不含此类杂质。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-14": {
        "text": "用药物和杂质的溶解行为的差异进行杂质检查，是属于特殊杂质检查法。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-15": {
        "text": "《药典》中所规定的杂质检查项目是固定不变的。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-16": {
        "text": "气相色谱中，柱温直接影响分离效能和分析速度，应根据被测物的沸点、极性大小选择合适的柱温。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-17": {
        "text": "气相色谱中，对于多组份混合物或沸点相差较大的组分可采用程序升温的方法。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-18": {
        "text": "高效液相色谱仪检测器的响应值与待测溶液的浓度通常不呈一次线性关系的是蒸发光散射检测器。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-19": {
        "text": "二极管阵列检测器（DAD）可以同时记录供试品的吸收光谱，故可用于供试品的光谱鉴定和色谱峰的纯度检查。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-20": {
        "text": "为了减少滴定误差，需要选择合适的指示剂或指示方法，使滴定终点尽可能接近滴定反应的化学计量点。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-21": {
        "text": "为去除血浆中蛋白质，可加入异丙醇。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-22": {
        "text": "生物样品经前处理后能够降低分析时的背景噪声。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-23": {
        "text": "提取回收率的验证要考察高、中、低三个浓度的QC样品。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-24": {
        "text": "在生物样品分析方法验证中，精密度用实际样品测定。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-25": {
        "text": "当待测物热稳定性好时，可采用加热的方法将一些热变性蛋白质沉淀。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-26": {
        "text": "水杨酸、乙酰水杨酸均易溶于水，所以以水作为滴定介质。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-27": {
        "text": "水杨酸类药物均可以与三氯化铁在适当的条件下产生有色的铁配合物。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-28": {
        "text": "乙酰水杨酸中仅含有一种特殊杂质水杨酸。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-29": {
        "text": "阿司匹林能与三氯化铁试液直接显色。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-30": {
        "text": "二氢吡啶类药物的分析应避光操作。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-31": {
        "text": "硝苯地平的铈量法测定含量是基于硝苯地平的氧化性。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-32": {
        "text": "硝苯地平可还原后重氮化偶合反应进行鉴别。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-33": {
        "text": "硝苯地平的铈量法进行含量测定时的pH条件应是强酸性。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-34": {
        "text": "尼莫地平的苯环硝基具有氧化性，可将氢氧化亚铁氧化为红棕色氢氧化铁沉淀。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-35": {
        "text": "硝苯地平的丙酮溶液与氢氧化钠试液反应显橙红色。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-36": {
        "text": "尼群地平与碘化铋钾试剂反应呈橙红色沉淀。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-37": {
        "text": "氨氯地平可用重氮化偶合反应进行鉴别。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-38": {
        "text": "氨氯地平具有旋光性。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-39": {
        "text": "中国药典规定硝苯地平在避光条件下用HPLC检查有关物质。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-40": {
        "text": "巴比妥类药物与重金属离子的反应是由于结构中含有丙二酰脲。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-41": {
        "text": "巴比妥类药物在酸性条件下发生一级电离而有紫外吸收。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-42": {
        "text": "差示紫外分光光度法测定巴比妥类药物，其目的是消除杂质吸收的干扰。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-43": {
        "text": "药物的酸碱度检查法采用蒸馏水为溶剂。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-44": {
        "text": "氯氮卓水解后显芳伯氨基反应。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-45": {
        "text": "由于辅料影响，盐酸异丙嗪片需提取后再进行IR鉴别。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-46": {
        "text": "用铈量法测定吩噻嗪类药物的含量时，常用的指示剂是吩噻嗪类药物自身做指示剂。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-47": {
        "text": "非水滴定法可用于吩噻嗪类药物片剂的直接滴定。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-48": {
        "text": "有氧化物存在时，吩噻嗪类药物的鉴别可采用钯离子比色法。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-49": {
        "text": "盐酸氯丙嗪可与稀盐酸-三硝基苯酚生成沉淀。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-50": {
        "text": "异丙嗪置于铜网上燃烧，火焰显绿色。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-51": {
        "text": "奋乃静置于铜网上燃烧，火焰显绿色。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-52": {
        "text": "盐酸氯丙嗪可被硝酸氧化显红色用于鉴别。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-53": {
        "text": "吩噻嗪类药物与钯离子配合呈色的反应可用于鉴别。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-54": {
        "text": "硫氮杂蒽母核在205nm、254nm、300nm三个波长处有最大吸收，可用紫外分光光度法鉴别本类药物。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-55": {
        "text": "青蒿素和双氢青蒿素均可采用与碘化钾试液-淀粉反应进行鉴别。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-56": {
        "text": "硫酸奎宁在稀硫酸溶液中显蓝色荧光。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-57": {
        "text": "双氢青蒿素是青蒿琥酯的体内活性代谢物。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-58": {
        "text": "中国药典中青蒿素原料药采用UV法进行含量测定。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-59": {
        "text": "中国药典中用于某生物碱的鉴别方法为：供试品水溶液中滴加溴试液与氨试液，即显翠绿色，该反应是Vitali反应。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-60": {
        "text": "中国药典规定硫酸奎宁需检查其他金鸡纳碱。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-61": {
        "text": "硫酸奎宁供试品溶液中滴加氯化钡溶液，生成白色沉淀。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-62": {
        "text": "硫酸奎宁属于喹啉类药物。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-63": {
        "text": "绿奎宁反应可用于鉴别硫酸奎宁。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-64": {
        "text": "喹啉类药物具有喹啉杂环，可用紫外吸收光谱的特征鉴别该类药物。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-65": {
        "text": "CZE电泳模式中只能使用水相缓冲溶液。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-66": {
        "text": "UPLC操作中流速不受限制，且越高越好。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-67": {
        "text": "MECC主要用于非离子状态的样品。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-68": {
        "text": "CZE主要用于非离子状态的样品。",
        "options": {},
        "answer": "",
        "answer_text": "×"
    },
    "1-69": {
        "text": "环糊精是手性HPLC技术中手性流动相添加剂。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-70": {
        "text": "奎宁是手性HPLC技术中手性流动相添加剂。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-71": {
        "text": "纤维素可作HPLC的手性固定相。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-72": {
        "text": "GC-MS最常用的测定方法为总离子流法和质量碎片图谱法。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-73": {
        "text": "目前GC-MS最常用的接口是毛细管柱直接导入型接口。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "1-74": {
        "text": "UPLC与HPLC基于相同的分离机制，故相互之间的方法转换非常简易。",
        "options": {},
        "answer": "",
        "answer_text": "√"
    },
    "2-1": {
        "text": "在《中国药典》中，通用的测定方法收载在（ ）",
        "options": {
            "A": "药典一部",
            "B": "药典二部",
            "C": "药典三部",
            "D": "药典四部"
        },
        "answer": "D",
        "answer_text": "药典四部"
    },
    "2-2": {
        "text": "解释和使用《中国药典》正确进行质量检定的基本原则的是（ ）",
        "options": {
            "A": "检验方法",
            "B": "真实性",
            "C": "代表性",
            "D": "索引",
            "E": "凡例"
        },
        "answer": "E",
        "answer_text": "凡例"
    },
    "2-3": {
        "text": "以下不属于《中国药典》二部收载的是（ ）",
        "options": {
            "A": "化学药品",
            "B": "抗生素",
            "C": "生物药品",
            "D": "生化药品",
            "E": "放射性药品"
        },
        "answer": "C",
        "answer_text": "生物药品"
    },
    "2-4": {
        "text": "按《中国药典》精密量取50ml某溶液时，宜选用（ ）",
        "options": {
            "A": "50ml量筒",
            "B": "50ml移液管",
            "C": "50ml滴定管",
            "D": "100ml量筒",
            "E": "50ml烧杯"
        },
        "answer": "B",
        "answer_text": "50ml移液管"
    },
    "2-5": {
        "text": "《中国药典》规定“精密称定”时，系指重量应准确至所取重量的（ ）",
        "options": {
            "A": "百分之一",
            "B": "千分之一",
            "C": "万分之一",
            "D": "百分之十",
            "E": "千分之三"
        },
        "answer": "B",
        "answer_text": "千分之一"
    },





    "3-1": {
        "text": "药事体系的基本职能有（）",
        "options": {
            "A": "培养药学人才",
            "B": "提供安全、有效、稳定、经济的药品",
            "C": "提供用药咨询服务",
            "D": "指导合理用药"
        },
        "answer": "ABCD",
        "answer_text": "A.培养药学人才, B.提供安全、有效、稳定、经济的药品, C.提供用药咨询服务, D.指导合理用药"
    },
    "3-2": {
        "text": "微观的药事管理包括 （）",
        "options": {
            "A": "药品质量管理",
            "B": "药学信息管理",
            "C": "药学服务管理",
            "D": "药学人员管理"
        },
        "answer": "ABCD",
        "answer_text": "A.药品质量管理, B.药学信息管理, C.药学服务管理, D.药学人员管理"
    },
    "3-3": {
        "text": "药事管理工作采用的手段有（）",
        "options": {
            "A": "政策手段",
            "B": "法律手段",
            "C": "技术手段",
            "D": "媒体监督手段"
        },
        "answer": "ABCD",
        "answer_text": "A.政策手段, B.法律手段, C.技术手段, D.媒体监督手段"
    },
    "3-4": {
        "text": "药事管理学科基础包括下面哪些学科（）",
        "options": {
            "A": "社会学",
            "B": "管理学",
            "C": "法学",
            "D": "经济学"
        },
        "answer": "ABCD",
        "answer_text": "A.社会学, B.管理学, C.法学, D.经济学"
    },
    "3-5": {
        "text": "根据工作领域不同，可以将药师分为：（）",
        "options": {
            "A": "社区药房药师",
            "B": "医疗保健机构药师",
            "C": "生产部门药师",
            "D": "流通领域药师"
        },
        "answer": "ABCD",
        "answer_text": "A.社区药房药师, B.医疗保健机构药师, C.生产部门药师, D.流通领域药师"
    },
    "3-6": {
        "text": "医疗机构药师的临床药学功能包括：（）",
        "options": {
            "A": "提供药学保健",
            "B": "开展药物治疗监测",
            "C": "开展药物利用评价",
            "D": "药物不良反应监测"
        },
        "answer": "ABCD",
        "answer_text": "A.提供药学保健, B.开展药物治疗监测, C.开展药物利用评价, D.药物不良反应监测"
    },
    "3-7": {
        "text": "社会药房药师的功能有：（）",
        "options": {
            "A": "供应合格药品",
            "B": "用药指导",
            "C": "管理药品",
            "D": "提供临床药学服务"
        },
        "answer": "ABC",
        "answer_text": "A.供应合格药品, B.用药指导, C.管理药品"
    },
    "3-8": {
        "text": "生产部门药师的功能有：（）",
        "options": {
            "A": "质量保证",
            "B": "质量控制",
            "C": "制定生产计划",
            "D": "追踪药品上市后的使用信息"
        },
        "answer": "ABCD",
        "answer_text": "A.质量保证, B.质量控制, C.制定生产计划, D.追踪药品上市后的使用信息"
    },
    "3-9": {
        "text": "执业西药师的考试科目包括：（）",
        "options": {
            "A": "药学专业知识一",
            "B": "药学专业知识二",
            "C": "药事管理与法规",
            "D": "综合知识与技能"
        },
        "answer": "ABCD",
        "answer_text": "A.药学专业知识一, B.药学专业知识二, C.药事管理与法规, D.综合知识与技能"
    },
    "3-10": {
        "text": "执业中药师的考试科目包括：（）",
        "options": {
            "A": "中药学专业知识一",
            "B": "中药学专业知识二",
            "C": "药事管理与法规",
            "D": "综合知识与技能"
        },
        "answer": "ABCD",
        "answer_text": "A.中药学专业知识一, B.中药学专业知识二, C.药事管理与法规, D.综合知识与技能"
    },
    "3-11": {
        "text": "临床药师的主要功能有：（）",
        "options": {
            "A": "药物治疗专家",
            "B": "药物信息主要来源",
            "C": "调剂药品",
            "D": "治疗结果评价和建议"
        },
        "answer": "ABD",
        "answer_text": "A.药物治疗专家, B.药物信息主要来源, D.治疗结果评价和建议"
    },
    "3-12": {
        "text": "执业药师继续教育分为下面几类：（）",
        "options": {
            "A": "必修",
            "B": "选修",
            "C": "必选",
            "D": "自修"
        },
        "answer": "ABD",
        "answer_text": "A.必修, B.选修, D.自修"
    },
    "3-13": {
        "text": "纳入《基本医疗保险药品目录》的药品应符合下列哪些原则？（）",
        "options": {
            "A": "临床必需",
            "B": "安全有效",
            "C": "价格合理",
            "D": "使用方便"
        },
        "answer": "ABCD",
        "answer_text": "A.临床必需, B.安全有效, C.价格合理, D.使用方便"
    },
    "3-14": {
        "text": "《基本医疗保险药品目录》所列药品包括（）",
        "options": {
            "A": "西药",
            "B": "中药材",
            "C": "中成药",
            "D": "中药饮片"
        },
        "answer": "ABC",
        "answer_text": "A.西药, B.中药材, C.中成药"
    },
    "3-15": {
        "text": "纳入《基本医疗保险药品目录》中“甲类目录”的药品是：",
        "options": {
            "A": "临床必需",
            "B": "使用广泛",
            "C": "疗效好",
            "D": "同类药品中价格低"
        },
        "answer": "ABCD",
        "answer_text": "A.临床必需, B.使用广泛, C.疗效好, D.同类药品中价格低"
    },
    "3-16": {
        "text": "纳入《基本医疗保险药品目录》中“乙类目录”的药品是：",
        "options": {
            "A": "临床治疗选择使用",
            "B": "疗效好",
            "C": "同类药品价格略高",
            "D": "同类药品价格低"
        },
        "answer": "ABC",
        "answer_text": "A.临床治疗选择使用, B.疗效好, C.同类药品价格略高"
    },
    "3-17": {
        "text": "药品作为特殊商品，其特殊性体现在：",
        "options": {
            "A": "专属性",
            "B": "两重性",
            "C": "质量的重要性",
            "D": "时限性"
        },
        "answer": "ABCD",
        "answer_text": "A.专属性, B.两重性, C.质量的重要性, D.时限性"
    },
    "3-18": {
        "text": "下列哪些属于药品的质量特征：",
        "options": {
            "A": "安全性",
            "B": "有效性",
            "C": "稳定性",
            "D": "均一性"
        },
        "answer": "ABCD",
        "answer_text": "A.安全性, B.有效性, C.稳定性, D.均一性"
    },
    "3-19": {
        "text": "药品质量监督检验的性质是：",
        "options": {
            "A": "盈利性",
            "B": "公正性",
            "C": "权威性",
            "D": "仲裁性"
        },
        "answer": "BCD",
        "answer_text": "B.公正性, C.权威性, D.仲裁性"
    },
    "3-20": {
        "text": "非处方药的遴选原则为：",
        "options": {
            "A": "应用安全",
            "B": "疗效确切",
            "C": "质量稳定",
            "D": "应用方便"
        },
        "answer": "ABCD",
        "answer_text": "A.应用安全, B.疗效确切, C.质量稳定, D.应用方便"
    },
    "3-21": {
        "text": "化学药品的名称包括：",
        "options": {
            "A": "通用名",
            "B": "化学名",
            "C": "英文名",
            "D": "汉语拼音"
        },
        "answer": "ABCD",
        "answer_text": "A.通用名, B.化学名, C.英文名, D.汉语拼音"
    },
    "3-22": {
        "text": "中药材的名称包括：",
        "options": {
            "A": "英文名",
            "B": "中文名",
            "C": "汉语拼音",
            "D": "拉丁名"
        },
        "answer": "ACD",
        "answer_text": "A.英文名, C.汉语拼音, D.拉丁名"
    },
    "3-23": {
        "text": "新药研发参照下列原则选择新药品种：",
        "options": {
            "A": "市场前景好",
            "B": "技术水平高",
            "C": "不侵犯知识产权",
            "D": "适合企业产品结构"
        },
        "answer": "ABCD",
        "answer_text": "A.市场前景好, B.技术水平高, C.不侵犯知识产权, D.适合企业产品结构"
    },
    "3-24": {
        "text": "新药的性状包括药物的：",
        "options": {
            "A": "色",
            "B": "味",
            "C": "嗅",
            "D": "外观"
        },
        "answer": "ABCD",
        "answer_text": "A.色, B.味, C.嗅, D.外观"
    },
    "3-25": {
        "text": "新药剂型的确立取决于：",
        "options": {
            "A": "作用部位",
            "B": "药物性质",
            "C": "生物利用度",
            "D": "给药途径"
        },
        "answer": "ABCD",
        "answer_text": "A.作用部位, B.药物性质, C.生物利用度, D.给药途径"
    },
    "3-26": {
        "text": "中药注册按照（）进行分类。",
        "options": {
            "A": "中药创新药",
            "B": "中药改良型新药",
            "C": "古代经典名方中药复方制剂",
            "D": "同名同方药"
        },
        "answer": "ABCD",
        "answer_text": "A.中药创新药, B.中药改良型新药, C.古代经典名方中药复方制剂, D.同名同方药"
    },
    "3-27": {
        "text": "新药的毒理学研究主要包括：",
        "options": {
            "A": "全身用药毒性试验",
            "B": "局部用药毒性试验",
            "C": "特殊毒理研究",
            "D": "药物依赖性试验"
        },
        "answer": "ABC",
        "answer_text": "A.全身用药毒性试验, B.局部用药毒性试验, C.特殊毒理研究"
    },
    "3-28": {
        "text": "特殊毒理研究包括：",
        "options": {
            "A": "致突变试验",
            "B": "致癌试验",
            "C": "生殖毒性试验",
            "D": "急性毒性试验"
        },
        "answer": "ABCD",
        "answer_text": "A.致突变试验, B.致癌试验, C.生殖毒性试验, D.急性毒性试验"
    },
    "3-29": {
        "text": "药品注册按照（）进行分类注册管理。",
        "options": {
            "A": "中药",
            "B": "化学药",
            "C": "生物制品",
            "D": "疫苗"
        },
        "answer": "ABCD",
        "answer_text": "A.中药, B.化学药, C.生物制品, D.疫苗"
    },
    "3-30": {
        "text": "药品经营活动的特点体现为：",
        "options": {
            "A": "单一性",
            "B": "综合性",
            "C": "专业性",
            "D": "政策性"
        },
        "answer": "ABCD",
        "answer_text": "A.单一性, B.综合性, C.专业性, D.政策性"
    },
    "3-31": {
        "text": "《药品经营许可证管理办法》适用于：",
        "options": {
            "A": "药品经营许可证发证",
            "B": "药品经营许可证换证",
            "C": "药品经营许可证变更",
            "D": "药品经营许可证监督管理"
        },
        "answer": "ABCD",
        "answer_text": "A.药品经营许可证发证, B.药品经营许可证换证, C.药品经营许可证变更, D.药品经营许可证监督管理"
    },
    "3-32": {
        "text": "医疗机构储存药品须采取下列哪些措施来保证药品质量：",
        "options": {
            "A": "冷藏",
            "B": "防冻",
            "C": "防潮",
            "D": "避光"
        },
        "answer": "ABCD",
        "answer_text": "A.冷藏, B.防冻, C.防潮, D.避光"
    },
    "3-33": {
        "text": "社会药房从业人员按功能分为如下等级：",
        "options": {
            "A": "店员",
            "B": "助理药师",
            "C": "药师",
            "D": "执业药师"
        },
        "answer": "ABCD",
        "answer_text": "A.店员, B.助理药师, C.药师, D.执业药师"
    },
    "3-34": {
        "text": "药品经营企业的库区环境应该：",
        "options": {
            "A": "无污染源",
            "B": "地面平整",
            "C": "无积水",
            "D": "无杂草"
        },
        "answer": "ABCD",
        "answer_text": "A.无污染源, B.地面平整, C.无积水, D.无杂草"
    },
    "3-35": {
        "text": "药品经营企业仓库可以分为：",
        "options": {
            "A": "合格品库",
            "B": "不合格库",
            "C": "发货库",
            "D": "退货库"
        },
        "answer": "ABCD",
        "answer_text": "A.合格品库, B.不合格库, C.发货库, D.退货库"
    },
    "3-36": {
        "text": "医疗机构包括：",
        "options": {
            "A": "医院",
            "B": "卫生院",
            "C": "门诊部",
            "D": "卫生室"
        },
        "answer": "ABCD",
        "answer_text": "A.医院, B.卫生院, C.门诊部, D.卫生室"
    },
    "3-37": {
        "text": "医疗机构临床药学业务包括：",
        "options": {
            "A": "治疗药物监测",
            "B": "药物信息收集",
            "C": "合理用药咨询",
            "D": "不良反应监测"
        },
        "answer": "ABCD",
        "answer_text": "A.治疗药物监测, B.药物信息收集, C.合理用药咨询, D.不良反应监测"
    },
    "3-38": {
        "text": "医疗机构的调剂部门可以分为：",
        "options": {
            "A": "门诊调剂",
            "B": "住院部调剂",
            "C": "急诊调剂",
            "D": "中药调剂"
        },
        "answer": "ABCD",
        "answer_text": "A.门诊调剂, B.住院部调剂, C.急诊调剂, D.中药调剂"
    },
    "3-39": {
        "text": "调剂处方的“四查十对”中的“四查”是指：",
        "options": {
            "A": "查处方",
            "B": "查药品",
            "C": "查配伍禁忌",
            "D": "查用药合理性"
        },
        "answer": "ABCD",
        "answer_text": "A.查处方, B.查药品, C.查配伍禁忌, D.查用药合理性"
    },
    "3-40": {
        "text": "医疗机构药学技术人员的技术职务可以分为：",
        "options": {
            "A": "主任药师",
            "B": "副主任药师",
            "C": "主管药师",
            "D": "药师"
        },
        "answer": "ABCD",
        "answer_text": "A.主任药师, B.副主任药师, C.主管药师, D.药师"
    },
    "3-41": {
        "text": "一级保护野生药材物种包括：",
        "options": {
            "A": "禁止采猎",
            "B": "必须持有《采药证》，按照批准的计划采猎、收购",
            "C": "属于自然淘汰的，其药用部分由各级药材公司负责经营管理，限量出口",
            "D": "不得出口",
            "E": "限量出口"
        },
        "answer": "ACD",
        "answer_text": "A.禁止采猎, C.属于自然淘汰的，其药用部分由各级药材公司负责经营管理，限量出口, D.不得出口"
    },
    "3-42": {
        "text": "申请中药一级保护的条件是：",
        "options": {
            "A": "对特定疾病有显著疗效的",
            "B": "对特定疾病有特殊疗效的",
            "C": "用于预防和治疗特殊疾病的",
            "D": "相当于国家一级保护野生药材物种的人工制品",
            "E": "从天然药物中提取的特殊制剂"
        },
        "answer": "ABC",
        "answer_text": "A.对特定疾病有显著疗效的, B.对特定疾病有特殊疗效的, C.用于预防和治疗特殊疾病的"
    },
    "3-43": {
        "text": "国家一级保护的野生动植物药材有：",
        "options": {
            "A": "虎骨",
            "B": "豹骨",
            "C": "羚羊角",
            "D": "鹿茸"
        },
        "answer": "ABCD",
        "answer_text": "A.虎骨, B.豹骨, C.羚羊角, D.鹿茸"
    },
    "4-1": {
        "text": "我国执业药师：",
        "options": {},
        "answer": "",
        "answer_text": "我国执业药师：执业药师是指经全国统一考试合格，取得《执业药师资格证书》，并经注册登记，在药品生产、经营、使用单位中执业的药学技术人员。英文：Licensed Pharmacist。分为：执业中药师和执业西药师"
    },
    "4-2": {
        "text": "药品：",
        "options": {},
        "answer": "",
        "answer_text": "药品是指用于预防、治疗、诊断人的疾病，有目的地调节人的生理机能并规定有适应症或者功能主治、用法和用量的物质，包括中药材、中药饮片、中成药、化学原料药及其制剂、抗生素、生化药品、放射性药品、血清、疫苗、血液制品和诊断药品等。"
    },
    "4-3": {
        "text": "新药：",
        "options": {},
        "answer": "",
        "answer_text": "新药是指未曾在中国境内上市销售的药品。"
    },
    "4-4": {
        "text": "处方药：",
        "options": {},
        "answer": "",
        "answer_text": "处方药是指凭执业医师和执业助理医师处方方可购买、调配和使用的药品。"
    },
    "4-5": {
        "text": "国家基本药物：",
        "options": {},
        "answer": "",
        "answer_text": "国家基本药物是指国家为了使本国公众获得基本医疗保障，有国家从目前应用的各类药物中经过科学评价而遴选出具有代表性的、可供疾病预防与治疗时优先考虑选择的药物。"
    },
    "4-6": {
        "text": "非处方药：",
        "options": {},
        "answer": "",
        "answer_text": "非处方药是指由国务院药品监督管理部门公布的，不需要凭执业医师和执业助理医师处方，消费者可以自行判断、购买和使用的药品。"
    },
    "4-7": {
        "text": "药品批发企业：",
        "options": {},
        "answer": "",
        "answer_text": "药品批发企业是指将购进的药品销售给药品生产、经营企业、医疗机构的药品经营企业。"
    },
    "4-8": {
        "text": "药品零售企业：",
        "options": {},
        "answer": "",
        "answer_text": "药品零售企业是将购进的药品直接销售给终端消费者的药品经营企业。"
    },
    "4-9": {
        "text": "药品注册：",
        "options": {},
        "answer": "",
        "answer_text": "药品注册是指药品注册申请人依照法定程序和相关要求提出药物临床试验、药品上市许可、再注册等申请以及补充申请，药品监督管理部门基于法律法规和现有科学认知进行安全性、有效性和质量可控性等审查，决定是否同意其申请的活动。"
    },
    "4-10": {
        "text": "药物临床试验：",
        "options": {},
        "answer": "",
        "answer_text": "药物临床试验是指以药品上市注册为目的，在人体中进行的药物研究，旨在确定药物的安全性和有效性。"
    },
    "4-11": {
        "text": "药品标准复核：",
        "options": {},
        "answer": "",
        "answer_text": "药品标准复核是指对申请人申报药品标准中设定项目的科学性、检验方法的可行性、质控指标的合理性等进行的实验室评估。"
    },
    "4-12": {
        "text": "定点零售药店：",
        "options": {},
        "answer": "",
        "answer_text": "定点零售药店是经统筹地区劳动保障行政部门审查，并经社会保险经办机构确定的，为城镇职工基本医疗保险参保人员提供处方外配服务的零售药店。"
    },
    "4-13": {
        "text": "处方外配：",
        "options": {},
        "answer": "",
        "answer_text": "处方外配是指参保人员持定点医疗机构处方，在定点零售药店购药的行为。"
    },
    "4-14": {
        "text": "医师处方：",
        "options": {},
        "answer": "",
        "answer_text": "医师处方是指由注册的执业医师和执业助理医师在诊疗活动中为患者开具的、由取得药学专业技术职务任职资格的药学专业技术人员审核、调配、核对，并作为患者用药凭证的医疗文书。处方还包括医疗机构病区用药医嘱单。"
    },
    "4-15": {
        "text": "调剂：",
        "options": {},
        "answer": "",
        "answer_text": "调剂是指配药、配方、发药的过程，又称为调配处方。"
    },
    "4-16": {
        "text": "药品有效期：",
        "options": {},
        "answer": "",
        "answer_text": "药品有效期是指药品在一定的存储条件下，能够保证其质量合格的期限。"
    },
    "4-17": {
        "text": "精神药品：",
        "options": {},
        "answer": "",
        "answer_text": "精神药品是指列入精神药品目录的药品和其他物质。精神药品分为第一类精神药品和第二类精神药品。"
    },
    "4-18": {
        "text": "中药材：",
        "options": {},
        "answer": "",
        "answer_text": "中药材指药用植物、动物、矿物的药用部分采收后经产地初加工形成的原料药材。"
    },
    "4-19": {
        "text": "中药饮片：",
        "options": {},
        "answer": "",
        "answer_text": "中药饮片是指在中医药理论指导下，根据辨证施治和调剂、制剂的需要，对中药材进行特殊加工炮制后的制成品。"
    },
    "4-20": {
        "text": "中成药：",
        "options": {},
        "answer": "",
        "answer_text": "中成药以中药材为原料，在中医药理论指导下，按规定的处方和方法，加工制成的一定剂型，标明药物作用、适应证、用法用量，供医生、患者直接使用的药物，主要有丸、散、膏、丹、露、酒、锭、片剂、冲剂、糖浆等不同的剂型。"
    },
    "5-1": {
        "text": "药事管理学的研究内容包括哪些方面？",
        "options": {},
        "answer": "",
        "answer_text": "药事管理学的研究内容包括药事管理体制、药品监督管理、药品法制管理、药品注册管理、药品生产和经营管理、药品使用管理、药品信息管理、药品知识产权保护、药学技术人员管理等方面。"
    },
    "5-2": {
        "text": "国家基本药物遴选原则是什么？",
        "options": {},
        "answer": "",
        "answer_text": "国家基本药物遴选原则包括防治必需、安全有效、价格合理、使用方便、中西药并重、基本保障、临床首选、基层能够配备等。"
    },
    "5-3": {
        "text": "简述《药品管理法》的立法目的、适用范围。",
        "options": {},
        "answer": "",
        "answer_text": "《药品管理法》的立法目的是加强药品监督管理，保证药品质量，保障人体用药安全，维护人民身体健康和用药的合法权益。适用范围包括在中华人民共和国境内从事药品的研制、生产、经营、使用和监督管理的单位或个人，必须遵守该法。"
    },
    "5-4": {
        "text": "开办药品生产企业必须具备什么条件？",
        "options": {},
        "answer": "",
        "answer_text": "《药品管理法》第十五条：具有依法经过资格认定的药学技术人员；具有与所经营药品相适应的营业场所、设备、仓储设施、卫生环境；具有与所经营药品相适应的质量管理机构或者人员；具有保证所经营药品质量的规章制度。"
    },
    "5-5": {
        "text": "什么是假药、劣药？",
        "options": {},
        "answer": "",
        "answer_text": "假药：药品所含成份与国家药品标准规定的成份不符的；以非药品冒充药品或者以他种药品冒充此种药品的。有下列情形之一的药品，按假药论处：国务院药品监督管理部门规定禁止使用的；依照本法必须批准而未经批准生产、进口，或者依照本法必须检验而未经检验即销售的；变质的；被污染的；使用依照本法必须取得批准文号而未取得批准文号的原料药生产的；所标明的适应症或者功能主治超出规定范围的。劣药：药品成份的含量不符合国家药品标准的。有下列情形之一的药品，按劣药论处：未标明有效期或者更改有效期的；不注明或者更改生产批号的；超过有效期的；直接接触药品的包装材料和容器未经批准的；擅自添加着色剂、防腐剂、香料、矫味剂及辅料的；其他不符合药品标准规定的。"
    },
    "5-6": {
        "text": "疫苗的批签发制度是什么意思？",
        "options": {},
        "answer": "",
        "answer_text": "每批疫苗销售前或者进口时，应当经国务院药品监督管理部门指定的批签发机构按照相关技术要求进行审核、检验。符合要求的，发给批签发证明；不符合要求的，发给不予批签发通知书。"
    },
    "5-7": {
        "text": "简述药品生产的特点。",
        "options": {},
        "answer": "",
        "answer_text": "药品生产的特点包括准入条件严格、质量要求高、环境保护迫切、生产技术先进、生产过程复杂。"
    },
    "5-8": {
        "text": "简述药品生产企业的特征。",
        "options": {},
        "answer": "",
        "answer_text": "药品生产企业的特征包括经济性、盈利性、独立性。"
    },
    "5-9": {
        "text": "药品分类储存保管中的“六分开”包括哪些方面？",
        "options": {},
        "answer": "",
        "answer_text": "药品分类储存保管中的“六分开”包括以下方面：\n1.药品与非药品分开\n2.处方药与非处方药分开\n3.特殊管理药品与一般药品分开\n4.有储存温度要求的与常温药品分开\n5.易窜味的药品、中药材、中药饮片以及危险药品与其他药品分开\n6.外用药与其他方法服用的药品分开"
    },
    "5-10": {
        "text": "哪些药品不得发布广告？",
        "options": {},
        "answer": "",
        "answer_text": "以下药品不得发布广告：\n1.麻、精、毒、放药品\n2.药品监督管理部门明令停止或禁止生产、销售和使用的药品\n3.医疗机构配制的制剂\n4.军队特需药品\n5.批准试生产的药品"
    },
    "5-11": {
        "text": "医药专利包括哪些类型？",
        "options": {},
        "answer": "",
        "answer_text": "医药专利包括以下类型：\n1. 医药发明专利\n2. 实用新型专利\n3. 外观设计专利"
    }
}

def display_questions(start, end):
    st.title('药事管理学试卷展示')
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
    st.title("药剂学试卷展示应用")
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


