import streamlit
import pandas
import requests 
import snowflake.connector
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')



streamlit.title('My Mom\'s New Healthy Diner')


streamlit.header('\U0001F600 Breakfast Favorites')
streamlit.text('\U0001F423 Omega 3 & Blueberry Oatmeal')
streamlit.text('\U0001F33F Kale , spinach & Rocket Smoothie')
streamlit.text('\U0001F95A Hard-Boiled Free Range Egg')
streamlit.text('\U0001F951 Avacado Toast')


streamlit.header('\U0001F34C \U0001F96D  \U0001F352 Build Your Own Fruit Smoothie \U0001F347 \U0001F34A')

fruits_selected = streamlit.multiselect("Pick some Fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header('FruityVice Fruit Advise')

fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Apple')
streamlit.write('The user entered', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")


# take the json version and normalize it #
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("the fruit load list contains:")
streamlit.dataframe(my_data_rows)
add_my_fruit=streamlit.text_input('What fruit would you like to add?', 'jackfruit')
streamlit.write('Thanks for adding', add_my_fruit)

