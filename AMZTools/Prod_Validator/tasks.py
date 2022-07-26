from celery import shared_task
import pandas as pd
import numpy as np
from Prod_Validator.models import *
import copy


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
    df = df.loc[:, ~df.columns.isin(['Cerebro IQ Score', 'Search Volume Trend (30 days)','Competing Products','CPR','Sponsored ASINs','Amazon Recommended','Sponsored','Organic','Sponsored Rank (avg)','Sponsored Rank (count)','Amazon Recommended Rank (avg)','Amazon Recommended Rank (count)','Relative Rank','Competitor Rank (avg)','Ranking Competitors (count)','Competitor Performance Score'])]
    data_list = df.to_dict(orient='records')
    column_list = df.columns.values
    head1 = ManualValidatorHead.objects.create(keyword = ManualValidator.objects.get(id=pk), phrase = column_list[0],search_volume = column_list[1],
                                    title_density = column_list[2],position = column_list[3], asin2 = column_list[4], asin3 = column_list[5],
                                    asin4 = column_list[6],asin5 = column_list[7],asin6 = column_list[8], asin7 = column_list[9],asin8 = column_list[10],
                                    asin9 = column_list[11],asin10 = column_list[12],asin11 = column_list[13])
    objs = [
        ManualValidatorData(
            head = ManualValidatorHead.objects.get(id=head1.id), phrase = e[column_list[0]] ,search_volume = e[column_list[1]], title_density = e[column_list[2]],
                                    position = e[column_list[3]], asin2 = e[column_list[4]], asin3 = e[column_list[5]],
                                    asin4 = e[column_list[6]],asin5 = e[column_list[7]],asin6 = e[column_list[8]], 
                                    asin7 = e[column_list[9]],asin8 = e[column_list[10]], asin9 = e[column_list[11]],asin10 = e[column_list[12]],
                                    asin11 = e[column_list[13]]
        )
        for e in data_list
    ]
    msg = ManualValidatorData.objects.bulk_create(objs=objs)
    return "done"


@shared_task(bind=True)
def filter_data(self, filess, min_sv, min_rel, max_rank, mv_f_id, mv_pk):
    # read excel and convert to dataframe
    df = pd.read_excel(filess)
    df = df.loc[:, ~df.columns.isin(['Cerebro IQ Score', 'Search Volume Trend (30 days)','Competing Products','CPR','Sponsored ASINs','Amazon Recommended','Sponsored','Organic','Sponsored Rank (avg)','Sponsored Rank (count)','Amazon Recommended Rank (avg)','Amazon Recommended Rank (count)','Relative Rank','Competitor Rank (avg)','Ranking Competitors (count)','Competitor Performance Score'])]
    original_df = copy.copy(df)
    # # filter out each column to make it int type so that calculations can be done ahead
    
    for i in df.columns:
        if i != 'Phrase' and df.dtypes[i] == 'object':
            df[i]=df[i].astype(str)
            df[i]=df[i].map(clean_size)
            df.replace(to_replace=[None], value=np.nan, inplace=True)
            df.fillna('0', inplace=True)
            df[i]=df[i].astype(int)
    
    # # after converting each column to int type filter out dataframe where each row is having Search Volume greater than min sv
    df = df[df['Search Volume']>=int(min_sv)]

    # # get the column list for further user
    column_list = df.columns.tolist()

    # # get last 10 asins column heading to make a different dataframe for only asins
    df1=df[column_list[-10:]]

    # # filter out this asins df such that in each row every column value greater than max_rank or equal to max rank will be converted to Nan
    d=df1[df1<=int(max_rank)]

    # # count total Nan in each row and see if count of nan is greater than (10-min_relv+1) i.e filter out only those rows that have at least min_rev (number of)
    # # of asins having value less than max rank
    min_relv = (10-int(min_rel))+1
    d = d[d.isnull().sum(axis=1) < min_relv]

    # create a score column to count number of rel . but first copy sv column values to it just to create column 
    d["score"] = df['Search Volume']
    d["score"] = d.notna().sum(axis=1)-1

    # # making the final dataframe having all columns with all filtered values
    del column_list[2:4]
    df=df.loc[d.index.tolist(), column_list]
    df["score"] = d["score"].values

    # # exclude phrase in order to add up the sv having asin greater than 10 and 30 column wise

    # changes:::::::::::::::::::::::  sv gets added if asin column is less than or equal to 10 or 30

    top10= [df.loc[df[i] <= 10, 'Search Volume'].sum() for i in df.columns.tolist()[2:12]]
    top30= [df.loc[df[i] <= 30, 'Search Volume'].sum() for i in df.columns.tolist()[2:12]]

    sv_total = df['Search Volume'].sum()

    # # Create your result model
    mv_f_result = ManualValidatorDataFilterResult.objects.create(filter=ManualValidatorDataFilter.objects.get(id=int(mv_f_id)),
                                                    total_phrase = df['Phrase'].count(),
                                                    search_volume_total=sv_total,
                                                    top_10_sv = top10,
                                                    top_30_sv = top30,
                                                    top_10percent_sv = [(x*100)/sv_total for x in top10],
                                                    top_30percent_sv = [(x*100)/sv_total for x in top30]
                                                )
    
    df = original_df.loc[d.index.tolist(), column_list]
    df["score"] = d["score"].values
    data_list = df.to_dict(orient='records')
 
    objs = [
        ManualValidatorFilteredData(
                            mv_filtered_result = ManualValidatorDataFilterResult.objects.get(id=mv_f_result.id), phrase = e[column_list[0]] ,search_volume = e[column_list[1]], asin2 = e[column_list[2]],
                            asin3 = e[column_list[3]], asin4 = e[column_list[4]],asin5 = e[column_list[5]],asin6 = e[column_list[6]], 
                            asin7 = e[column_list[7]],asin8 = e[column_list[8]], asin9 = e[column_list[9]],asin10 = e[column_list[10]],
                            asin11 = e[column_list[11]], score = e['score']
        )
        for e in data_list
    ]
    msg = ManualValidatorFilteredData.objects.bulk_create(objs=objs)

    return 'done'
