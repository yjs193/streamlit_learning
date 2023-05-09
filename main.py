import streamlit as st
import numpy as np
import pandas as pd
import datetime
import time
st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown('Streamlit is **_really_ cool**.')

# with st.spinner('Wait for it...'):
#         time.sleep(5)
# st.success('Done!')

st.balloons()
st.error('This is an error')
st.warning('This is a warning')
st.info('This is a purely informational message')
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)

code = '''def hello():print("Hello, Streamlit!")'''
st.code(code, language='python')
df = pd.DataFrame(
    {
        "first column": [5, 6, 7, 8],
        "second column": [100, 200, 400, 300]
    }
)
st.write(df.style.highlight_max(axis=0))

genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary')
)
if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy")

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider(
'Select a range of values',
0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
number = st.number_input('Insert a number')
st.write('The current number is ', number)
d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)


txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')


st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')
np.random.seed(2023)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.write(chart_data)

st.line_chart(chart_data)
st.area_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [23.13, 113.27],
    columns=['lat', 'lon'])
st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data

option = st.sidebar.selectbox(
    'Which number do you like best?',
    df['first column'])
st.sidebar.write('You selected: ', option)

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
st.write('You selected:', options)

if st.button("I'm a buttom"):
    st.write("The button has been pressed")
else:
    st.write("The button has not been pressed")

left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we\'re done!'

