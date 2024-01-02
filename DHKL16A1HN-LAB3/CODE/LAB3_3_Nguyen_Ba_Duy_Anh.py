import pandas as pd

# 1. Đọc file stocks2.csv vào DataFrame stocks2
path_stocks1 = 'P:\Bài tập lab\DHKL16A1HN-LAB3\DATA-LAB3_CSV\stocks1.csv'
path_stocks2='P:\Bài tập lab\DHKL16A1HN-LAB3\DATA-LAB3_CSV\stocks2.csv'
data1 = pd.read_csv(path_stocks1)
data2 = pd.read_csv(path_stocks2)

# 2. Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
stocks=pd.concat([data1,data2])
def stocks1_2():
    return stocks

# 3. Tính giá trung bình (open, high, low, close) cho mỗi ngày.
trung_binh = stocks.groupby('date')[['open', 'high', 'low', 'close']].mean()

# 4. Hiển thị 5 dòng đầu tiên của kết quả
print("Hiển thị 5 dòng đầu tiên của kết quả:\n",trung_binh[0:5])
