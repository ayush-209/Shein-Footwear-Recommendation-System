import pandas as pd
import streamlit as st
import pickle

def add_https(url):
    if not url.startswith('https:'):
        return 'https:' + url
    return url


def recommend_shoes(shoe):
    shoe_idx = shoes[shoes['name'] == shoe].index[0]
    distances = cosine_sim[shoe_idx]
    shoe_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]
    rec_shoes_list = []
    shoes_link_list = []
    img_list = []
    for i in shoe_list:
        rec_shoes_list.append(shoes.iloc[i[0]]['name'])
        shoes_link_list.append(shoes.iloc[i[0]]['link'])
        img_list.append(shoes.iloc[i[0]]['hero_image'])
    return rec_shoes_list, shoes_link_list, img_list

st.title('Shein Shoes Recommender')

shoes_dict = pickle.load(open('shoes_dict.pkl', 'rb'))
shoes = pd.DataFrame(shoes_dict)
popular_dict = pickle.load(open('popular_dict.pkl', 'rb'))
popular = pd.DataFrame(popular_dict)
cosine_sim = pickle.load(open('cosine_sim.pkl', 'rb'))

shoes['hero_image'] = shoes['hero_image'].apply(add_https)
popular['hero_image'] = popular['hero_image'].apply(add_https)

search_query = st.selectbox(label='Please search for a pair of shoes or select one from the options after clicking the drop down button', options=shoes['name'].values)

recommend_button = st.button(label='Search similar shoes')

if recommend_button:
    recommendations, links, images = recommend_shoes(search_query)
    rec_no = 1
    for i, j, k in zip(recommendations, links, images):
        st.subheader(f'Recommendation {rec_no}:')
        st.image(k, width=200)
        st.write(i)
        st.markdown(f'Visit the [store]({j})')
        rec_no += 1
st.divider()

st.header('Most popular among customers')
cols = st.columns(5)

with cols[0]:
    st.subheader('1st most popular')
    st.image(popular.iloc[0]['hero_image'])
    st.write(popular.iloc[0]['name'][:40]+ '...')
    st.markdown(f'visit [store]({popular.iloc[0]["link"]})')

with cols[1]:
    st.subheader('2nd most popular')
    st.image(popular.iloc[1]['hero_image'])
    st.write(popular.iloc[1]['name'][:40]+ '...')
    st.markdown(f'visit [store]({popular.iloc[1]["link"]})')

with cols[2]:
    st.subheader('3rd most popular')
    st.image(popular.iloc[2]['hero_image'])
    st.write(popular.iloc[2]['name'][:40]+ '...')
    st.markdown(f'visit [store]({popular.iloc[2]["link"]})')

with cols[3]:
    st.subheader('4th most popular')
    st.image(popular.iloc[3]['hero_image'])
    st.write(popular.iloc[3]['name'][:40]+ '...')
    st.markdown(f'visit [store]({popular.iloc[3]["link"]})')

with cols[4]:
    st.subheader('5th most popular')
    st.image(popular.iloc[4]['hero_image'])
    st.write(popular.iloc[4]['name'])
    st.markdown(f'visit [store]({popular.iloc[4]["link"]})')

