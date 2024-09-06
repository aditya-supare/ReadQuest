import streamlit as st
import openai
import requests
from dotenv import load_dotenv
import os
from fpdf import FPDF

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

def get_book_data(genre):
    url = f"https://openlibrary.org/subjects/{genre}.json"
    response = requests.get(url)
    data = response.json()
    books = data.get('works', [])
    book_list = []
    
    for book in books[:5]:  
        title = book.get('title', 'No title available')
        description = book.get('description', 'No description available')
        book_list.append(f"Title: {title}\nDescription: {description}\n")
    
    return "\n".join(book_list)


def enhance_recommendations(book_list):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert in book recommendations."},
                  {"role": "user", "content": f"Provide detailed and personalized recommendations based on the following list of books:\n\n{book_list}"}],
        max_tokens=1000
    )
    enriched_recommendations = response['choices'][0]['message']['content'].strip()
    return enriched_recommendations


def generate_pdf_report(recommendations):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Personalized Book Recommendations", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=recommendations)

    pdf_output = pdf.output(dest='S')
    return pdf_output.encode('latin1')  


st.title("Personalized Book Recommendation System")

genres = st.text_area("Enter your genres (comma-separated):")

if st.button("Get Recommendations"):
    if not genres:
        st.error("Please enter at least one genre.")
    else:
        try:
            genres_list = [genre.strip().replace(' ', '_').lower() for genre in genres.split(',')]
            book_list = []

            for genre in genres_list:
                st.write(f"Fetching book information for: {genre}")
                content = get_book_data(genre)
                if content:
                    st.write(f"Content retrieved for: {genre}")
                    book_list.append(content)

            if book_list:
                st.subheader("Enhancing Recommendations")
                recommendations = enhance_recommendations("\n".join(book_list))
                
                if "I'm sorry" in recommendations:
                    st.error("No specific book titles found. Please provide more detailed genres or specific book titles.")
                else:
                    st.write("Recommendations:")
                    st.write(recommendations[:1000] + '...')  
                    
                    st.subheader("Generating PDF Report")
                    pdf_report = generate_pdf_report(recommendations)
                    st.download_button("Download Recommendations", pdf_report, file_name="book_recommendations.pdf", mime="application/pdf")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.write("Exception details:", str(e))
