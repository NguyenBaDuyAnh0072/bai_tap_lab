import sqlite3

# 1. Tạo và Kết Nối với CSDL: Sử dụng SQLite3 trong Python để tạo và kết nối với product.db.
sql=sqlite3.connect('P:\Bài tập lab\DHKL16A1HN-LAB4\DATA-LAB4\product.db')

cursor=sql.cursor()

# 2. Tạo Bảng product: Xây dựng và thực thi lệnh SQL để tạo bảng product với các trường 
# như Id, Name, Price, Amount
cursor.execute('''
               CREATE TABLE IF NOT EXISTS product(
                   Id INTEGER PRIMARY KEY,
                   Name Text NOT NULL,
                   Price REAL NOT NULL,
                   Amount INTEGER NOT NULL)''')


# 3. Phát Triển Các Chức Năng: Xây dựng các hàm Python để thực hiện các chức năng như 
# thêm, hiển thị, tìm kiếm, cập nhật và xóa sản phẩm.

# THÊM
def them(sql,Name,Price,Amount):
    cursor=sql.cursor()
    cursor.execute("INSERT INTO product(Name,Price,Amount) VALUES(?,?,?)",(Name,Price,Amount))
    sql.commit()
    print("Đã thêm sản phẩm")

# HIỂN THỊ
def hien_thi(sql):
    cursor=sql.cursor()
    cursor.execute("SELECT * FROM product")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
        
# TÌM KIẾM
def tim_kiem(sql,Name):
    cursor=sql.cursor()
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?",('%' + Name +'%',))
    rows=cursor.fetchall()
    for row in rows:
        print(row)
        
# CẬP NHẬT        
def cap_nhat(sql,Name,Price,Amount,Id):
    cursor=sql.cursor()
    cursor.execute("UPDATE product SET Name=?,Price=?,Amount=? Where Id=?",(Name,Price,Amount,Id))
    sql.commit()   
    
# XÓA
def xoa(sql,Id):
    cursor=sql.cursor()
    cursor.execute("DELETE FROM product Where Id=?",(Id))
    sql.commit()
    
# HIỂN THỊ CHỨC NĂNG
while True:
    print("\n1. THÊM SẢN PHẨM")
    print("2. HIỂN THỊ SẢN PHẨM")
    print("3. TÌM KIẾM SẢN PHẨM")
    print("4. CẬP NHẬT SẢN PHẨM")
    print("5. XÓA SẢN PHẨM")
    print("6. THOÁT")
    
    lua_chon = input("Nhập lựa chọn của bạn: ")

    if lua_chon == '1':
        Name = input("Nhập tên sản phẩm: ")
        Price = float(input("Nhập giá sản phẩm: "))
        Amount = int(input("Nhập số lượng sản phẩm: "))
        them(sql,Name,Price,Amount)
        
    if lua_chon == '2':
        hien_thi(sql)
        
    if lua_chon == '3':
        Name = input("Nhập tên sản phẩm cần tìm: ")
        tim_kiem(sql,Name)
        
    if lua_chon=='4':
        Name = input("Nhập tên sản phẩm: ")
        Price = float(input("Nhập giá sản phẩm: "))
        Amount = int(input("Nhập số lượng sản phẩm: "))
        Id=int(input("Nhập Id sản phẩm:"))
        cap_nhat(sql,Name,Price,Amount,Id)
        
    if lua_chon=='5':
        Id=input("Nhập Id sản phẩm:")
        xoa(sql,Id)
        
    if lua_chon == '6':
        print("Đang thoát chương trình...")
        break

cursor.close()
sql.close()