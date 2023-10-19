import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit 超入門')
st.write('プログレスバー')

'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'


st.title('Streamlit 超入門')
st.write('DataFrame')

df = pd.DataFrame({
    '一列目': [1, 2, 3, 4],
    '二列目': [10, 20, 30, 40]
})
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

randdf = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.bar_chart(randdf)

mapdf = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(mapdf)

st.write('Display Image')
if st.checkbox('Show Image'):
    img = Image.open('photo.jpg')
    st.image(img, caption='Tokyo girl', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください、',
    list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'

text = st.sidebar.text_input('あなたの趣味を教えてください。')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'あなたの趣味：', text
'コンディション', condition

left_column, right_column = st.columns(2)
button = left_column.button('右側にマップを表示')
if button:
    right_column.map(mapdf)

expander1 = st.expander('問い合わせ')
textbox = expander1.text_input('問い合わせ内容の記入')
expander1.write(textbox)

expander2 = st.expander('注文')
selectbox = expander2.selectbox(
    '注文内容',
    list(range(1, 11))
)
expander2.write(selectbox)

expander3 = st.expander('満足度')
slider = expander3.slider('満足度', 0, 100, 50)
expander3.write(slider)
