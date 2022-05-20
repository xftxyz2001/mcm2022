from aqicalc import AQICalculator

aqicalc = AQICalculator('A.xlsx', '监测点A逐日污染物浓度实测数据')
aqicalc.calc('监测点A日AQI及首要污染物')

aqicalc = AQICalculator('BC.xlsx', '监测点B逐日污染物浓度实测数据')
aqicalc.calc('监测点B日AQI及首要污染物')

aqicalc = AQICalculator('BC.xlsx', '监测点C逐日污染物浓度实测数据')
aqicalc.calc('监测点C日AQI及首要污染物')

