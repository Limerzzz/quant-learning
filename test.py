# 导入akshare库
import akshare as ak

# 获取沪深300ETF的历史数据
stock_data = ak.fund_etf_hist_em(
    symbol="510300", period="daily", start_date="20210101", end_date="20240101")

# 打印数据
print(stock_data)
