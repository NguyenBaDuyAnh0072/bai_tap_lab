# LAB 3.5: SỬ DỤNG MULTIINDEX VÀ GROUPBY

import pandas as pd

data1 = pd.read_csv('P:\Bài tập lab\DHKL16A1HN-LAB3\DATA-LAB3_CSV\stocks1.csv')
data2 = pd.read_csv('P:\Bài tập lab\DHKL16A1HN-LAB3\DATA-LAB3_CSV\stocks2.csv')
stocks=pd.concat([data1,data2])

# 1. Tạo MultiIndex cho DataFrame stocks bằng cách sử dụng cột date và symbol làm chỉ mục.
multi_index=stocks.set_index(['date', 'symbol'])

# 2. Sử dụng GroupBy để tính giá trung bình (open, high, low, close) và volume trung bình cho mỗi ngày, cho mỗi mã chứng khoán.
value_tb = multi_index.groupby(level=['date', 'symbol']).mean()

# 3. Sắp xếp dữ liệu theo ngày và mã chứng khoán.
value_tb=value_tb.sort_index()

# 4. Hiển thị kết quả cho 5 ngày đầu tiên.
print("Hiển thị kết quả cho 5 ngày đầu tiên:\n",value_tb[0:5])