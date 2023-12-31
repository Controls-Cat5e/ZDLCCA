import streamlit as st
st.set_page_config(
        page_title="Zero Degree Labs CCA",
)
# Title
st.title("Zero Degree Labs CCA")
st.header("PACT Prototype, Carbon Calculator only (Alpha 0.02)")
km_drive = st.text_input("On average how much do you drive per month (numeric only)")
units = st.selectbox("What was the units of the previous answer?", ["Kilometers", "Miles"])
fuel_type = st.selectbox("What is your car's fuel type?", ["Petrol", "Diesel", "Hybrid"])
size_car = st.selectbox("What size car do you drive?", ["Small", "Average/mixed", "SUV", "Truck"])

st.write("#")

# Airplane portion

st.header("Airplane")

air_usage =st.text_input("How much do you fly per year? (units depend on previous input)")
# add the airline q later

st.write("#")
st.header("Home Appliance")
# Home appliance portion

light_type = st.selectbox("Do you utilize LED's or other conventional bulbs", ["LED", "Conventional"])
solar_panels = st.selectbox("Do you utilize solar panels for your house?", ["Yes", "No"])
power_usage = st.text_input("How much electricity do you utilize per month? (numeric only, kilowatthour)")

st.write("#")
button = st.button("Calculate carbon footprint")
carbon_footprint = 0
if button:
    if size_car == "Small":
        if fuel_type == "Petrol":
            if units == "Miles":
                carbon_footprint += round(float(km_drive) * 0.32990, 2)

                
            elif units == "Kilometers":
                carbon_footprint += round(float(km_drive) * 0.205, 2)

                
        elif fuel_type == "Diesel":
            if units == "Miles":
                carbon_footprint += round(float(km_drive) * 0.296, 2)

                
            if units == "Kilometers":
                carbon_footprint += round(float(km_drive) * 0.185, 2)

                
                
        elif fuel_type == "Hybrid":
            if units == "Miles":
                carbon_footprint += round(float(km_drive) * 0.227, 2)

                
            if units == "Kilometers":
                carbon_footprint += round(float(km_drive) * 0.142, 2)
                
                
    elif size_car == "Average/mixed":
        if fuel_type == "Petrol":
            if units == "Miles":
                carbon_footprint += round(float(km_drive) * 0.40935, 2)

                
            elif units == "Kilometers":
                carbon_footprint += round(float(km_drive) * 0.40935/1.609, 2)

                
        elif fuel_type == "Diesel":
            if units == "Miles":
                carbon_footprint += round(float(km_drive) * 0.40935, 2)

                
            if units == "Kilometers":
                carbon_footprint += round(float(km_drive) * 0.40935/1.609, 2)

                
                
        elif fuel_type == "Hybrid":
            if units == "Miles":
                carbon_footprint += round(float(km_drive) * 0.227, 2)

                
            if units == "Kilometers":
                carbon_footprint += round(float(km_drive) * 0.142, 2)
                
                
    elif size_car == "SUV":
        if fuel_type == "Petrol":
            if units == "Miles":
                carbon_footprint += round(float(km_drive) * 0.56964, 2)

                
            elif units == "Kilometers":
                carbon_footprint += round(float(km_drive) * 0.56964/1.609, 2)

                
        elif fuel_type == "Diesel":
            if units == "Miles":
                carbon_footprint += round(float(km_drive) * 0.56964, 2)

                
            if units == "Kilometers":
                carbon_footprint += round(float(km_drive) * 0.56964/1.609, 2)

                
                
        elif fuel_type == "Hybrid":
            if units == "Miles":
                carbon_footprint += round(float(km_drive) * 0.227, 2)

                
            if units == "Kilometers":
                carbon_footprint += round(float(km_drive) * 0.142, 2)
   
    if units == "Miles":
        carbon_footprint += round(float(air_usage) * 0.257, 2)
        
    elif units == "Kilometers":
        carbon_footprint += round(float(air_usage) * 0.257/1.609, 2)
        
    carbon_footprint += round(float(power_usage) * 0.38782148, 2)
    
    st.write("Your carbon footprint is: ", carbon_footprint, "kg CO2e")

        
        

                
                
                
        