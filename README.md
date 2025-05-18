# EZHostz - Multi Agent Content Generation

## Project Overview
EZHostz is a demo project showcasing the power of CrewAI agents collaborating to generate high-quality content efficiently. This project demonstrates how multiple AI agents can work together to research a topic and write detailed articles using AI language models and web search tools.

The project includes:
- A Streamlit web app for interactive content generation.
- A standalone Python script to run the content generation workflow.
- Integration with CrewAI and SerperDev search tool for research and writing.

## Features
- Multi-agent collaboration: Senior Research Analyst and Content Writer agents.
- Configurable AI language model parameters (temperature).
- Configurable number of search results for research.
- Streamlit interface for easy topic input and content generation.
- Download generated content as markdown files.

## Requirements
- Python version 3.12 or lower (higher than 3.7)
- The dependencies listed in `requirements.txt`:
  - crewai
  - crewai-tools
  - python-dotenv
  - streamlit

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add any necessary environment variables (e.g., API keys for SerperDev).

## Running the Project

### Streamlit Web App
To launch the interactive Streamlit app:
```bash
streamlit run streamlit_app.py
```
- Enter the topic for content generation.
- Adjust the temperature and number of search results.
- Click "Generate Content" to start the process.
- Download the generated article as a markdown file.

### Standalone Script
To run the content generation script directly:
```bash
python app.py
```
- This script runs a predefined topic ("Harms of Social Media") and prints the generated content to the console.

## Contributing
Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them with clear messages.
4. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request describing your changes.

Please ensure your code follows the existing style and includes appropriate documentation.

## License
This project is open for contributions and collaboration. Feel free to use and modify the code as needed.

---

Built with ❤️ by EZHostz
