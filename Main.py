import streamlit as st
from PIL import Image
Main_Image = Image.open("PRR_Main_Image.TIFF")
#---------------------------------------#
st.set_page_config(page_icon=Main_Image, page_title="PowerHouse River Resort")
st.image(Main_Image, width=250)
st.header("PowerHouse River Resort", divider="green")
st.write("")
st.markdown("**Powerhouse River Resort in Eheliyagoda offers air‑conditioned river‑view tents with private bathrooms and balconies. It features a pool, garden, terrace, free WiFi, parking, and an Asian restaurant. Walking tours and hiking are available, though worth verifying.**")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
google_map_iframe = """<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3162.8851888000005!2d80.3105!3d6.8741!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3ae36574f4419451%3A0x1234567890abcdef!2sPowerhouse%20River%20Resort!5e0!3m2!1sen!2slk!4v1689176350000!5m2!1sen!2slk" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" class="map-frame"  <!-- Add a class for CSS styling -->></iframe> """
custom_css = """<style>.map-frame {border-radius: 20px; /* Adjust this value for more or less rounding */overflow: hidden;  /* Ensures the content within the rounded border is also rounded */border: 5px solid #007BFF; /* Optional: Add a border color */}</style>"""
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(google_map_iframe, unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
st.write("")
st.write("")
st.write("")
st.write("")
with st.container():
   I1, I2, I3, I4, I5 = st.columns(5)
   with I1:
       Image_1 = Image.open("Image_1.jpg")
       st.image(Image_1, width=700)
   with I2:
       Image_2 = Image.open("Image_2.jpg")
       st.image(Image_2)
   with I3:
       Image_3 = Image.open("Image_3.jpg")
       st.image(Image_3)
   with I4:
       Image_4 = Image.open("Image_4.jpg")
       st.image(Image_4)
   with I5:
       Image_5 = Image.open("Image_5.jpg")
       st.image(Image_5)

   I12, I22, I32, I42, I52 = st.columns(5)
   with I12:
       Image_12 = Image.open("Image_1.jpg")
       st.image(Image_12, width=700)
   with I22:
       Image_22 = Image.open("Image_2.jpg")
       st.image(Image_22)
   with I32:
       Image_32 = Image.open("Image_3.jpg")
       st.image(Image_32)
   with I42:
       Image_42 = Image.open("Image_4.jpg")
       st.image(Image_42)
   with I52:
       Image_52 = Image.open("Image_5.jpg")
       st.image(Image_52)
st.write("© 2025 The Alunes Group. All rights reserved")
st.write("© 2025 Powerhouse River Resort. All rights reserved")
