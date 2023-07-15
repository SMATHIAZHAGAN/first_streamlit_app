import streamlit
import pandas
import requests

streamlit.title('My Moms\' New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
   
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# streamlit.dataframe(my_fruit_list)

# Pre-populate the pick list with two fruits
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# streamlit.dataframe(my_fruit_list)

# Filter selected fruits from the table and display
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response)

streamlit.header('Frutiyvice Fruit Advice!')

# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response.json()) # writes data to the screen

# take the json version of the response and normalize it
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it in the screen dataas table
# streamlit.dataframe(fruityvice_normalized)

# Make API call to read data from fruityvice site in json format
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "Kiwi")
# take the json version of the response and normalize it
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it in the screen dataas table
# streamlit.dataframe(fruityvice_normalized)


# Add a textbox for user to input fruit
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
# Make API call to read data from fruityvice site in json format
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it in the screen dataas table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
streamlit.header('Connected to PC_RIVERY_DB Database')

# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
#my_cur.execute("insert into fruit_load_list values ('" +  add_my_fruit + "')")
streamlit.write('Thanks for adding ', add_my_fruit)
