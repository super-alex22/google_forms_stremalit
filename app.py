import streamlit as st
import time
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-family: "Segoe UI Emoji", "Noto Color Emoji", "Apple Color Emoji", sans-serif;
}
</style>
""", unsafe_allow_html=True)
if 'answer_result' not in st.session_state:
    st.session_state.answer_result = None;
if 'btn_disabled' not in st.session_state: 
    st.session_state.btn_disabled = False
if st.session_state.answer_result == "True":
    st.session_state.btn_disabled = True
    st.success("Hooray! The answer is correct")


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
                
                st.success("Hooray! The answer is correct")
                st.session_state.answer_result = "True"
            else:
                st.error("The answer is incorrect")
                st.session_state.answer_result = "Incorrect"
        elif st.session_state.answer_result == "True":
            st.success("Hooray! The answer is correct")
        elif (question1_submit == True and question1 != "Choose answer") or (question1 == "Rome" and question1_submit == True) or (question1_submit == True and question1 == "Cairo") or (question1 == "Panama City" and question1_submit == True):
            st.session_state.btn_disabled = True
            st.session_state.answer_result = "False"
            st.error("The answer is incorrect")
            time.sleep(2)
            st.rerun()
        else:
            st.warning("This question is mandatory if Your Mightiness would like to have proceeded")
