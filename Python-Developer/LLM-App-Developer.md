### Assignment: Build a GenAI-Powered Application with Modern LLM Tools

**Objective:**  
This assignment aims to test a developer’s understanding and implementation of modern Large Language Model (LLM) integration concepts using popular Python libraries such as `streamlit`, `langchain`, `llama-index`, `OpenAI API`, and `ollama`. The developer will build a small application that interacts with a database using natural language queries and visualizes the output in a Streamlit web interface.

**Duration:**  
4-6 hours

**Prerequisites:**
1. **Python Programming**: Good command over Python programming and object-oriented principles.
2. **Basic Knowledge of Databases**: Understanding of basic SQL and database interactions.
3. **Familiarity with Streamlit**: Ability to create interactive web apps using Streamlit.
4. **Experience with LLM APIs**: Experience with integrating LLM APIs like `langchain`, `llama-index`, or OpenAI.

---

### Problem Statement: Build a Natural Language SQL Query Tool

**Task:**
You are required to build a simple web-based tool that allows users to interact with a database using natural language queries. The tool should have the following functionalities:

1. **Input Natural Language Queries**: Users should be able to input queries in plain English (e.g., "Show the top 10 customers by revenue").
2. **Generate SQL Using LLM API**: Use LLMs (via OpenAI API, LangChain, or Ollama) to translate the natural language query into a corresponding SQL query.
3. **Execute the SQL Query**: Connect to a PostgreSQL database and run the generated SQL query.
4. **Display Results**: Display the results in a table format and provide options to visualize the results using various charts.
5. **Chart Options**: Include options to visualize the results as a line chart, bar chart, or pie chart.

**Application Flow:**
1. **User Input**: User enters a natural language query in a text box.
2. **SQL Generation**: Use one of the LLM APIs to convert the natural language query into a valid SQL query.
3. **SQL Execution**: Run the SQL query on a PostgreSQL database and retrieve results.
4. **Display and Visualization**: Show the results in a table and provide chart options.
5. **Schema Awareness**: Display the database schema and allow the user to see table structures to enhance the prompt generation.

### Requirements:
- **Use `streamlit` for the frontend**.
- **Choose any LLM Backend**: Use either `OpenAI API`, `langchain`, or `llama-index` to handle natural language to SQL conversion.
- **Database**: Use a PostgreSQL database with a sample schema provided or a public dataset of your choice.
- **Object-Oriented Programming**: Structure the application using classes and modules to follow object-oriented principles.
- **Chart Integration**: Use Streamlit's in-built `line_chart`, `bar_chart`, or other visualization options.

### Instructions:
1. **Setup Environment:**
   - Install required libraries:
     ```bash
     pip install streamlit psycopg2 pandas requests langchain llama-index openai ollama python-dotenv
     ```
   - Use Docker to set up a PostgreSQL database or connect to a locally running PostgreSQL instance.
   
2. **Application Structure:**
   - Implement an object-oriented design using classes and modules.
   - Suggested module structure:
     ```
     ├── app.py                    # Main Streamlit app
     ├── llm_integration.py        # LLM API integration classes/functions
     ├── query_executor.py         # Database connection and query execution
     ├── schema_manager.py         # Schema management (optional)
     ├── utils.py                  # Helper functions
     ├── requirements.txt          # List of dependencies
     └── .env                      # Environment variables (for API keys, DB credentials)
     ```

3. **Features to Implement:**
   1. **User Input**: Use Streamlit to create a text box for user input.
   2. **LLM Integration**:
      - Create a `LLMQueryGenerator` class to abstract different LLM backends (OpenAI, LangChain, Ollama).
      - Use methods like `generate_sql_from_nl(natural_language_query)` to convert natural language to SQL.
   3. **Database Interaction**:
      - Create a `DatabaseExecutor` class to handle database connections and run SQL queries.
      - Use `run_query(sql_query)` method to execute and fetch results.
   4. **Visualization Options**:
      - Create a dropdown menu for visualization options (`line chart`, `bar chart`, `pie chart`).
   5. **Code Structure and Documentation**:
      - Use classes and methods with clear docstrings and comments.
      - Follow best practices for code modularity and reusability.

4. **Sample Database Schema:**
   - Include a sample schema with a few tables (e.g., `customers`, `orders`, `products`) or use a public dataset like the `Chinook` sample database.

5. **Submission:**
   - Submit your code via GitHub or as a zip file.
   - Include instructions on how to set up the environment and run the application.
   - Make sure to include a `README.md` file that outlines the application structure and how to use it.

### Evaluation Criteria:
1. **Code Structure**: Use of object-oriented programming principles and clear modularization.
2. **Integration with LLMs**: Effective use of one or more LLM APIs (`OpenAI`, `LangChain`, or `Ollama`) to generate SQL from natural language.
3. **Functionality**: Completeness of the application, including SQL generation, execution, and visualization.
4. **Error Handling**: Proper error handling for SQL errors, invalid inputs, and API communication.
5. **Documentation**: Clear documentation of classes, functions, and the overall workflow.
6. **UI/UX**: Usability and interactivity of the Streamlit interface.

---

### Additional Challenge (Optional):
1. **LLM Schema Awareness**: Include schema-awareness in your LLM prompt. Modify the LLM prompt to include the current database schema so that the generated SQL queries are more accurate.
2. **Extensibility**: Allow switching between multiple LLM providers (OpenAI, Ollama, etc.) using a dropdown in the Streamlit UI.

This assignment should test the developer's ability to work with modern LLM tools and build a real-world GenAI application using structured data. Let me know if you need any modifications or additional details!
