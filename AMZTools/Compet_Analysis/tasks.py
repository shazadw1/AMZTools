from celery import shared_task
import pandas as pd
import numpy as np
from .models import *
import copy
import os
from django.core.files.base import File


def clean_size(x):
    if "-" == x:
        x=x.replace('-',str(0))
        return (x)
    elif ">" in x:
        x=x.replace('>',str(0))
        return (x)
    elif "NaN" in x:
        x=x.replace('NaN',str(0))
    elif "nan" in x:
        x=x.replace('nan',str(0))
    elif "N/R" in x:
        x=x.replace('N/R',str(0))
    elif x == None:
        x=x.replace(None, str(0))
    else:
        return (x)



@shared_task(bind=True)
def test_func(self,filesss, pk):
    filess = pd.read_excel(filesss)
    df = pd.DataFrame(filess)
    if 'Keyword Phrase' in df.columns.tolist():
        df = df.rename(columns={"Keyword Phrase": "Phrase"})
    column_list = df.columns.tolist()
    column_list_asin = column_list[-9:]
    final_colms=['Phrase','Search Volume','Title Density','Position (Rank)']+column_list_asin
    df = df[final_colms]
    data_list = df.to_dict(orient='records')
    # column_list = df.columns.values
    df.to_excel(str(pk)+"cerebro.xlsx")
    head1 = Comp_Analysis_KW_Cerebro_Data_Head.objects.create(keyword = Comp_Analysis_basic_data.objects.get(id=pk), phrase = final_colms[0],search_volume = final_colms[1],
                                    title_density = final_colms[2],position = final_colms[3], asin2 = final_colms[4], asin3 = final_colms[5],
                                    asin4 = final_colms[6],asin5 = final_colms[7],asin6 = final_colms[8], asin7 = final_colms[9],asin8 = final_colms[10],
                                    asin9 = final_colms[11],asin10 = final_colms[12])
    head=Comp_Analysis_KW_Cerebro_Data_Head.objects.get(id=head1.id)
    file = open(str(pk)+"cerebro.xlsx", 'rb') 
    a = File(file)
    head.excel_file.save(str(pk)+"cerebro.xlsx", a)

    os.remove(str(pk)+"cerebro.xlsx")                             
    objs = [
        Comp_Analysis_KW_Cerebro_Data(
            head = Comp_Analysis_KW_Cerebro_Data_Head.objects.get(id=head1.id), phrase = e[final_colms[0]] ,search_volume = e[final_colms[1]], title_density = e[final_colms[2]],
                                    position = e[final_colms[3]], asin2 = e[final_colms[4]], asin3 = e[final_colms[5]],
                                    asin4 = e[final_colms[6]],asin5 = e[final_colms[7]],asin6 = e[final_colms[8]], 
                                    asin7 = e[final_colms[9]],asin8 = e[final_colms[10]], asin9 = e[final_colms[11]],asin10 = e[final_colms[12]]
        )
        for e in data_list
    ]
    msg = Comp_Analysis_KW_Cerebro_Data.objects.bulk_create(objs=objs)
    return "done"


@shared_task(bind=True)
def filter_data(self, filess, min_sv, min_rel, max_rank, mv_f_id, mv_pk):
    # read excel and convert to dataframe
    df = pd.read_excel(filess)
    original_df = copy.copy(df)

    # filter out each column to make it int type so that calculations can be done ahead
    column_list = df.columns.tolist()
    column_list = column_list[1:]

    for i in column_list:
        if i != 'Phrase' and df.dtypes[i] != 'int':
            df.replace(to_replace=[None], value=np.nan, inplace=True)
            df.fillna('0', inplace=True)
            df[i]=df[i].astype(str)
            df[i]=df[i].map(clean_size)
            try:
                df[i]=df[i].astype(int)
            except:
                df[i]=df[i].astype(float)
                df[i]=df[i].astype(int)
        else:
            pass
    
    # # after converting each column to int type filter out dataframe where each row is having Search Volume greater than min sv
    df = df[df['Search Volume']>=int(min_sv)]


    # # get last 10 asins column heading to make a different dataframe for only asins
    df1=df[column_list[-10:]]

    # # filter out this asins df such that in each row every column value greater than max_rank or equal to max rank will be converted to Nan
    d = df1[df1<=int(max_rank)]

    # # count total Nan in each row and see if count of nan is greater than (10-min_relv+1) i.e filter out only those rows that have at least min_rev (number of)
    # # of asins having value less than max rank
    min_relv = (10-int(min_rel))+1
    d = d[d.isnull().sum(axis=1) < min_relv]

    # create a score column to count number of rel . but first copy sv column values to it just to create column 
    d["score"] = df['Search Volume']
    d["score"] = d.notna().sum(axis=1)-1

    # # making the final dataframe having all columns with all filtered values
    # del column_list[2:3]
    df=df.loc[d.index.tolist(), column_list]

    df["score"] = d["score"].values

    # # exclude phrase in order to add up the sv having asin greater than 10 and 30 column wise
    columns_list = column_list[-10:]                
    top10= [df.loc[df[i] <= 10, 'Search Volume'].sum() for i in columns_list]
    top30= [df.loc[df[i] <= 30, 'Search Volume'].sum() for i in columns_list]

    sv_total = df['Search Volume'].sum()
    thirty_percent = [(x*100)/sv_total for x in top30]
    
    # top3
    i = sorted(zip(thirty_percent, columns_list), reverse=True)[:3]
    top3 = [i[j][1] for j in range(3)]
    # # Create your result model
    mv_f_result = Comp_Analysis_Data_FilterResult.objects.create(filter=Comp_Analysis_Data_Filter.objects.get(id=int(mv_f_id)),
                                                    total_phrase = df['Phrase'].count(),
                                                    search_volume_total=sv_total,
                                                    top_10_sv = top10,
                                                    top_30_sv = top30,
                                                    top_10percent_sv = [(x*100)/sv_total for x in top10],
                                                    top_30percent_sv = thirty_percent,
                                                    top_3 = top3
                                                )    
    column_list.remove('Title Density')
    
    df = original_df.loc[d.index.tolist(), column_list]
    df["score"] = d["score"].values
    data_list = df.to_dict(orient='records')
    
    objs = [
        Comp_Analysis_Filtered_Data(
                            mv_filtered_result = Comp_Analysis_Data_FilterResult.objects.get(id=mv_f_result.id), phrase = e[column_list[0]] ,search_volume = e[column_list[1]], asin2 = e[column_list[2]],
                            asin3 = e[column_list[3]], asin4 = e[column_list[4]],asin5 = e[column_list[5]],asin6 = e[column_list[6]], 
                            asin7 = e[column_list[7]],asin8 = e[column_list[8]], asin9 = e[column_list[9]],asin10 = e[column_list[10]],
                            asin11 = e[column_list[11]], score = e['score']
        )
        for e in data_list
    ]
    msg = Comp_Analysis_Filtered_Data.objects.bulk_create(objs=objs)
    df.to_excel(str(mv_pk)+"filteredcerebro.xlsx")
    file = open(str(mv_pk)+"filteredcerebro.xlsx", 'rb') 
    head=Comp_Analysis_Data_FilterResult.objects.get(id=mv_f_result.id)
    a = File(file)
    head.filtered_file.save(str(mv_pk)+"filteredcerebro.xlsx", a)

    os.remove(str(mv_pk)+"filteredcerebro.xlsx")  
    return 'done'


@shared_task(bind=True)
def master_table(self, filtered_condition_id):

    # getting filtered dataframe and making a final competitor file named AKWs

    filess = Comp_Analysis_Data_FilterResult.objects.get(filter__id=filtered_condition_id)
    filtered_df = pd.read_excel(filess.filtered_file)
    top3_list = list(eval(filess.top_3))
    for i in top3_list:
        if filtered_df.dtypes[i] != 'int':
            filtered_df.replace(to_replace=[None], value=np.nan, inplace=True)
            filtered_df.fillna('0', inplace=True)
            filtered_df[i]=filtered_df[i].astype(str)
            filtered_df[i]=filtered_df[i].map(clean_size)
            try:
                filtered_df[i]=filtered_df[i].astype(int)
            except:
                filtered_df[i]=filtered_df[i].astype(float)
                filtered_df[i]=filtered_df[i].astype(int)
        else:
            pass

    max_rank = filess.filter.max_rank
    print(max_rank)

    # top 3 competitors
    a = filtered_df.loc[filtered_df[top3_list[0]] <= int(max_rank), ('Phrase','Search Volume')]
    b = filtered_df.loc[filtered_df[top3_list[1]] <= max_rank, ('Phrase','Search Volume')]
    c = filtered_df.loc[filtered_df[top3_list[2]] <= max_rank, ('Phrase','Search Volume')]

    # you have to get the original data for this top competitors 

    # combined top 3 competitors
    AKWs=pd.concat([b,a,c]).drop_duplicates()
    AKWs['category_type'] = 'AKWs'


    # getting a Magnet file
    magnet = pd.read_excel(filess.filter.mv.magnet)
    # getting a Amazon Kws file
    amz = pd.read_excel(filess.filter.mv.amazon_choice)

    CKWs = filtered_df[['Phrase', 'Search Volume']]
    CKWs['category_type'] = 'CKWs'

    magnet_column_list = magnet.columns.tolist()
    if "Keyword Phrase" in magnet_column_list:
        Magnet = magnet[['Keyword Phrase', 'Search Volume']]
        Magnet = Magnet.rename(columns={"Keyword Phrase": "Phrase"})
    else:
        Magnet = magnet[['Phrase', 'Search Volume']]
    Magnet['category_type'] = 'Magnet'

    amz_column_list = amz.columns.tolist()
    if "Keyword Phrase" in amz_column_list:
        AMZKWs = amz[['Keyword Phrase', 'Search Volume']]
        AMZKWs = AMZKWs.rename(columns={"Keyword Phrase": "Phrase"})
    else:
        AMZKWs = amz[['Phrase', 'Search Volume']]
    AMZKWs['category_type'] = 'AMZ KWs'

    CAMAMZ=pd.concat([AKWs,CKWs,Magnet,AMZKWs]).drop_duplicates()
    CAMAMZ['category_type'] = 'CKWs+AKWs+Magnet+AMZ KWs'

    AM = pd.concat([AKWs,Magnet]).drop_duplicates()
    AM['category_type'] = 'AKWs+Magnet'

    CAMZ = pd.concat([CKWs,AMZKWs]).drop_duplicates()
    CAMZ['category_type'] = 'CKWs+AMZ KWs'

    CMAMZ = pd.concat([CKWs,Magnet,AMZKWs]).drop_duplicates()
    CMAMZ['category_type'] = 'CKWs+Magnet+AMZ KWs'

    CM = pd.concat([CKWs,Magnet]).drop_duplicates()
    CM['category_type'] = 'CKWs+Magnet'

    CA = pd.concat([AKWs,CKWs]).drop_duplicates()
    CA['category_type'] = 'CKWs+AKWs'

    CAAMZ = pd.concat([AKWs,CKWs,AMZKWs]).drop_duplicates()
    CAAMZ['category_type'] = 'CKWs+AKWs+AMZ KWs'

    CAM = pd.concat([AKWs,CKWs,Magnet]).drop_duplicates()
    CAM['category_type'] = 'CKWs+AKWs+Magnet'

    master =pd.concat([CAMAMZ,AKWs,CKWs,Magnet,AM,CAMZ,CMAMZ,CM,CA,CAAMZ,CAM])
    master.sort_index()

    data_list = master.to_dict(orient='records')

    objs = [
        Comp_Analysis_kw_master_table(
            filtered_comp = Comp_Analysis_basic_data.objects.get(id=filess.filter.mv.id), 
            phrase = e['Phrase'],
            search_volume = e['Search Volume'],
            source = e['category_type']
        )
        for e in data_list
    ]
    msg = Comp_Analysis_kw_master_table.objects.bulk_create(objs=objs)
    Comp_Analysis_basic_data.objects.filter(id=filess.filter.mv.id).update(master_table=True)
    return "done"
