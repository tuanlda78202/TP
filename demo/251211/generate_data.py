import pandas as pd
import random

def create_domain_partition():
    df = pd.read_excel('Data_Excel.xlsx')
    list_mw_north, list_mw_central, list_mw_south = [],[],[]
    for i in range (len(df)):
        if df.iloc[i,64] > 20:
            list_mw_north.append(df.iloc[i,0])
        elif df.iloc[i,64] < 12:
            list_mw_south.append(df.iloc[i,0])
        else:
            list_mw_central.append(df.iloc[i,0])
    return list_mw_north, list_mw_central, list_mw_south

def create_main_warehouse():
    df=pd.read_excel('Data_Excel.xlsx')
    Latitude=list(df['Latitude'])
    Longitude=list(df['Longitude'])
    province=df['Province']
    position_main_warehouse1=[]
    position_main_warehouse2=[]
    position_main_warehouse3=[]
    for i in range(len(Latitude)):
        if Latitude[i] >20 :
            position_main_warehouse1.append(i)
        elif Latitude[i] >12:
            position_main_warehouse2.append(i)
        else:
            position_main_warehouse3.append(i)
    main_warehouse1=province[random.choice(position_main_warehouse1)].strip()
    main_warehouse2=province[random.choice(position_main_warehouse2)].strip()
    main_warehouse3=province[random.choice(position_main_warehouse3)].strip()
    list_main_warehouse=[main_warehouse1,main_warehouse2,main_warehouse3]
    return list_main_warehouse
    
def create_data_A_star(start,goal,random_mainwarehouse = False):
    if random_mainwarehouse == False:
        list_main_warehouse = ['Ha Noi','Da Nang','Ho Chi Minh']
    else:
        list_main_warehouse=create_main_warehouse()
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
    dict_data={}
    dict_data_cost={}
    cost_truck = 35.000 
    cost_plane = 160.000 
    v_truck = 60 
    v_plane = 800 
    time_save_warehouse=2
    for i in list_main_warehouse:
        list_each_province=[]
        list_each_province_cost=[]
        for j in list_main_warehouse:
            if i!=j:
                list_each_province.append(j)
                list_each_province.append(list_distance[dict_province[i]][dict_province[j]])
                list_each_province_cost.append(j)
                list_each_province_cost.append((list_distance[dict_province[i]][dict_province[j]]/v_plane+time_save_warehouse)\
                                               *cost_plane)
            dict_data[i]=list_each_province 
            dict_data_cost[i]=list_each_province_cost
    for i in data_neighbor:
        list_each_province=[]
        list_each_province_cost=[]
        for j in data_neighbor[i]:
            list_each_province.append(j)
            list_each_province.append(list_distance[dict_province[i]][dict_province[j]])
            list_each_province_cost.append(j)
            list_each_province_cost.append(list_distance[dict_province[i]][dict_province[j]]/v_truck*cost_truck)
        list_each_province.append(list_distance[dict_province[i]][dict_province[goal]])
        list_each_province_cost.append(list_distance[dict_province[i]][dict_province[goal]]/v_plane*2*cost_plane)
        if i in dict_data:
            dict_data[i]+=list_each_province
            dict_data_cost[i]+=list_each_province_cost
        else:
            dict_data[i]=list_each_province
            dict_data_cost[i]=list_each_province_cost
    '''
    print(list_main_warehouse)
    print(dict_data)
    print()
    print()
    print(dict_data_cost)
    '''
    return  list_main_warehouse,dict_data_cost
create_data_A_star('Vinh Phuc','Ca Mau')
def create_data_UCS(random_mainwarehouse = False):
    if random_mainwarehouse == False:
        list_main_warehouse = ['Ha Noi','Da Nang','Ho Chi Minh']
    else:
        list_main_warehouse=create_main_warehouse()
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
    dict_data={}
    dict_data_cost={}
    cost_truck = 35.000 
    cost_plane = 160.000 
    v_truck = 60 
    v_plane = 800 
    for i in list_main_warehouse:
        list_each_province=[]
        list_each_province_cost=[]
        for j in list_main_warehouse:
            if i!=j:
                list_each_province.append(j)
                list_each_province.append(list_distance[dict_province[i]][dict_province[j]])
                list_each_province_cost.append(j)
                list_each_province_cost.append(list_distance[dict_province[i]][dict_province[j]]/v_plane*cost_plane)
            dict_data[i]=list_each_province 
            dict_data_cost[i]=list_each_province_cost
    for i in data_neighbor:
        list_each_province=[]
        list_each_province_cost=[]
        for j in data_neighbor[i]:
            list_each_province.append(j)
            list_each_province.append(list_distance[dict_province[i]][dict_province[j]])
            list_each_province_cost.append(j)
            list_each_province_cost.append(list_distance[dict_province[i]][dict_province[j]]/v_truck*cost_truck)
        if i in dict_data:
            dict_data[i]+=list_each_province
            dict_data_cost[i]+=list_each_province_cost
        else:
            dict_data[i]=list_each_province
            dict_data_cost[i]=list_each_province_cost
    return list_main_warehouse,dict_data_cost

def create_data_IDA(random_mainwarehouse = False):
    if random_mainwarehouse == False:
        list_main_warehouse = ['Ha Noi','Da Nang','Ho Chi Minh']
    else:
        list_main_warehouse=create_main_warehouse()
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

    return list_main_warehouse,data_neighbor