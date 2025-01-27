#Retaurant Name Generator

## About
This project uses the Langchain library to get 
restaurant name suggestions based in cuisine and
then gets suggestions for menu items.

## Dependencies

### Python packages
Install the python packages from requirements.txt
`pip install -r requirements.txt`

### .env file
1. Create a .env folder in `src/` directory.
2. Add a variable called `OPENAI_API_KEY` and add the actual key there:
`OPENAI_API_KEY=sk-<some alphanumeric string here>`

## Run
Run it via streamlit

`streamlit run src/main.py`