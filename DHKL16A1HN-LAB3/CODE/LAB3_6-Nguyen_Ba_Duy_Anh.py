# LAB 3.6: TẠO VÀ PHÂN TÍCH PIVOT TABLE
import pandas as pd
data1 = pd.read_csv('P:\Bài tập lab\DHKL16A1HN-LAB3\DATA-LAB3_CSV\stocks1.csv')
data2 = pd.read_csv('P:\Bài tập lab\DHKL16A1HN-LAB3\DATA-LAB3_CSV\stocks2.csv')
stocks=pd.concat([data1,data2])

# 1. Tạo Pivot Table từ DataFrame stocks với date làm chỉ mục, symbol làm cột, và giá trị trung bình của close làm giá trị
pivot_table = stocks.pivot_table(values='close',index='date', columns='symbol',  aggfunc='mean')
print("PIVOT TABLE:\n",pivot_table)

# 2. Thêm một cột tính tổng volume giao dịch cho mỗi mã chứng khoán (symbol)
pivot_table = stocks.groupby('symbol')['volume'].sum()


# Nhiệm vụ 3: Sắp xếp Pivot Table dựa trên tổng volume giao dịch, từ cao xuống thấp.
pivot_table = pivot_table.sort_values(ascending=False)

print("---------------------------------------------------------------")
# Nhiệm vụ 4: Hiển thị kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất.
print("Hiển thị kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất:\n",pivot_table[0:5])