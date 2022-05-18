from celery import shared_task
import pandas as pd
from Prod_Validator.models import ManualValidatorHead, ManualValidatorData, ManualValidator

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
