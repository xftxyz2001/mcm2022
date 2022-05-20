import numpy as np
import pandas as pd
import math


def computeCorrelation(x, y):
    '''
    用于计算R方，x、y均为矩阵
    '''
    xbar = np.nanmean(x)
    ybar = np.nanmean(y)
    SR = 0
    varX = 0
    varY = 0
    for i in range(0, len(x)):  # 多少实例
        diffxx = x[i] - xbar
        diffyy = y[i] - ybar
        SR += (diffxx * diffyy)
        varX += diffxx ** 2  # 求平方然后累计起来
        varY += diffyy ** 2  # 求平方然后累计起来
    ST = math.sqrt(varX * varY)
    # 返回R方=方差/总方差
    return SR / ST


def solve_ques2(pollution, Air_condition, AQI):
    '''
    以行 为污染物与API，列为天气特征生成R方的表格
    '''
    # 取出附件一中表二每一个空气特征的数组
    Air_condition_arry = Air_condition
    Air_condition_items = ['温度', '湿度', '气压', '风速', '风向']
    pollution_arry = pollution
    pollution_items = ['so2', 'no2', 'pm10', 'pm2dot5', 'co', 'o3']
    R_squre_ans = []
    # PCC_ans = []
    df_R = pd.DataFrame({'Condition': Air_condition_items})
    # 求每个天气特征与污染物的R方,i为列，j为行，并追加到表中
    for i in range(len(pollution_items)):
        for j in range(len(Air_condition_items)):
            R_squre_ans.append(computeCorrelation(
                Air_condition_arry[j], pollution_arry[i]))
        df_R.insert(i+1, pollution_items[i], R_squre_ans)
        R_squre_ans = []
    # 求天气特征与AQI的R方，并追加到表中
    for j in range(len(Air_condition_items)):
        R_squre_ans.append(computeCorrelation(Air_condition_arry[j], AQI))
    df_R.insert(len(pollution_items)+1, 'AQI', R_squre_ans)
    df_R.to_excel('R_Square.xlsx', sheet_name='sheet1', index=False)


if __name__ == '__main__':
    pollution = np.loadtxt('pollution.txt')
    Air_condition = np.loadtxt('Air_condition.txt')
    AQI = np.loadtxt('AQI.txt')
    solve_ques2(pollution, Air_condition, AQI)
