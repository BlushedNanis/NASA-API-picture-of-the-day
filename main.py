import streamlit as st
from requests import get
from dotenv import load_dotenv
from os import getenv

#Load .env file
load_dotenv()

#Make request from NASA API and transform it into a dict
response = get("https://api.nasa.gov/planetary/"
               f"apod?api_key={getenv("api_key")}").json()

#Get image binary data and write a jpg file
image = get(response["hdurl"]).content
with open("image.jpg", "wb") as file:
    file.write(image)
