import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.express as px

cm = sns.light_palette("green", as_cmap=True)
mint_address = '0x0bc3807ec262cb779b38d65b38158acc3bfede10'
auction_house = '0x830bd73e4184cef73443c15111a1df14e495c706' 
def landing_page(key, df,sales,transfers):
    st.image('https://openseauserdata.com/files/e22c98856cf40d4efb9d2dcb69d25c9b.png')
    st.markdown("""## Flipside Crypto: Nouns DAO
                
### Intro

The Nouns are an Ethereum NFT project that brings a unique minting mechanism to the NFT space. One Noun is auctioned trustlessly every 24 hours, forever. 100% of the proceeds from these auctions are sent to the DAO treasury, which as of the time of this writing sits at 24,780 ETH. Getting a Noun won’t be cheap, as recent auctions have closed at over 100 ETH. As a Noun token holder you are entitled to one vote in the DAO, which uses a fork of Compound Governance and controls the treasury. There are no rules about trait rarity, and the artwork is generative and stored on-chain. Once an auction ends, someone must settle the current auction to initiate a new auction, which will restart the minting / auction cycle.

A sub-DAO was recently formed out of Nouns DAO called Lil Nouns DAO. This project has many of the same characteristics of Nouns DAO, except Lil Nouns mint every 15 minutes as opposed to once a day. 

For more details, see https://nouns.wtf/ & https://lilnouns.wtf/
""")
    st.markdown(
        """
        
Every 10th Lil Noun for the first 5 years of the project will be sent to our multisig, where it will be vested and distributed to individual Nounders.

Every 11th Lil Noun for the first 5 years of the project will be sent to the NounsDAO, where they'll be distributed to individual Nouns, Nounders, and community members alike.

Part 1: 
""")
    st.markdown(
        """
### Analyze the mint and secondary NFT marketplace activity for Nouns DAO. 
""")
    
    options = sorted(df['TOKENID'].unique())
    selected = st.selectbox('Select Noun', options[::-1],0)
    transfers_selected = transfers.query('(TOKENID==@selected) & (EVENT_TYPE=="other")').drop(['EVENT_TYPE','TOKENID'],axis=1)
    sales_selected = sales.query('TOKENID==@selected')
    current_address = transfers_selected.sort_values('BLOCK_TIMESTAMP',ascending=False)['NFT_TO_ADDRESS'].iloc[0]
    if current_address == mint_address:
        current_owner = ' Nouns DAO: Treasury'
    elif current_address == auction_house:
        current_owner = 'Nouns DAO: Nouns Auction House Proxy'
    else:
        current_owner = current_address
    st.image(f'https://noun.pics/{selected}.jpg')
    
    st.markdown(f"""{key} {selected} current_owner: [{current_owner}](https://etherscan.io/address/{current_address})  
{sales_selected.shape[0]} sales
                """)
    with st.expander('show data'):
        l,r = st.columns(2)
        with l:
            st.write(f'transfers')
            
            st.dataframe(transfers_selected)
        with r:
            st.write(f'sales')
            st.dataframe(sales_selected)
    
    
    st.markdown("""
### Sales:
                """)
    st.markdown(
        """
### Can we conclude if there are certain types of traits (body, accessory, etc.) that are causing some Nouns to sell or mint for more than others?


Part 2: 
""")
    st.markdown(
        """
### Who is typically settling Nouns auctions? 
""")
    st.markdown(
        """
### Does the winner settle the auction, or does an eager new bidder settle the current auction to begin the next auction?

    """)

    st.markdown(f""" ## Conclusion
                

### Queries used

### Github
    """)