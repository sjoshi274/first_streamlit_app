import streamlit
import pandas
import requests 
import snowflake.connector
from urllib.error import URLError

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

# create the repeatable code block called function
def  get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice  )
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())    
      return fruityvice_normalized

# new section to display fruityvice api response
streamlit.header('FruityVice Fruit Advice!')
try:
    fruit_choice  =  streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
             streamlit.error("please select a fruit to get information")
                  
    else:                 
         back_from_function =  get_fruityvice_data(fruit_choice)
         streamlit.dataframe(back_from_function)
    
except  URLError  as e:
              streamlit.error()

  

streamlit.header("the fruit load list contains:")
# snowflake related functions
def get_fruit_load_list():
      with my_cnx.cursor() as my_cur:
       my_cur.execute("SELECT * from fruit_load_list")
       return my_cur.fetchall()

# add a u button to load fruit
if streamlit.button('Get fruit load list'):
      my_cnx = snowflake.connector.connect(insecure_mode=True   ,  **streamlit.secrets["snowflake"] )
      my_data_rows = get_fruit_load_list()
      my_cnx.close()
      streamlit.dataframe(my_data_rows)
      
      
      # allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
     with my_cnx.cursor() as my_cur:
          my_cur.execute("insert into fruit_load_list values ('" +  new_fruit   +"')")
          return "thanks for adding " + new_fruit
                                 

 add_my_fruit = streamlit.text_input('What fruit would you like to add?')
 if streamlit.button('add a fruit to the list'):
      my_cnx = snowflake.connector.connect(insecure_mode=True   ,  **streamlit.secrets["snowflake"] )
      back_from_function  =  insert_row_snowflake(add_my_fruit)
      my_cnx.close()
      streamlit.text(back_from_function)

