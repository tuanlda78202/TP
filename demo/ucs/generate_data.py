import pandas as pd

def create_data_A_star(start,goal):
    data_neighbor={'Lai Chau':['Dien Bien','Lao Cai','Son La','Yen Bai'],\
                'Yen Bai':['Lao Cai','Lai Chau','Son La','Hà Giang','Phu Tho','Tuyen Quang'],\
                'Dien Bien':['Lai Chau','Son La'],\
                'Thanh Hoa':['Son La','Nghe An','Ninh Binh','Hoa Binh'],
                'Nghe An':['Ha Tinh','Thanh Hoa'],\
                'Quang Binh':['Ha Tinh','Quang Tri'] ,\
                'Ha Tinh':['Nghe An','Quang Binh'],\
                'Quang Tri':['Quang Binh','Hue'],\
                'Hue':['Quang Tri','Da Nang'],\
               'Da Nang':['Hue','Quang Nam'],\
                'Quang Nam':['Da Nang','Kon Tum','Quang Ngai'],\
                'Kon Tum':['Quang Nam','Quang Ngai','Gia Lai'],\
                'Quang Ngai':['Kon Tum','Quang Nam','Binh Dinh'],\
                'Gia Lai':['Kon Tum','Binh Dinh','Phu Yen','Dak Lak'],\
                'Binh Dinh':['Quang Ngai','Gia Lai','Phu Yen'],\
                'Dak Lak':['Dak Nong','Lam Dong','Khanh Hoa','Phu Yen','Gia Lai'],\
                'Phu Yen':['Gia Lai','Binh Dinh','Dak Lak','Khanh Hoa'],\
                'Khanh Hoa':['Dak Lak','Phu Yen','Lam Dong','Ninh Thuan'],\
                'Dak Nong':['Dak Lak','Lam Dong','Binh Phuoc'],\
                'Lam Dong':['Dak Lak','Dak Nong','Binh Phuoc','Dong Nai','Binh Thuan','Ninh Thuan','Khanh Hoa'],\
                'Ninh Thuan':['Lam Dong','Khanh Hoa','Binh Thuan'],\
                'Binh Phuoc':['Tay Ninh','Binh Duong','Dong Nai','Dak Nong','Lam Dong'],\
                'Dong Nai':['Lam Dong','Binh Phuoc','Binh Thuan','Ho Chi Minh','Vung Tau','Binh Duong'],\
                'Binh Thuan':['Vung Tau','Lam Dong','Ninh Thuan','Dong Nai'],\
                'Tay Ninh':['Long An', 'Ho Chi Minh', 'Binh Duong','Binh Phuoc'],\
                'Binh Duong':['Tay Ninh','Ho Chi Minh','Dong Nai','Binh Phuoc'],\
                'Ho Chi Minh':['Tay Ninh','Binh Duong','Dong Nai','Long An','Vung Tau'],\
                'Vung Tau':['Ho Chi Minh','Dong Nai','Binh Thuan'],\
                'Long An':['Tay Ninh','Ho Chi Minh','Dong Thap','Tien Giang'],\
                'Dong Thap':['Long An','Tien Giang','Vinh Long','Can Tho','An Giang'],\
                'Tien Giang':['Long An','Dong Thap','Vinh Long','Ben Tre'],\
                'Ben Tre':['Vinh Long','Tien Giang','Tra Vinh'],\
                'An Giang':['Kien Giang','Can Tho','Dong Thap'],\
                'Can Tho':['Kien Giang','An Giang','Dong Thap','Vinh Long','Hau Giang'],\
                'Vinh Long':['Can Tho','Dong Thap','Ben Tre','Tra Vinh','Hau Giang'],\
                'Tra Vinh':['Ben Tre','Vinh Long','Soc Trang'],\
                'Soc Trang':['Hau Giang','Bac Lieu','Tra Vinh'],\
                'Hau Giang':[ 'Kien Giang','Bac Lieu','Soc Trang','Can Tho','Vinh Long'],\
                'Kien Giang':['An Giang','Can Tho','Hau Giang','Bac Lieu','Ca Mau'],\
                'Bac Lieu':['Kien Giang','Hau Giang','Soc Trang','Ca Mau'],\
                'Ca Mau':['Kien Giang','Bac Lieu'],\
                'Ha Noi':['Phu Tho','Hoa Binh','Bac Giang','Vinh Phuc','Bac Ninh','Hung Yen','Ha Nam'],\
                'Phu Tho':['Son La','Yen Bai','Hoa Binh','Ha Noi','Vinh Phuc','Tuyen Quang'],\
                'Hoa Binh':['Ninh Binh','Thanh Hoa','Ha Nam','Ha Noi','Phu Tho','Son La'],\
                'Bac Giang':['Quang Ninh','Hai Duong','Bac Ninh','Ha Noi','Thai Nguyen','Lang Son'],\
                'Vinh Phuc':['Phu Tho', 'Ha Noi','Thai Nguyen','Tuyen Quang'],\
                'Bac Ninh':['Ha Noi','Hung Yen','Hai Duong', 'Bac Giang'],\
                'Hung Yen':['Ha Noi','Bac Ninh','Hai Duong','Thai Binh','Ha Nam'],\
                'Ha Nam':['Ha Noi','Hung Yen','Thai Binh','Nam Dinh','Ninh Binh','Hoa Binh'],\
                'Hai Phong':['Thai Binh','Thai Binh','Quang Ninh'],\
                'Hai Duong':['Bac Ninh', 'Hung Yen','Thai Binh','Hai Phong','Quang Ninh','Bac Giang'],\
                'Nam Dinh':['Ninh Binh','Ha Nam','Thai Binh'],\
                'Thai Nguyen':['Tuyen Quang', 'Bac Kan','Lang Son','Bac Giang','Ha Noi','Vinh Phuc'],\
                'Thai Binh':['Nam Dinh', 'Ha Nam','Hung Yen','Hai Duong','Hai Duong','Hai Phong'],\
                'Quang Ninh':['Hai Duong','Hai Phong','Bac Giang','Lang Son'],\
                'Lang Son':['Quang Ninh','Bac Giang','Thai Nguyen','Bac Kan','Cao Bang'],\
                'Ninh Binh':['Hoa Binh','Thanh Hoa','Nam Dinh','Ha Nam'],\
                'Lao Cai':['Lai Chau','Yen Bai','Hà Giang'],\
                'Cao Bang':['Hà Giang','Bac Kan','Lang Son'],\
                'Hà Giang':['Cao Bang','Tuyen Quang','Yen Bai','Lao Cai'],\
                'Tuyen Quang':['Hà Giang','Bac Kan','Thai Nguyen','Vinh Phuc','Phu Tho','Yen Bai'],\
                'Bac Kan':['Tuyen Quang','Thai Nguyen','Lang Son','Cao Bang'],\
                'Son La':['Dien Bien','Yen Bai','Phu Tho','Hoa Binh','Thanh Hoa'],\
               }
    df=pd.read_excel('Data_Excel.xlsx')
    Province1 = df['Province']
    Province=[]
    for i in Province1:
        Province.append(i.strip())

    list_distance=[]
    for i in df.values:
        list_distance.append(list(i[1:-2]))
    dict_province={}
    for i in range(len(Province)):
        dict_province[Province[i]]=i
    dict_province    
    dict_data={}
    for i in data_neighbor:
        list_each_province=[]
        for j in data_neighbor[i]:
            list_each_province.append(j)
            list_each_province.append(list_distance[dict_province[i]][dict_province[j]])
        list_each_province.append(list_distance[dict_province[i]][dict_province[goal]])
        dict_data[i]=list_each_province
    return dict_data  
#print(create_data_A_star('Ha Noi','Thanh Hoa'))

def create_data_UCS():
    data_neighbor={'Lai Chau':['Dien Bien','Lao Cai','Son La','Yen Bai'],\
                'Yen Bai':['Lao Cai','Lai Chau','Son La','Hà Giang','Phu Tho','Tuyen Quang'],\
                'Dien Bien':['Lai Chau','Son La'],\
                'Thanh Hoa':['Son La','Nghe An','Ninh Binh','Hoa Binh'],
                'Nghe An':['Ha Tinh','Thanh Hoa'],\
                'Quang Binh':['Ha Tinh','Quang Tri'] ,\
                'Ha Tinh':['Nghe An','Quang Binh'],\
                'Quang Tri':['Quang Binh','Hue'],\
                'Hue':['Quang Tri','Da Nang'],\
               'Da Nang':['Hue','Quang Nam'],\
                'Quang Nam':['Da Nang','Hue','Kon Tum','Quang Ngai'],\
                'Kon Tum':['Quang Nam','Quang Ngai','Gia Lai'],\
                'Quang Ngai':['Kon Tum','Quang Nam','Binh Dinh'],\
                'Gia Lai':['Kon Tum','Binh Dinh','Phu Yen','Dak Lak'],\
                'Binh Dinh':['Quang Ngai','Gia Lai','Phu Yen'],\
                'Dak Lak':['Dak Nong','Lam Dong','Khanh Hoa','Phu Yen','Gia Lai'],\
                'Phu Yen':['Gia Lai','Binh Dinh','Dak Lak','Khanh Hoa'],\
                'Khanh Hoa':['Dak Lak','Phu Yen','Lam Dong','Ninh Thuan'],\
                'Dak Nong':['Dak Lak','Lam Dong','Binh Phuoc'],\
                'Lam Dong':['Dak Lak','Dak Nong','Binh Phuoc','Dong Nai','Binh Thuan','Ninh Thuan','Khanh Hoa'],\
                'Ninh Thuan':['Lam Dong','Khanh Hoa','Binh Thuan'],\
                'Binh Phuoc':['Tay Ninh','Binh Duong','Dong Nai','Dak Nong','Lam Dong'],\
                'Dong Nai':['Lam Dong','Binh Phuoc','Binh Thuan','Ho Chi Minh','Vung Tau','Binh Duong'],\
                'Binh Thuan':['Vung Tau','Lam Dong','Ninh Thuan','Dong Nai'],\
                'Tay Ninh':['Long An', 'Ho Chi Minh', 'Binh Duong','Binh Phuoc'],\
                'Binh Duong':['Tay Ninh','Ho Chi Minh','Dong Nai','Binh Phuoc'],\
                'Ho Chi Minh':['Tay Ninh','Binh Duong','Dong Nai','Long An','Vung Tau'],\
                'Vung Tau':['Ho Chi Minh','Dong Nai','Binh Thuan'],\
                'Long An':['Tay Ninh','Ho Chi Minh','Dong Thap','Tien Giang'],\
                'Dong Thap':['Long An','Tien Giang','Vinh Long','Can Tho','An Giang'],\
                'Tien Giang':['Long An','Dong Thap','Vinh Long','Ben Tre'],\
                'Ben Tre':['Vinh Long','Tien Giang','Tra Vinh'],\
                'An Giang':['Kien Giang','Can Tho','Dong Thap'],\
                'Can Tho':['Kien Giang','An Giang','Dong Thap','Vinh Long','Hau Giang'],\
                'Vinh Long':['Can Tho','Dong Thap','Ben Tre','Tra Vinh','Hau Giang'],\
                'Tra Vinh':['Ben Tre','Vinh Long','Soc Trang'],\
                'Soc Trang':['Hau Giang','Bac Lieu','Tra Vinh'],\
                'Hau Giang':[ 'Kien Giang','Bac Lieu','Soc Trang','Can Tho','Vinh Long'],\
                'Kien Giang':['An Giang','Can Tho','Hau Giang','Bac Lieu','Ca Mau'],\
                'Bac Lieu':['Kien Giang','Hau Giang','Soc Trang','Ca Mau'],\
                'Ca Mau':['Kien Giang','Bac Lieu'],\
                'Ha Noi':['Phu Tho','Hoa Binh','Bac Giang','Vinh Phuc','Bac Ninh','Hung Yen','Ha Nam'],\
                'Phu Tho':['Son La','Yen Bai','Hoa Binh','Ha Noi','Vinh Phuc','Tuyen Quang'],\
                'Hoa Binh':['Ninh Binh','Thanh Hoa','Ha Nam','Ha Noi','Phu Tho','Son La'],\
                'Bac Giang':['Quang Ninh','Hai Duong','Bac Ninh','Ha Noi','Thai Nguyen','Lang Son'],\
                'Vinh Phuc':['Phu Tho', 'Ha Noi','Thai Nguyen','Tuyen Quang'],\
                'Bac Ninh':['Ha Noi','Hung Yen','Hai Duong', 'Bac Giang'],\
                'Hung Yen':['Ha Noi','Bac Ninh','Hai Duong','Thai Binh','Ha Nam'],\
                'Ha Nam':['Ha Noi','Hung Yen','Thai Binh','Nam Dinh','Ninh Binh','Hoa Binh'],\
                'Hai Phong':['Thai Binh','Thai Binh','Quang Ninh'],\
                'Hai Duong':['Bac Ninh', 'Hung Yen','Thai Binh','Hai Phong','Quang Ninh','Bac Giang'],\
                'Nam Dinh':['Ninh Binh','Ha Nam','Thai Binh'],\
                'Thai Nguyen':['Tuyen Quang', 'Bac Kan','Lang Son','Bac Giang','Ha Noi','Vinh Phuc'],\
                'Thai Binh':['Nam Dinh', 'Ha Nam','Hung Yen','Hai Duong','Hai Duong','Hai Phong'],\
                'Quang Ninh':['Hai Duong','Hai Phong','Bac Giang','Lang Son'],\
                'Lang Son':['Quang Ninh','Bac Giang','Thai Nguyen','Bac Kan','Cao Bang'],\
                'Ninh Binh':['Hoa Binh','Thanh Hoa','Nam Dinh','Ha Nam'],\
                'Lao Cai':['Lai Chau','Yen Bai','Hà Giang'],\
                'Cao Bang':['Hà Giang','Bac Kan','Lang Son'],\
                'Hà Giang':['Cao Bang','Tuyen Quang','Yen Bai','Lao Cai'],\
                'Tuyen Quang':['Hà Giang','Bac Kan','Thai Nguyen','Vinh Phuc','Phu Tho','Yen Bai'],\
                'Bac Kan':['Tuyen Quang','Thai Nguyen','Lang Son','Cao Bang'],\
                'Son La':['Dien Bien','Yen Bai','Phu Tho','Hoa Binh','Thanh Hoa'],\
               }
    df=pd.read_excel('Data_Excel.xlsx')
    Province1 = df['Province']
    Province=[]
    for i in Province1:
        Province.append(i.strip())

    list_distance=[]
    for i in df.values:
        list_distance.append(list(i[1:-2]))
    dict_province={}
    for i in range(len(Province)):
        dict_province[Province[i]]=i
    dict_province    
    dict_data={}
    for i in data_neighbor:
        list_each_province=[]
        for j in data_neighbor[i]:
            list_each_province.append(j)
            list_each_province.append(list_distance[dict_province[i]][dict_province[j]])
        dict_data[i]=list_each_province
    return dict_data  

def main():
    pass

if __name__ == "__main__":
    main()