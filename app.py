import streamlit as st
countries_with_flags = [
    "🇦🇫 Afghanistan", "🇦🇱 Albania", "🇩🇿 Algeria", "🇦🇩 Andorra", "🇦🇴 Angola", 
    "🇦🇷 Argentina", "🇦🇲 Armenia", "🇦🇺 Australia", "🇦🇹 Austria", "🇦🇿 Azerbaijan", 
    "🇧🇸 Bahamas", "🇧🇭 Bahrain", "🇧🇩 Bangladesh", "🇧🇧 Barbados", "🇧🇪 Belgium", 
    "🇧🇿 Belize", "🇧🇯 Benin", "🇧🇹 Bhutan", "🇧🇴 Bolivia", "🇧🇦 Bosnia and Herzegovina", 
    "🇧🇼 Botswana", "🇧🇷 Brazil", "🇧🇳 Brunei", "🇧🇬 Bulgaria", "🇧🇫 Burkina Faso", 
    "🇧🇮 Burundi", "🇰🇭 Cambodia", "🇨🇲 Cameroon", "🇨🇦 Canada", "🇨🇻 Cape Verde", 
    "🇨🇫 Central African Republic", "🇨🇱 Chile", "🇨🇳 China", "🇨🇴 Colombia", "🇰🇲 Comoros", 
    "🇨🇬 Congo", "🇨🇷 Costa Rica", "🇭🇷 Croatia", "🇨🇺 Cuba", "🇨🇾 Cyprus", 
    "🇨🇿 Czech Republic", "🇩🇰 Denmark", "🇩🇯 Djibouti", "🇩🇲 Dominica", "🇩🇴 Dominican Republic", 
    "🇪🇨 Ecuador", "🇪🇬 Egypt", "🇸🇻 El Salvador", "🇪🇪 Estonia", "🇪🇹 Ethiopia", 
    "🇫🇯 Fiji", "🇫🇮 Finland", "🇫🇷 France", "🇬🇦 Gabon", "🇬🇲 Gambia", 
    "🇬🇪 Georgia", "🇩🇪 Germany", "🇬🇭 Ghana", "🇬🇷 Greece", "🇬🇩 Grenada", 
    "🇬🇹 Guatemala", "🇬🇳 Guinea", "🇬🇼 Guinea-Bissau", "🇬🇾 Guyana", "🇭🇹 Haiti", 
    "🇭🇳 Honduras", "🇭🇺 Hungary", "🇮🇸 Iceland", "🇮🇳 India", "🇮🇩 Indonesia", 
    "🇮🇷 Iran", "🇮🇶 Iraq", "🇮🇪 Ireland", "🇮🇱 Israel", "🇮🇹 Italy", 
    "🇯🇲 Jamaica", "🇯🇵 Japan", "🇯🇴 Jordan", "🇰🇿 Kazakhstan", "🇰🇪 Kenya", 
    "🇰🇷 Korea, South", "🇰🇼 Kuwait", "🇰🇬 Kyrgyzstan", "🇱🇦 Laos", "🇱🇻 Latvia", 
    "🇱🇧 Lebanon", "🇱🇸 Lesotho", "🇱🇷 Liberia", "🇱🇾 Libya", "🇱🇮 Liechtenstein", 
    "🇱🇹 Lithuania", "🇱🇺 Luxembourg", "🇲🇬 Madagascar", "🇲🇼 Malawi", "🇲🇾 Malaysia", 
    "🇲🇻 Maldives", "🇲🇱 Mali", "🇲🇹 Malta", "🇲🇽 Mexico", "🇲🇩 Moldova", 
    "🇲🇨 Monaco", "🇲🇳 Mongolia", "🇲🇪 Montenegro", "🇲🇦 Morocco", "🇲🇿 Mozambique", 
    "🇲🇲 Myanmar", "🇳🇦 Namibia", "🇳🇵 Nepal", "🇳🇱 Netherlands", "🇳🇿 New Zealand", 
    "🇳🇮 Nicaragua", "🇳🇪 Niger", "🇳🇬 Nigeria", "🇳🇴 Norway", "🇴🇲 Oman", 
    "🇵🇰 Pakistan", "🇵🇦 Panama", "🇵🇾 Paraguay", "🇵🇪 Peru", "🇵🇭 Philippines", 
    "🇵🇱 Poland", "🇵🇹 Portugal", "🇶🇦 Qatar", "🇷🇴 Romania", "🇷🇼 Rwanda", 
    "🇰🇳 Saint Kitts and Nevis", "🇱🇨 Saint Lucia", "🇸🇲 San Marino", "🇸🇦 Saudi Arabia", "🇸🇳 Senegal", 
    "🇷🇸 Serbia", "🇸🇨 Seychelles", "🇸🇱 Sierra Leone", "🇸🇬 Singapore", "🇸🇰 Slovakia", 
    "🇸🇮 Slovenia", "🇿🇦 South Africa", "🇪🇸 Spain", "🇱🇰 Sri Lanka", "🇸🇩 Sudan", 
    "🇸🇷 Suriname", "🇸🇪 Sweden", "🇨🇭 Switzerland", "🇸🇾 Syria", "🇹🇼 Taiwan", 
    "🇹🇯 Tajikistan", "🇹🇿 Tanzania", "🇹🇭 Thailand", "🇹🇬 Togo", "🇹🇴 Tonga", 
    "🇹🇹 Trinidad and Tobago", "🇹🇳 Tunisia", "🇹🇷 Turkey", "🇹🇲 Turkmenistan", "🇺🇬 Uganda", 
    "🇺🇦 Ukraine", "🇦🇪 United Arab Emirates", "🇬🇧 United Kingdom", "🇺🇸 United States", "🇺🇾 Uruguay", 
    "🇺🇿 Uzbekistan", "🇻🇦 Vatican City", "🇻🇪 Venezuela", "🇻🇳 Vietnam", "🇾🇪 Yemen", 
    "🇿🇲 Zambia", "🇿🇼 Zimbabwe"
]
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
country = st.selectbox(""Select a country",
    options=countries_with_flags,
    index=None,
    placeholder="Choose an option..."")
