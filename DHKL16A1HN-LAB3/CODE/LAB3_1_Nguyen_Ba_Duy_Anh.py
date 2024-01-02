import pandas as pd

#1. Đọc file stocks1.csv vào DataFrame stocks1.
file_path = 'P:\Bài tập lab\DHKL16A1HN-LAB3\DATA-LAB3_CSV\stocks1.csv'
data = pd.read_csv(file_path)

#2. Hiển thị 5 dòng đầu tiên của stocks1.
print("\n Hiển thị 5 dòng đầu tiên của stocks1:\n",data[0:5])
print("------------------------------------------------------")

#3. Hiển thị kiểu dữ liệu (dtype) của mỗi cột trong stocks1.
print("Hiển thị kiểu dữ liệu(dtype) của mỗi cột trong stocks1:\n",data.dtypes)
print("------------------------------------------------------")

#4. Xem thông tin tổng quan (info) của stocks1
print("Thông tin tổng quan(infor) của stocks1:\n",data.info())
