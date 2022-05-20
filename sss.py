from aqicalc import AQICalculator

a = AQICalculator('待处理数据.xlsx', 'Sheet2')

a.calc('处理后数据.xlsx')
