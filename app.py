import streamlit as st
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import plotly.express as px

# Download necessary NLTK data
nltk.download('vader_lexicon')

# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    sentiment = sia.polarity_scores(text)
    if sentiment['compound'] >= 0.05:
        return 'Positive'
    elif sentiment['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def get_recommendation(positive_count, total_count):
    """
    Đưa ra quyết định dựa trên tỷ lệ đánh giá tích cực
    """
    positive_percentage = (positive_count / total_count) * 100
    
    if positive_percentage >= 70:
        return "Highly Recommended ⭐⭐⭐⭐⭐", "Sản phẩm được đánh giá rất tốt, nên mua!"
    elif positive_percentage >= 50:
        return "Recommended ⭐⭐⭐⭐", "Sản phẩm được đánh giá khá tốt, có thể cân nhắc mua."
    elif positive_percentage >= 30:
        return "Neutral ⭐⭐⭐", "Sản phẩm có đánh giá trung bình, cần cân nhắc kỹ."
    else:
        return "Not Recommended ⭐⭐", "Sản phẩm có nhiều đánh giá tiêu cực, không nên mua."

def main():
    st.title('Product Review Analysis System')
    
    # Create tabs
    tab1, tab2 = st.tabs(["Single Review Analysis", "Bulk Analysis"])
    
    with tab1:
        # Single review analysis
        st.header("Analyze a Single Review")
        user_input = st.text_area("Enter your review text here:")
        
        if st.button("Analyze"):
            if user_input:
                sentiment = analyze_sentiment(user_input)
                scores = sia.polarity_scores(user_input)
                
                # Display results in columns
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Sentiment Analysis")
                    st.write(f"Overall Sentiment: {sentiment}")
                    st.write("Detailed Scores:")
                    st.write(f"Positive: {scores['pos']:.2f}")
                    st.write(f"Neutral: {scores['neu']:.2f}")
                    st.write(f"Negative: {scores['neg']:.2f}")
                    st.write(f"Compound: {scores['compound']:.2f}")
                
                with col2:
                    st.subheader("Recommendation")
                    if sentiment == 'Positive':
                        st.success("This is a positive review! 👍")
                    elif sentiment == 'Negative':
                        st.error("This is a negative review! 👎")
                    else:
                        st.warning("This is a neutral review! 😐")
    
    with tab2:
        # Bulk analysis
        st.header("Analyze Multiple Reviews")
        uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
        
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            
            if 'Review' in df.columns:
                # Analyze sentiments
                df['Sentiment'] = df['Review'].apply(analyze_sentiment)
                
                # Calculate sentiment counts
                sentiment_counts = df['Sentiment'].value_counts()
                positive_count = sentiment_counts.get('Positive', 0)
                total_count = len(df)
                
                # Create columns for visualization
                col1, col2 = st.columns(2)
                
                with col1:
                    # Show sentiment distribution pie chart
                    fig_pie = px.pie(values=sentiment_counts.values, 
                                   names=sentiment_counts.index,
                                   title='Sentiment Distribution')
                    st.plotly_chart(fig_pie)
                
                with col2:
                    # Show sentiment distribution bar chart
                    fig_bar = px.bar(x=sentiment_counts.index, 
                                   y=sentiment_counts.values,
                                   title='Sentiment Counts')
                    st.plotly_chart(fig_bar)
                
                # Get recommendation
                recommendation, explanation = get_recommendation(positive_count, total_count)
                
                # Display recommendation
                st.subheader("Overall Recommendation")
                st.write(f"**{recommendation}**")
                st.write(explanation)
                
                # Show additional metrics
                col3, col4, col5 = st.columns(3)
                
                with col3:
                    positive_pct = (sentiment_counts.get('Positive', 0) / total_count) * 100
                    st.metric("Positive Reviews", f"{positive_pct:.1f}%")
                
                with col4:
                    neutral_pct = (sentiment_counts.get('Neutral', 0) / total_count) * 100
                    st.metric("Neutral Reviews", f"{neutral_pct:.1f}%")
                
                with col5:
                    negative_pct = (sentiment_counts.get('Negative', 0) / total_count) * 100
                    st.metric("Negative Reviews", f"{negative_pct:.1f}%")
                
                # Show the dataframe with results
                st.subheader("Detailed Analysis Results")
                st.dataframe(df)
                
                # Download results
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download Analysis Results",
                    data=csv,
                    file_name="sentiment_analysis_results.csv",
                    mime="text/csv"
                )
            else:
                st.error("CSV file must contain a 'Review' column")

if __name__ == "__main__":
    main()