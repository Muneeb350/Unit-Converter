import streamlit as st

st.title("🔁 Unit Converter App")
st.markdown("### Converts Length, Time and Speed instantly")
st.write("Welcome! Select a category, enter a value and get the converted result")


category = st.selectbox("Choose a category", ["Length", "Time", "Speed"])
 
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
        
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value *60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
        
    elif category == "Speed":
        if unit == "m/s to km/h":
            return value * 3.6
        elif unit == "km/h to m/s":
            return value / 3.6
        elif unit == "m/s to mph":
            return value * 2.23694
        elif unit == "mph to m/s":
            return value / 2.23694
        elif unit == "km/h to mph":
            return value * 0.621371
        elif unit == "mph to km/h":
            return value / 0.621371
        elif unit == "knots to km/h":
            return value * 1.852
        elif unit == "km/h to knots":
            return value / 1.852
        
if category == "Length":
    unit = st.selectbox("📏 Select conversion", ["Kilometers to miles", "Miles to kilometers"])
elif category == "Time":
    unit = st.selectbox("⏱️ Select conversion", ["Seconds to minutes", "Minutes to seconds",
                            "Minutes to hours", "Hours to minutes", "Hours to days", 
                            "Days to hours"])

elif category == "Speed":
    unit = st.selectbox("⚡ Select conversion", ["m/s to km/h", "km/h to m/s", "m/s to mph",
                            "mph to m/s", "km/h to mph", "mph to km/h", "knots to km/h", 
                            "km/h to knots"])
    
value = st.number_input("Enter the value to convert", min_value=0.0)

if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        converted_to = unit.split("to")[1]
        st.success(f"The result is {result:.2f}{converted_to}")
    else:
        st.error("⚠️ Conversion not supported or something went wrong.")
    