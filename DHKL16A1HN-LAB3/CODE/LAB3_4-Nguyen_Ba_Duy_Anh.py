import pandas as pd

# 1. Đọc file companies.csv vào DataFrame companies
companies = pd.read_csv('P:\Bài tập lab\DHKL16A1HN-LAB3\DATA-LAB3_CSV\companies.csv')
data1 = pd.read_csv('P:\Bài tập lab\DHKL16A1HN-LAB3\DATA-LAB3_CSV\stocks1.csv')
data2 = pd.read_csv('P:\Bài tập lab\DHKL16A1HN-LAB3\DATA-LAB3_CSV\stocks2.csv')
stocks=pd.concat([data1,data2])


# 2. Hiển thị 5 dòng đầu tiên của companies
print("Hiển thị 5 dòng đầu tiên của companies:\n",companies[0:5])

# 3. Kết hợp stocks (đã tạo từ bài 3) và companies dựa trên cột chung là symbol.
ket_hop_data = pd.merge(stocks, companies, on='symbol')
print("Dữ liệu stocks và companies dựa trên cột chung là symbol:\n",ket_hop_data)

# 4. Tính giá đóng cửa (close) trung bình cho mỗi công ty
gia_dong_cua = ket_hop_data.groupby('symbol')['close'].mean()

# 5. Hiển thị kết quả cho 5 công ty đầu tiên
print("Hiển thị kết quả cho 5 công ty đầu tiên:\n",gia_dong_cua[0:5])
