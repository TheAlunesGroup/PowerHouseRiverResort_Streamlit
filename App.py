import streamlit as st
from PIL import Image
Main_Image = Image.open("PRR_Main_Image.TIFF")
st.set_page_config(layout="wide", page_title="PowerHouse River Resort")
st.image(Main_Image, width=250)
st.header("PowerHouse River Resort", divider="green")
st.write("")
#---------------------------------------#
with st.form("Booking Registration"):
    st.subheader("• Initial Set-Up", divider="blue")
    Name_Text_Input = st.text_input("Enter Your Name")
    Check_in_Date = st.date_input("Check-in Date", value="today", min_value="today")
    Check_out_Date = st.date_input("Check-out Date", value=Check_in_Date, min_value=Check_in_Date)
    Meal_Plan_Select_Box = st.selectbox("Select a Meal Plan", options=["BB", "HB", "FB"])
    Amount_of_Rooms_Number_Input = st.number_input("Amount of Rooms", min_value=1, max_value=4)
    #----------------------------------------------------------------------------------------------#
    if Amount_of_Rooms_Number_Input:
        Type_of_Room_1 = st.selectbox("Type of Room", ["Deluxe", "Standard"])
        st.subheader("• Amount of Pax", divider="blue")
        if Type_of_Room_1 == "Deluxe":
            Number_of_Adults_1 = st.number_input("Adults(Aged 12 & Above)", min_value=2, max_value=3)
            Number_of_Children_0_5_1 = st.number_input("Children(Aged 0-5)", min_value=0, max_value=1)
            Number_of_Children_6_11_1 = st.number_input("Children(Aged 6-11)", min_value=0, max_value=1)
        elif Type_of_Room_1 == "Standard":
            Number_of_Adults_1 = st.number_input("Adults(Aged 12 & Above)", min_value=2, max_value=4)
            Number_of_Children_0_5_1 = st.number_input("Children(Aged 0-5)", min_value=0, max_value=2)
            Number_of_Children_6_11_1 = st.number_input("Children(Aged 6-11)", min_value=0, max_value=2)
        BN = st.selectbox("Extra Meal Options", ["BBQ", "Normal"])
        #---------------------------------------------------------------------------------------------------#
    if st.form_submit_button():
        if Check_out_Date == Check_in_Date:
            st.warning("Please Change the Check-out date")
        if Check_in_Date > Check_out_Date:
            st.warning("Please have the Check-out date be later after Check-in date")
        else:

            if Number_of_Adults_1 == 3 and Number_of_Children_0_5_1 == 1 and Number_of_Children_6_11_1 == 1:
                Summary_File = f"Booking Summary \n Name:{Name_Text_Input} \n Check-in Date:{Check_in_Date} \n Check-out Date:{Check_out_Date} \n Meal Plan:{Meal_Plan_Select_Box} \n Amount of Room{Amount_of_Rooms_Number_Input} "
                with st.expander("", expanded=True):
                    st.header("Summary")
                    st.markdown(f"**Name:** {Name_Text_Input}")
                    st.markdown(f"**Check-in Date:** {Check_in_Date}")
                    st.markdown(f"**Check-out Date:** {Check_out_Date}")
                    st.markdown(f"**Board:** {Meal_Plan_Select_Box}")
                    st.markdown(f"**Room Type:** {Type_of_Room_1}")
                    st.markdown(f"**Number of Rooms:** {Amount_of_Rooms_Number_Input}")
                    st.markdown(f"**Total Price:**")
st.write("© 2025 The Alunes Group. All rights reserved")
st.write("© 2025 Powerhouse River Resort. All rights reserved")