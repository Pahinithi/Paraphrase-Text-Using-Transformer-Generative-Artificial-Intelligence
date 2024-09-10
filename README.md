# Paraphrase Text Using Transformer

## Overview

This project provides a tool for generating multiple paraphrased versions of a given text using the Google Pegasus model. It offers a user-friendly interface built with FastAPI and styled using Bootstrap and custom CSS. The application leverages advanced NLP techniques to transform input text into varied paraphrases.

## Features

- **Paraphrase Generation**: Uses the Google Pegasus model to generate diverse paraphrases of the input text.
- **User Interface**: Clean and responsive design implemented with FastAPI and Bootstrap.
- **Custom Styling**: Enhanced UI/UX with custom CSS for a polished look.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Pahinithi?tab=repositories
   cd Paraphrase-Text-Using-Transformer
   ```

2. **Install the Required Packages:**

   Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the FastAPI Server:**

   ```bash
   uvicorn app:app --reload
   ```

2. **Open Your Browser and Navigate to:**

   ```
   http://127.0.0.1:8000
   ```

3. **Use the Application:**

   - Enter the text you want to paraphrase.
   - Specify the number of paraphrases you need.
   - Click "Generate" to see the paraphrased versions of your text.

## Code Structure

- **`app.py`**: FastAPI application that serves the web interface and handles form submissions.
- **`generate.py`**: Contains the logic for generating paraphrases using the Pegasus model.
- **`templates/index.html`**: HTML template for the user interface.
- **`static/styles.css`**: Custom styles for the application.
- **`requirements.txt`**: List of required Python packages.

## Screenshots

<img width="1728" alt="AI03" src="https://github.com/user-attachments/assets/de85f6ec-90d4-49a6-b6fc-55e8bd8a36b4">


## Demo

A live demo of the application can be found [here](https://drive.google.com/file/d/1NhT2ScUhTxYvYUc3b7H1YQWUKq2MDMiM/view?usp=sharing).

## Contributing

If you would like to contribute to this project:

1. Fork the repository on GitHub.
2. Create a new branch for your changes.
3. Commit your changes and push them to your forked repository.
4. Open a pull request with a description of your changes.

## License

This project is licensed under the MIT License.

