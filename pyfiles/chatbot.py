import streamlit as st

from optimize import main

st.title("CFD optimization chatbot")
st.write("Enter initial inlet temperature here!")

input_temperature = st.number_input("Initial temperature: ", value=1.0)

if st.button("Run optimization"):
    with st.spinner("Running optimization..."):
        try:
            optimal_values = main(input_temperature)
            st.success("Optimization finished!")
            st.write("Velocity", optimal_values.x[0])
            st.write("Temperature", optimal_values.fun)
        except Exception as e:
            st.error("Error occurred!", e)