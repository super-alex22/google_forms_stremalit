import streamlit as st
import time
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-family: "Segoe UI Emoji", "Noto Color Emoji", "Apple Color Emoji", sans-serif;
}
</style>
""", unsafe_allow_html=True)
if 'counter' not in st.session_state:
    st.session_state.counter = 0
if 'answer_result' not in st.session_state:
    st.session_state.answer_result = None;
if 'btn_disabled' not in st.session_state: 
    st.session_state.btn_disabled = False

if 'btn_disabled_q2' not in st.session_state: 
    st.session_state.btn_disabled_q2 = False
    
if 'answer_result_q2' not in st.session_state: 
    st.session_state.answer_result_q2 = None
if 'answer_result_q3' not in st.session_state:
    st.session_state.answer_result_q3 = None
if 'btn_disabled_q3' not in st.session_state:
    st.session_state.btn_disabled_q3 = False
if 'btn_disabled_q4' not in st.session_state:
    st.session_state.btn_disabled_q4 = False
if 'answer_result_q4' not in st.session_state:
    st.session_state.answer_result_q4 = None
if 'btn_disabled_q5' not in st.session_state:
    st.session_state.btn_disabled_q5 = False
if 'answer_result_q5' not in st.session_state:
    st.session_state.answer_result_q5 = None
if 'quiz_finished' not in st.session_state:
    st.session_state.quiz_finished = False

countries_list = ["🇦🇫 Afghanistan","🇦🇱 Albania","🇩🇿 Algeria","🇦🇩 Andorra","🇦🇴 Angola","🇦🇬 Antigua and Barbuda","🇦🇷 Argentina","🇦🇲 Armenia","🇦🇺 Australia","🇦🇹 Austria","🇦🇿 Azerbaijan","🇧🇸 Bahamas","🇧🇭 Bahrain","🇧🇩 Bangladesh","🇧🇧 Barbados","🇧🇾 Belarus","🇧🇪 Belgium","🇧🇿 Belize","🇧🇯 Benin","🇧🇹 Bhutan","🇧🇴 Bolivia","🇧🇦 Bosnia and Herzegovina","🇧🇼 Botswana","🇧🇷 Brazil","🇧🇳 Brunei","🇧🇬 Bulgaria","🇧🇫 Burkina Faso","🇧🇮 Burundi","🇨🇻 Cabo Verde","🇰🇭 Cambodia","🇨🇲 Cameroon","🇨🇦 Canada","🇨🇫 Central African Republic","🇹🇩 Chad","🇨🇱 Chile","🇨🇳 China","🇨🇴 Colombia","🇰🇲 Comoros","🇨🇬 Congo","🇨🇩 Congo (DRC)","🇨🇷 Costa Rica","🇨🇮 Côte d’Ivoire","🇭🇷 Croatia","🇨🇺 Cuba","🇨🇾 Cyprus","🇨🇿 Czech Republic","🇩🇰 Denmark","🇩🇯 Djibouti","🇩🇲 Dominica","🇩🇴 Dominican Republic","🇪🇨 Ecuador","🇪🇬 Egypt","🇸🇻 El Salvador","🇬🇶 Equatorial Guinea","🇪🇷 Eritrea","🇪🇪 Estonia","🇸🇿 Eswatini","🇪🇹 Ethiopia","🇫🇯 Fiji","🇫🇮 Finland","🇫🇷 France","🇬🇦 Gabon","🇬🇲 Gambia","🇬🇪 Georgia","🇩🇪 Germany","🇬🇭 Ghana","🇬🇷 Greece","🇬🇩 Grenada","🇬🇹 Guatemala","🇬🇳 Guinea","🇬🇼 Guinea-Bissau","🇬🇾 Guyana","🇭🇹 Haiti","🇭🇳 Honduras","🇭🇺 Hungary","🇮🇸 Iceland","🇮🇳 India","🇮🇩 Indonesia","🇮🇷 Iran","🇮🇶 Iraq","🇮🇪 Ireland","🇮🇱 Israel","🇮🇹 Italy","🇯🇲 Jamaica","🇯🇵 Japan","🇯🇴 Jordan","🇰🇿 Kazakhstan","🇰🇪 Kenya","🇰🇮 Kiribati","🇰🇼 Kuwait","🇰🇬 Kyrgyzstan","🇱🇦 Laos","🇱🇻 Latvia","🇱🇧 Lebanon","🇱🇸 Lesotho","🇱🇷 Liberia","🇱🇾 Libya","🇱🇮 Liechtenstein","🇱🇹 Lithuania","🇱🇺 Luxembourg","🇲🇬 Madagascar","🇲🇼 Malawi","🇲🇾 Malaysia","🇲🇻 Maldives","🇲🇱 Mali","🇲🇹 Malta","🇲🇭 Marshall Islands","🇲🇷 Mauritania","🇲🇺 Mauritius","🇲🇽 Mexico","🇫🇲 Micronesia","🇲🇩 Moldova","🇲🇨 Monaco","🇲🇳 Mongolia","🇲🇪 Montenegro","🇲🇦 Morocco","🇲🇿 Mozambique","🇲🇲 Myanmar","🇳🇦 Namibia","🇳🇷 Nauru","🇳🇵 Nepal","🇳🇱 Netherlands","🇳🇿 New Zealand","🇳🇮 Nicaragua","🇳🇪 Niger","🇳🇬 Nigeria","🇰🇵 Democratic People's Republic of Korea (DPRK)","🇲🇰 North Macedonia","🇳🇴 Norway","🇴🇲 Oman","🇵🇰 Pakistan","🇵🇼 Palau","🇵🇦 Panama","🇵🇬 Papua New Guinea","🇵🇾 Paraguay","🇵🇪 Peru","🇵🇭 Philippines","🇵🇱 Poland","🇵🇹 Portugal","🇶🇦 Qatar","🇷🇴 Romania","🇷🇺 Russia","🇷🇼 Rwanda","🇰🇳 Saint Kitts and Nevis","🇱🇨 Saint Lucia","🇻🇨 Saint Vincent and the Grenadines","🇼🇸 Samoa","🇸🇲 San Marino","🇸🇹 São Tomé and Príncipe","🇸🇦 Saudi Arabia","🇸🇳 Senegal","🇷🇸 Serbia","🇸🇨 Seychelles","🇸🇱 Sierra Leone","🇸🇬 Singapore","🇸🇰 Slovakia","🇸🇮 Slovenia","🇸🇧 Solomon Islands","🇸🇴 Somalia","🇿🇦 South Africa","🇰🇷 South Korea","🇸🇸 South Sudan","🇪🇸 Spain","🇱🇰 Sri Lanka","🇸🇩 Sudan","🇸🇷 Suriname","🇸🇪 Sweden","🇨🇭 Switzerland","🇸🇾 Syria","🇹🇯 Tajikistan","🇹🇿 Tanzania","🇹🇭 Thailand","🇹🇱 Timor-Leste","🇹🇬 Togo","🇹🇴 Tonga","🇹🇹 Trinidad and Tobago","🇹🇳 Tunisia","🇹🇷 Turkey","🇹🇲 Turkmenistan","🇹🇻 Tuvalu","🇺🇬 Uganda","🇺🇦 Ukraine","🇦🇪 United Arab Emirates","🇬🇧 United Kingdom","🇺🇸 United States","🇺🇾 Uruguay","🇺🇿 Uzbekistan","🇻🇺 Vanuatu","🇻🇦 Vatican City","🇻🇪 Venezuela","🇻🇳 Vietnam","🇾🇪 Yemen","🇿🇲 Zambia","🇿🇼 Zimbabwe","🇽🇰 Kosovo (частично признано)","🇹🇼 Taiwan (частично признано)","🇵🇸 Palestine (частично признано)","🇪🇭 Western Sahara (частично признано)"]

st.write("This is a geography quiz. Let's see how good your skills are")
st.write("I'd like humbly have you requested to enter your name here")
name = st.text_input("Have your name stated here")
gender = st.radio("Gender", ["Male", "Female", "Other", "Custom", "Prefer not to be shared"])
if gender == "Custom":
  gender_custom = st.text_input("Kindly have your gender stated here")
  st.write("Have me considered as")
  gender_custom_type = st.radio("Gender", ["Male", "Female", "Other"])
age = st.number_input("Kindly have your age stated here")
if age<1:
  st.error("You haven't been born yet. See you back when you are")
else:
  st.success("Your Mightiness is old enough to have this quiz completed")

country = st.selectbox(
    "Select your country of residence:",
    options=countries_list,
    index=None,
    placeholder="Start typing (e.g. Iceland)..."
)

if country:
    st.write(f"You selected: **{country}**")
    if "Belarus" in country or "Russia" in country or "DPRK" in country:
        st.error("These countries are destroying Ukraine's independency. The user registration from that countries is not currently possible.")
    else:
        st.success("Thank you for choosing your country.")
        
    with st.form("quiz_form"):
        st.write("Which city is the only one in the world to be located on two continents?")
        question1 = st.radio("City", ["Choose answer","Rome","Istanbul", "Cairo", "Panama City"])
        question1_submit = st.form_submit_button("Submit", disabled=st.session_state.btn_disabled)
        if question1_submit == True and question1 != "Choose answer":
            st.session_state.btn_disabled = True
            
            st.warning(f"Your answer is {question1}")
            if question1 == "Istanbul":
                
                st.session_state.answer_result = "True"
            else:
                st.session_state.answer_result = "Incorrect"
            st.rerun()
        else:
            st.warning("This question is mandatory if Your Mightiness would like to have proceeded")
if st.session_state.answer_result == "True":
    st.success("Hooray! The answer is correct")
elif st.session_state.answer_result == "Incorrect":
    st.error("The answer is incorrect")

if st.session_state.answer_result == "True" or st.session_state.answer_result == "Incorrect":
    with st.form("quiz_form_2"):
        st.write("How many countries (officially recognised members of the UN) are there in the world at present?")
        question2 = st.slider("Countries amount", 150, 200, None, 1)
        question2_submit = st.form_submit_button("Submit", disabled=st.session_state.btn_disabled_q2)
        if question2_submit == True:
            st.session_state.btn_disabled_q2 = True
            st.warning(f"Your answer is {question2}")
            if question2 == 193:
                st.session_state.answer_result_q2 = "True"
            else:
                st.session_state.answer_result_q2 = "Incorrect"
            st.rerun()
if st.session_state.answer_result_q2 == "True":
    st.success("Hooray! The answer is correct")
elif st.session_state.answer_result_q2 == "Incorrect":
    st.error("The answer is incorrect")

if st.session_state.answer_result_q2 is not None:
    with st.form("quiz_form_3"):
        st.write("Which of these countries do NOT have access to the sea?")
        question3 = st.multiselect("Countries", ["Switzerland", "Mongolia", "Portugal", "Hungary"])
        question3_submit = st.form_submit_button("Submit", disabled=st.session_state.btn_disabled_q3)
        if question3_submit == True:
            st.session_state.btn_disabled_q3 = True
            st.warning(f"Your answer is {question3}")
            if "Switzerland" in question3 and "Mongolia" in question3 and "Hungary" in question3 and "Portugal" not in question3:
                st.session_state.answer_result_q3 = "True"
            else:
                st.session_state.answer_result_q3 = "Incorrect"
            st.rerun()
if st.session_state.answer_result_q3 == "True":
    st.success("Hooray! The answer is correct")
elif st.session_state.answer_result_q3 == "Incorrect":
    st.error("The answer is incorrect")
if st.session_state.answer_result_q3 is not None:
     with st.form("quiz_form_4"):
        st.write("Select the typical temperature range in the Sahara Desert during the day (°C)")
        question4 = st.select_slider(
            "Select a range",
            options = [-40, -35, -30, -25, -20, -15, -10, -5, 0, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
            value = (25, 50)
        )
        question4_submit = st.form_submit_button("Submit", disabled=st.session_state.btn_disabled_q4)
        if question4_submit == True:
            st.session_state.btn_disabled_q4 = True
            st.warning(f"Your answer is {question4}")
            min_value = question4[0]
            max_value = question4[1]
            if (min_value>=30 and max_value>=50 and max_value<65):
                st.session_state.answer_result_q4 = "True"
            else:
                st.session_state.answer_result_q4 = "Incorrect"
            st.rerun()
if st.session_state.answer_result_q4 == "True":
    st.success("Hooray! The answer is correct")
elif st.session_state.answer_result_q4 == "Incorrect":
    st.error("The answer is incorrect")
if st.session_state.answer_result_q4 is not None:
     with st.form("quiz_form_5"):
        st.write("What is the height of Mount Everest in meters?")
        question5 = st.number_input("Type a number", value=0, placeholder="Type a number...")
        question5_submit = st.form_submit_button("Submit", disabled=st.session_state.btn_disabled_q5)
        if question5_submit == True:
            if question5>0:
                st.session_state.btn_disabled_q5 = True
                st.warning(f"Your answer is {question5}")
                if question5>8800 and question5<8900:
                    st.session_state.answer_result_q5 = "True"
                else:
                    st.session_state.answer_result_q5 = "Incorrect"
            else:
                st.error("Enter a valid number")
            st.rerun()

if st.session_state.answer_result_q5 == "True":
    st.success("Hooray! The answer is correct")
elif st.session_state.answer_result_q5 == "Incorrect":
    st.error("The answer is incorrect")
if st.session_state.answer_result_q5 is not None:
    with st.form("final_submit_form"):
        st.write("All questions answered. Submit your quiz!")
        final_submit = st.form_submit_button("Submit Quiz")

        if final_submit:
            st.session_state.quiz_finished = True
if st.session_state.quiz_finished:
    st.balloons()
    st.session_state.counter = 0
    st.toast("Quiz finished! 🎉")
    if st.session_state.answer_result == "True":
        st.session_state.counter+=1
    if st.session_state.answer_result_q2 == "True":
        st.session_state.counter+=1
    if st.session_state.answer_result_q3 == "True":
        st.session_state.counter+=1
    if st.session_state.answer_result_q4 == "True":
        st.session_state.counter+=1
    if st.session_state.answer_result_q5 == "True":
        st.session_state.counter+=1
    st.session_state.quiz_finished = False
    if st.session_state.counter <= 1:
        st.toast(f"Score: {st.session_state.counter}/5 — Geography is not your thing yet 🌍😅", icon="🟥")

    elif 2 <= st.session_state.counter <= 3:
        st.toast(f"Score: {st.session_state.counter}/5 — Not bad! Future explorer detected 🧭", icon="🟧")

    elif st.session_state.counter == 4:
        st.toast(f"Score: {st.session_state.counter}/5 — Geography Mastermind! 🧠🌍", icon="🟨")

    elif st.session_state.counter == 5:
        st.toast(f"Score: {st.session_state.counter}/5 — GEOGRAPHY GOD MODE ACTIVATED 👑🌍", icon="🟩")
            
