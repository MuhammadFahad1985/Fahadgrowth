import streamlit as st

# st.set_page_config(page_title= "growth mindset projet", project_icon="★")
# st.set_page_config(page_title="Growth Mindset Project", page_icon="star.png")
st.set_page_config(page_title="Growth Mindset Project", page_icon="🌟")


st.title("Growth mindset challange: Web Aap With Streamlit")

st.header("welcome to your growth journey")
st.write("embarace challange, learn from mistake, and unlock your full potential ")

st.header("💡Today Grouth Mindset quote")

st.write("sucess is not final,failure is not fatal: it is courage to continue that counts. ")

st.header("❔ what is your challange on today")
user_input = st.text_input("Describe a challange you're facing:")

if user_input:
    st.success(f"your're facing:{user_input}. keep pushing forward towards your goal!")
else:
    st.warning("Tell us about yout challange to get started!")    

st.header("Reflect on your learning")   
reflection = st.text_area("Write your reflection here:") 

if reflection:
    st.success(f"Great insight! your reflection: {reflection}")

else:
    st.info("reflecting on past experince help your grow ! share your dificulties")

st.header("Celebrate your wins")   
acheivment = st.text_input("share something your are recently accomplished:")

if acheivment:
    st.success(f"Amazing! you achieved:{acheivment} ")

else:
    st.info("big or small, every achivement counts! share your now  ")    

st.write("---")  
st.write("keep believing in yourself. Grouth is a journey, not a destination!") 
st.write("**Crated by Muhammad Fahad**") 

