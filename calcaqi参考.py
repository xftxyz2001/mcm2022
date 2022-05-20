import copy
import json
import numpy as np
import pandas as pd

if __name__ == '__main__':
    """此为1h的AQI计算代码，24h的只需要更换Idata即可"""
    qua = [0, 50, 100, 150, 200, 300, 400, 500]
    data = pd.read_json("a_daily.json")
    print(round(2.50))
    print(type(data))
    data1 = data.values
    print(type(data1))
    IAQI = list(np.zeros(len(data1[0][0]["PM2.5"])))
    print((data1[0][0]).keys())
    Data = np.array(
        [data1[0][0]["PM2.5"], data1[0][0]["PM10"], data1[0][0]["SO2"], data1[0][0]["NO2"], data1[0][0]["CO"],
         data1[0][0]["O3"]]).reshape(len(data1[0][0]["PM2.5"]), 6)
    Idata = [
        [0, 35, 75, 115, 150, 250, 350, 500],  # PM2.5 24小时平均
        [0, 50, 150, 250, 350, 420, 500, 600],  # （PM10）24小时平均
        [0, 150, 500, 650, 800],  # so2
        [0, 100, 200, 700, 1200, 2340, 3090, 3840],  # no2
        [0, 5, 10, 35, 60, 90, 120, 150],  # co
        [0, 160, 200, 300, 400, 800, 1000, 1200]  # o3
    ]
    # Idata = [
    #     [0, 35, 75, 115, 150, 250, 350, 500] , # PM2.5
    #     [0, 50, 150, 250, 350, 420, 500, 600],  # （PM10）
    #     [0, 50,150,475,800,1600,2100,2620],  # (SO2)
    #     [0,40,80,180,280,565,750,940],  #
    #     [0, 2,4,14,24,36,48,60],  # （CO）
    #     [0, 100,160,215,265,800]  # (O3)
    # ]
    # 上为24hAQI计算中需要用到的Idata
    T_IA = 0
    i = j = k = 0
    print(len(Idata))
    for i in range(len(Idata)):
        T_data = Data[:, i]
        T_Idata = Idata[i]
        for j in range(len(T_data)):
            for k in range(1, len(T_Idata)):
                if T_Idata[k] > T_data[j]:
                    break
            if k == (len(T_Idata) - 1) and T_Idata[k] < T_data[j]:
                T_IA = T_Idata[k]
            else:
                T_IA = int(round((((qua[k] - qua[k - 1]) / (T_Idata[k] - T_Idata[k - 1])) * (
                    T_data[j] - T_Idata[k - 1]) + qua[k - 1]) + 0.5))
            if T_IA > IAQI[j]:
                IAQI[j] = T_IA
    data1[0][0]["AQI"] = (IAQI)
    data2 = copy.deepcopy(data1[0][0]['date'])
    data1[0][0].pop("date")
    data1[0][0]["date"] = data2
    filename = "IAdata4.json"
    Dic = {}

    Dic["air_data"] = data1[0].tolist()
    with open(filename, 'w') as file_obj:
        json.dump(Dic, file_obj)
