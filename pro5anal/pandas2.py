# 재색인
# from crypt import methods      # 현재 mac 최신 버전에서는 사용 가능하지 않음
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# Series의 재색인
data = Series([1, 3, 2], index=(1, 4, 2))
print(data)
data2 = data.reindex((1, 2, 4))
print(data2)

print('\n재색인할때 값 채워넣기')
data3 = data.reindex([0,1,2,3,4,5])
print(data3)

# fill_vlaue : 대응값이 없는 인덱스에는 특정값으로 채움
data3 = data2.reindex([0, 1, 2, 3, 4, 5], fill_value=777)
print(data3)

print()
# NaN 앞 값으로 NaN을 채움
data3 = data2.reindex([0, 1, 2, 3, 4, 5], method='ffill')
print(data3)
data3 = data2.reindex([0, 1, 2, 3, 4, 5], method='backfill')        # 뒤의 값으로 # NaN 앞 값으로 NaN을 채움
print(data3)

print('\nDataFrame : bool 처리')
df = DataFrame(np.arange(12).reshape(4, 3),
                index= ['1월', '2월', '3월', '4월'],
                columns=['강남', '강북', '서초'])
print(df)

