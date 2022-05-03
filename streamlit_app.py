import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')



streamlit.title('My Mom\'s New Healthy Diner')


streamlit.header('\U0001F600 Breakfast Favorites')
streamlit.text('\U0001F423 Omega 3 & Blueberry Oatmeal')
streamlit.text('\U0001F33F Kale , spinach & Rocket Smoothie')
streamlit.text('\U0001F95A Hard-Boiled Free Range Egg')
streamlit.text('\U0001F951 Avacado Toast')


streamlit.header('\U0001F34C \U0001F96D  \U0001F352 Build Your Own Fruit Smoothie \U0001F347 \U0001F34A')

streamlit.multiselect("Pick some Fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])

streamlit.dataframe(my_fruit_list)



