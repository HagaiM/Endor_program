import pandas as pd
import statistics as s


def is_number(s):
    if isinstance(s, basestring) == True:
        try:
            float(s)
            return s
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass



def add_kpis_to_raw_data(source_file,output_file,remove_bad_rows = None):
    df = pd.read_csv(source_file)
    df['Date'] = pd.to_datetime(df['DATE'])
    df['Week_Number'] = df['Date'].dt.strftime('%U')
    df['day_of_week_in_number'] = df['Date'].dt.dayofweek
    df['year'] = pd.DatetimeIndex(df['Date']).year






    df_new  = df #df[df['CBETHUSD'].map(len) > 2]
    df_new.set_index(['year','Week_Number','Date'])
    dd = df_new.pivot_table(index=['year','Week_Number'], columns=['day_of_week_in_number'], values=['CBETHUSD'], aggfunc='first')
    dd = dd.reset_index()
    df1 = dd
    df1['all_values'] = list(df1['CBETHUSD'].values)

    list(df1.columns.values)
    df_kpis = pd.DataFrame()
    flag = 1

    for index, row in df1.iterrows():
        new_list = row[9].tolist()
        #is float check
        new_list = [is_number(i) for i in new_list]
        res = list(filter(None, new_list))
        res = [float(i) for i in res]
        median = s.median(res)
        median_low = s.median_low(res)
        median_high =s.median_high(res)
        average = s.mean(res)
        temp = pd.DataFrame({'year': row[0], 'Week_Number': row[1], 'Median': median, 'Median_Low': median_low, 'Median_High': median_high, 'AVG': average}, index=[flag])
        df_kpis = pd.concat([df_kpis, temp])
        flag +=1

    pd.DataFrame(df_kpis)


    result = pd.merge(df_new,df_kpis,on=['year','Week_Number'],how='left')
    final_result = pd.DataFrame(result, columns = ['DATE','CBETHUSD','Median_Low','Median_High','Median','AVG'])

    if remove_bad_rows == 1:
        for index, row in final_result.iterrows():
            if is_number(row[1]) is None:
                final_result.drop(index, inplace=True)



    final_result.to_csv(output_file, sep=',' , index=False)



source_file = '/Users/hagaimanor/Downloads/ETH_USD.csv'
output_file = '/Users/hagaimanor/Downloads/ETH_USD_agg.csv'
# remove_bad_rows 1 for remove bad data from output file
remove_bad_rows = 1
add_kpis_to_raw_data(source_file,output_file,1)