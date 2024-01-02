import pandas as pd

file_path = 'P:\Bài tập lab\DHKL16A1HN-LAB3\DATA-LAB3_CSV\stocks1.csv'
data = pd.read_csv(file_path)

print("Dữ liệu stocks1:\n",data)
print("------------------------------------------------------")

# 1. Kiểm tra xem trong stocks1 có dữ liệu Null nào không.
print("Số dữ liệu Null có trong stocks1: \n",data.isnull().sum())
print("------------------------------------------------------")

# 2. Thay thế dữ liệu Null ở cột high bằng giá trị trung bình của cột high.
trung_binh_high = data['high'].mean()
data['high']=data['high'].fillna(trung_binh_high)


# 3. Thay thế dữ liệu Null ở cột low bằng giá trị trung bình của cột low
mean_low = data['low'].mean()
data['low']=data['low'].fillna(mean_low)
print("Thay thế dữ liệu Null ở cột high,low bằng giá trị trung bình của cột high,low:")
print(data)
print("------------------------------------------------------")

# 4. Hiển thị thông tin tổng quan để xác nhận không còn dữ liệu Null.
print(data.info())
