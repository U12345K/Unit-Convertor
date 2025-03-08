import streamlit as st

# Apply custom styling
st.markdown("""
    <style>
        body {
            background-color: rgb(3, 3, 3);
            color: white;
        }
        .stApp {
            background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 10px rgba(0, 0, 0, 0.3);
        }
        h1 {
            text-align: center;
            font-size: 36px;
            color: white;
        }
        .stButton {
            background: linear-gradient(45deg, #0b6394, #351c75);
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s;
            box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
        }
        .stButton:hover {
            background: linear-gradient(45deg, #92fe9d, #00c9ff);
            transform: scale(1.05);
            color: black;
        }
        .result-box {
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            color: black;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown("<h1>Unit Converter</h1>", unsafe_allow_html=True)
st.write("This converter helps you transform units from one type to another.")

# Sidebar for conversion type
conversion_type = st.sidebar.selectbox(
    "Select Conversion Type", ["Length", "Weight", "Temperature", "Time"]
)

# Input value
value = st.number_input(
    "Enter the value to convert", value=0.0, min_value=0.0, step=0.1
)

# Columns for 'From' and 'To' unit selection
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Centimeters", "Kilometers", "Miles", "Feet", "Yards", "Inches"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Centimeters", "Kilometers", "Miles", "Feet", "Yards", "Inches"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

elif conversion_type == "Time":
    with col1:
        from_unit = st.selectbox("From", ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"])
    with col2:
        to_unit = st.selectbox("To", ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"])

# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {"Meters": 1, "Centimeters": 100, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084, "Yards": 1.09361, "Inches": 39.3701}
    return value / length_units[from_unit] * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {"Kilograms": 1, "Grams": 1000, "Milligrams": 1000000, "Pounds": 2.20462, "Ounces": 35.274}
    return value / weight_units[from_unit] * weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9 / 5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return ((value - 32) * 5 / 9) if to_unit == "Celsius" else ((value - 32) * 5 / 9 + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9 / 5 + 32) if to_unit == "Fahrenheit" else value
    return value

def time_converter(value, from_unit, to_unit):
    time_units = {"Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400, "Weeks": 604800, "Months": 2629746, "Years": 31556952}
    return value / time_units[from_unit] * time_units[to_unit]

# Button and result
if st.button("Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    elif conversion_type == "Time":
        result = time_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} is equal to {result} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Developed by UMAR KHAN</div>", unsafe_allow_html=True)
