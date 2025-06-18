import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide")  # make app use full width
st.header("Codeforces Analysis")
handle = st.text_input("Enter your codeforces username")
st.subheader("Valleys")

def isUrl(url):
    try:
        return requests.get(url).status_code == 200
    except:
        return False

def getResult(url):
    try:
        return requests.get(url).json()['result'] if isUrl(url) else []
    except:
        return []

def findValleysAndPlot(url):
    result = getResult(url)
    if len(result) > 2:
        contests = [entry['contestName'] for entry in result]
        ratings = [entry['newRating'] for entry in result]
        cat_index = pd.CategoricalIndex(contests, categories=contests, ordered=True)

        # Split screen into 2 columns
        left_col, right_col = st.columns(2)

        with left_col:
            with st.container():
                st.subheader("📈 Rating / Contest Number")
                df_rc = pd.DataFrame({
                    'Rating/Contest': [ratings[i] / (i + 1) for i in range(len(ratings))]
                }, index=cat_index)
                st.line_chart(df_rc, use_container_width=True)

            with st.container():
                st.subheader("📈 Ratings Over Contests")
                df_rating = pd.DataFrame({
                    'Rating': ratings
                }, index=cat_index)
                st.line_chart(df_rating, use_container_width=True)

        with right_col:
            valleys = []
            for i in range(len(result) - 1):
                r1 = result[i]
                r2 = result[i + 1]
                if r1['oldRating'] > r1['newRating'] and r2['oldRating'] < r2['newRating']:
                    valleys.append({
                        'Turning Points': r2['contestName'],
                        'Pre-Valley': r1['oldRating'],
                        'Valley': r1['newRating'],
                        'Post-Valley': r2['newRating'],
                        'Fall': r1['oldRating'] - r1['newRating'],
                        'Rise': r2['newRating'] - r2['oldRating']
                    })

            if valleys:
                st.subheader("📉 Detected Rating Valleys")
                df_valleys = pd.DataFrame(valleys)

                def highlight_rows(row):
                    if row['Fall'] < row['Rise']:
                        color = 'background-color: rgba(144, 238, 144, 0.4)'  # light transparent green
                    else:
                        color = 'background-color: rgba(255, 0, 0, 0.7)'      # bright transparent red
                    return [color] * len(row)

                # Calculate number of green and red rows
                green_count = sum(1 for row in valleys if (row['Fall'] < row['Rise']))
                red_count = len(valleys) - green_count

                # Show the ratio
                if red_count == 0:
                    ratio_text = "**🟩 Comeback Ratio = Infinite (No bad valleys)**"
                else:
                    ratio_text = f"**🟩 Comeback Ratio = {green_count/red_count:.2f}**"
                st.markdown(ratio_text)

                st.dataframe(df_valleys.style.apply(highlight_rows, axis=1), use_container_width=True)
            else:
                st.info("No rating valleys found (drop followed by rise).")
    else:
        st.warning("Not enough contest data to analyze.")

if handle:
    url = f"https://codeforces.com/api/user.rating?handle={handle}"
    findValleysAndPlot(url)
