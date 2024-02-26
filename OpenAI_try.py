import os
from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents.agent_types import AgentType
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import OpenAI
os.environ['OPENAI_API_KEY']=""
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
database="atliq_tshirts"
username="postgres"
password="postgres"
host="localhost"
port='5432'
db_uri=f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
db = SQLDatabase.from_uri(db_uri)
llm=OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model_name='gpt-3.5-turbo')
toolkit= SQLDatabaseToolkit(db=db , llm=OpenAI(temperature=0))
db_agent=create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

#db_agent.run("how many t-shirts do we have left for nike in xs size  and white color?")
db_agent.run("if we have to sell all the levis t-shirts today with discount applied how much rrevenue our store will generate?")
