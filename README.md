# READQUEST

This project is a Streamlit app that provides personalized book recommendations based on user-specified genres. It retrieves book information from the Open Library API and enhances the recommendations using OpenAI's GPT model. Users can download a detailed PDF report of the recommendations.

## Features

- **Retrieve Book Information**: Fetch book data from the Open Library API based on specified genres.
- **Enhance Recommendations**: Get detailed and personalized book recommendations generated using OpenAI's GPT model.
- **Downloadable PDF Report**: Download a PDF report containing the personalized book recommendations.

## Requirements

- Python 3.7 or higher
- An OpenAI API key

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/personalized-book-recommendation.git
    cd personalized-book-recommendation
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables in a `.env` file:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Enter your preferred genres (comma-separated) into the text area.

3. Click "Get Recommendations" to fetch book information, enhance recommendations, and generate a PDF report.

4. Download the PDF report of the recommendations if desired.

## Dependencies

- `streamlit`
- `openai`
- `requests`
- `python-dotenv`
- `fpdf`

## Example

1. Input genres such as "horror, thriller" into the text area.
2. The app will fetch book information for the specified genres.
3. Enhanced recommendations will be displayed, and a downloadable PDF report will be generated.

## License

This project is licensed under the MIT License.
