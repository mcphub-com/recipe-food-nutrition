import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/spoonacular/api/recipe-food-nutrition'

mcp = FastMCP('recipe-food-nutrition')

@mcp.tool()
def search_recipes(query: Annotated[str, Field(description='The recipe search query.')],
                   cuisine: Annotated[Union[str, None], Field(description='The cuisine(s) of the recipes. One or more (comma separated) of the following: african, chinese, japanese, korean, vietnamese, thai, indian, british, irish, french, italian, mexican, spanish, middle eastern, jewish, american, cajun, southern, greek, german, nordic, eastern european, caribbean, or latin american.')] = None,
                   excludeCuisine: Annotated[Union[str, None], Field(description="The cuisine(s) the recipes must not match. One or more, comma separated (will be interpreted as 'AND'). See a full list of supported cuisines.")] = None,
                   diet: Annotated[Union[str, None], Field(description='The diet to which the recipes must be compliant. Possible values are: pescetarian, lacto vegetarian, ovo vegetarian, vegan, paleo, primal, and vegetarian.')] = None,
                   intolerances: Annotated[Union[str, None], Field(description='A comma-separated list of intolerances. All found recipes must not have ingredients that could cause problems for people with one of the given tolerances. Possible values are: dairy, egg, gluten, peanut, sesame, seafood, shellfish, soy, sulfite, tree nut, and wheat.')] = None,
                   equipment: Annotated[Union[str, None], Field(description='The equipment required. Multiple values will be interpreted as \'or\'. For example, value could be \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"blender, frying pan, bowl\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"')] = None,
                   includeIngredients: Annotated[Union[str, None], Field(description='A comma-separated list of ingredients that should/must be contained in the recipe.')] = None,
                   excludeIngredients: Annotated[Union[str, None], Field(description='An comma-separated list of ingredients that must not be contained in the recipes.')] = None,
                   type: Annotated[Union[str, None], Field(description='The type of the recipes. One of the following: main course, side dish, dessert, appetizer, salad, bread, breakfast, soup, beverage, sauce, or drink.')] = None,
                   instructionsRequired: Annotated[Union[bool, None], Field(description='Whether the recipes must have instructions.')] = None,
                   fillIngredients: Annotated[Union[bool, None], Field(description='Add information about the used and missing ingredients in each recipe.')] = None,
                   addRecipeInformation: Annotated[Union[bool, None], Field(description='If set to true, you get more information about the recipes returned. This saves the calls to get recipe information.')] = None,
                   addRecipeInstructions: Annotated[Union[bool, None], Field(description='If set to true, you get analyzed instructions for each recipe returned.')] = None,
                   addRecipeNutrition: Annotated[Union[bool, None], Field(description='If set to true, you get nutritional information about each recipes returned.')] = None,
                   author: Annotated[Union[str, None], Field(description='The username of the recipe author.')] = None,
                   tags: Annotated[Union[str, None], Field(description='User defined tags that have to match. The author param has to be set.')] = None,
                   recipeBoxId: Annotated[Union[int, float, None], Field(description='The id of the recipe box to which the search should be limited to. Default: 0')] = None,
                   titleMatch: Annotated[Union[str, None], Field(description='A string that the recipes must contain in their titles.')] = None,
                   maxReadyTime: Annotated[Union[int, float, None], Field(description='The maximum time in minutes it should take to prepare and cook the recipe. Default: 45')] = None,
                   ignorePantry: Annotated[Union[bool, None], Field(description='Whether to ignore typical pantry items, such as water, salt, flour, etc.')] = None,
                   sort: Annotated[Union[str, None], Field(description='The strategy to sort recipes by. See the full list of supported sorting options.')] = None,
                   sortDirection: Annotated[Union[str, None], Field(description="The direction in which to sort. Must be either 'asc' (ascending) or 'desc' (descending).")] = None,
                   minCarbs: Annotated[Union[int, float, None], Field(description='The minimum number of grams of carbohydrates the recipe must have. Default: 0')] = None,
                   maxCarbs: Annotated[Union[int, float, None], Field(description='The maximum number of grams of carbohydrates the recipe can have. Default: 0')] = None,
                   minProtein: Annotated[Union[int, float, None], Field(description='The minimum number of grams of protein the recipe must have. Default: 0')] = None,
                   maxProtein: Annotated[Union[int, float, None], Field(description='The maximum number of grams of protein the recipe can have. Default: 0')] = None,
                   minCalories: Annotated[Union[int, float, None], Field(description='The minimum number of calories the recipe must have. Default: 0')] = None,
                   maxCalories: Annotated[Union[int, float, None], Field(description='The maximum number of calories the recipe can have. Default: 0')] = None,
                   minFat: Annotated[Union[int, float, None], Field(description='The minimum number of grams of fat the recipe must have. Default: 0')] = None,
                   maxFat: Annotated[Union[int, float, None], Field(description='The maximum number of grams of fat the recipe can have. Default: 0')] = None,
                   minAlcohol: Annotated[Union[int, float, None], Field(description='The minimum number of grams of alcohol the recipe must have. Default: 0')] = None,
                   maxAlcohol: Annotated[Union[int, float, None], Field(description='The maximum number of grams of alcohol the recipe can have. Default: 0')] = None,
                   minCaffeine: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of caffeine the recipe must have. Default: 0')] = None,
                   maxCaffeine: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of caffeine the recipe can have. Default: 0')] = None,
                   minCopper: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of copper the recipe must have. Default: 0')] = None,
                   maxCopper: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of copper the recipe can have. Default: 0')] = None,
                   minCalcium: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of calcium the recipe must have. Default: 0')] = None,
                   maxCalcium: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of calcium the recipe can have. Default: 0')] = None,
                   minCholine: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of choline the recipe must have. Default: 0')] = None,
                   maxCholine: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of choline the recipe can have. Default: 0')] = None,
                   minCholesterol: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of cholesterol the recipe must have. Default: 0')] = None,
                   maxCholesterol: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of cholesterol the recipe can have. Default: 0')] = None,
                   minFluoride: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of fluoride the recipe must have. Default: 0')] = None,
                   maxFluoride: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of fluoride the recipe can have. Default: 0')] = None,
                   minSaturatedFat: Annotated[Union[int, float, None], Field(description='The minimum number of grams of saturated fat the recipe must have. Default: 0')] = None,
                   maxSaturatedFat: Annotated[Union[int, float, None], Field(description='The maximum number of grams of saturated fat the recipe can have. Default: 0')] = None,
                   minVitaminA: Annotated[Union[int, float, None], Field(description='The minimum number of IU of Vitamin A the recipe must have. Default: 0')] = None,
                   maxVitaminA: Annotated[Union[int, float, None], Field(description='The maximum number of IU of Vitamin A the recipe can have. Default: 0')] = None,
                   minVitaminC: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of Vitamin C the recipe must have. Default: 0')] = None,
                   maxVitaminC: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of Vitamin C the recipe can have. Default: 0')] = None,
                   minVitaminD: Annotated[Union[int, float, None], Field(description='The minimum number of micrograms of Vitamin D the recipe must have. Default: 0')] = None,
                   maxVitaminD: Annotated[Union[int, float, None], Field(description='The maximum number of micrograms of Vitamin D the recipe can have. Default: 0')] = None,
                   minVitaminE: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of Vitamin E the recipe must have. Default: 0')] = None,
                   maxVitaminE: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of Vitamin E the recipe can have. Default: 0')] = None,
                   minVitaminK: Annotated[Union[int, float, None], Field(description='The minimum number of micrograms of Vitamin K the recipe must have. Default: 0')] = None,
                   maxVitaminK: Annotated[Union[int, float, None], Field(description='The maximum number of micrograms of Vitamin K the recipe can have. Default: 0')] = None,
                   minVitaminB1: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of Vitamin B1 the recipe must have. Default: 0')] = None,
                   maxVitaminB1: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of Vitamin B1 the recipe can have. Default: 0')] = None,
                   minVitaminB2: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of Vitamin B2 the recipe must have. Default: 0')] = None,
                   maxVitaminB2: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of Vitamin B2 the recipe can have. Default: 0')] = None,
                   minVitaminB5: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of Vitamin B5 the recipe must have. Default: 0')] = None,
                   maxVitaminB5: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of Vitamin B5 the recipe can have. Default: 0')] = None,
                   minVitaminB3: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of Vitamin B3 the recipe must have. Default: 0')] = None,
                   maxVitaminB3: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of Vitamin B3 the recipe can have. Default: 0')] = None,
                   minVitaminB6: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of Vitamin B6 the recipe must have. Default: 0')] = None,
                   maxVitaminB6: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of Vitamin B6 the recipe can have. Default: 0')] = None,
                   minVitaminB12: Annotated[Union[int, float, None], Field(description='The minimum number of micrograms of Vitamin B12 the recipe must have. Default: 0')] = None,
                   maxVitaminB12: Annotated[Union[int, float, None], Field(description='The maximum number of micrograms of Vitamin B12 the recipe can have. Default: 0')] = None,
                   minFiber: Annotated[Union[int, float, None], Field(description='The minimum number of grams of fiber the recipe must have. Default: 0')] = None,
                   maxFiber: Annotated[Union[int, float, None], Field(description='The maximum number of grams of fiber the recipe can have. Default: 0')] = None,
                   minFolate: Annotated[Union[int, float, None], Field(description='The minimum number of micrograms of folate the recipe must have. Default: 0')] = None,
                   maxFolate: Annotated[Union[int, float, None], Field(description='The maximum number of micrograms of folate the recipe can have. Default: 0')] = None,
                   minFolicAcid: Annotated[Union[int, float, None], Field(description='The minimum number of micrograms of folic acid the recipe must have. Default: 0')] = None,
                   maxFolicAcid: Annotated[Union[int, float, None], Field(description='The maximum number of micrograms of folic acid the recipe can have. Default: 0')] = None,
                   minIodine: Annotated[Union[int, float, None], Field(description='The minimum number of micrograms of iodine the recipe must have. Default: 0')] = None,
                   maxIodine: Annotated[Union[int, float, None], Field(description='The maximum number of micrograms of iodine the recipe can have. Default: 0')] = None,
                   minIron: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of iron the recipe must have. Default: 0')] = None,
                   maxIron: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of iron the recipe can have. Default: 0')] = None,
                   minMagnesium: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of magnesium the recipe must have. Default: 0')] = None,
                   maxMagnesium: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of magnesium the recipe can have. Default: 0')] = None,
                   minManganese: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of manganese the recipe must have. Default: 0')] = None,
                   maxManganese: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of manganese the recipe can have. Default: 0')] = None,
                   minPhosphorus: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of phosphorus the recipe must have. Default: 0')] = None,
                   maxPhosphorus: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of phosphorus the recipe can have. Default: 0')] = None,
                   minPotassium: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of potassium the recipe must have. Default: 0')] = None,
                   maxPotassium: Annotated[Union[int, float, None], Field(description='The maxnimum number of milligrams of potassium the recipe can have. Default: 0')] = None,
                   minSelenium: Annotated[Union[int, float, None], Field(description='The minimum number of micrograms of selenium the recipe must have. Default: 0')] = None,
                   maxSelenium: Annotated[Union[int, float, None], Field(description='The maximum number of micrograms of selenium the recipe can have. Default: 0')] = None,
                   minSodium: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of sodium the recipe must have. Default: 0')] = None,
                   maxSodium: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of sodium the recipe can have. Default: 0')] = None,
                   minSugar: Annotated[Union[int, float, None], Field(description='The minimum number of grams of sugar the recipe must have. Default: 0')] = None,
                   maxSugar: Annotated[Union[int, float, None], Field(description='The maximum number of grams of sugar the recipe can have. Default: 0')] = None,
                   minZinc: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of zinc the recipe must have. Default: 0')] = None,
                   maxZinc: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of zinc the recipe can have. Default: 0')] = None,
                   offset: Annotated[Union[int, float, None], Field(description='The number of results to skip (between 0 and 900). Default: 0')] = None,
                   number: Annotated[Union[int, float, None], Field(description='The number of results to return (between 1 and 100). Default: 10')] = None,
                   ranking: Annotated[Union[int, float, None], Field(description='Whether to minimize missing ingredients (0), maximize used ingredients (1) first, or rank recipes by relevance (2). Default: 0')] = None) -> dict: 
    '''Search through thousands of recipes using advanced filtering and ranking. NOTE: Since this method combines searching by query, by ingredients, and by nutrients into one endpoint, each request counts as 3 requests.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'cuisine': cuisine,
        'excludeCuisine': excludeCuisine,
        'diet': diet,
        'intolerances': intolerances,
        'equipment': equipment,
        'includeIngredients': includeIngredients,
        'excludeIngredients': excludeIngredients,
        'type': type,
        'instructionsRequired': instructionsRequired,
        'fillIngredients': fillIngredients,
        'addRecipeInformation': addRecipeInformation,
        'addRecipeInstructions': addRecipeInstructions,
        'addRecipeNutrition': addRecipeNutrition,
        'author': author,
        'tags': tags,
        'recipeBoxId': recipeBoxId,
        'titleMatch': titleMatch,
        'maxReadyTime': maxReadyTime,
        'ignorePantry': ignorePantry,
        'sort': sort,
        'sortDirection': sortDirection,
        'minCarbs': minCarbs,
        'maxCarbs': maxCarbs,
        'minProtein': minProtein,
        'maxProtein': maxProtein,
        'minCalories': minCalories,
        'maxCalories': maxCalories,
        'minFat': minFat,
        'maxFat': maxFat,
        'minAlcohol': minAlcohol,
        'maxAlcohol': maxAlcohol,
        'minCaffeine': minCaffeine,
        'maxCaffeine': maxCaffeine,
        'minCopper': minCopper,
        'maxCopper': maxCopper,
        'minCalcium': minCalcium,
        'maxCalcium': maxCalcium,
        'minCholine': minCholine,
        'maxCholine': maxCholine,
        'minCholesterol': minCholesterol,
        'maxCholesterol': maxCholesterol,
        'minFluoride': minFluoride,
        'maxFluoride': maxFluoride,
        'minSaturatedFat': minSaturatedFat,
        'maxSaturatedFat': maxSaturatedFat,
        'minVitaminA': minVitaminA,
        'maxVitaminA': maxVitaminA,
        'minVitaminC': minVitaminC,
        'maxVitaminC': maxVitaminC,
        'minVitaminD': minVitaminD,
        'maxVitaminD': maxVitaminD,
        'minVitaminE': minVitaminE,
        'maxVitaminE': maxVitaminE,
        'minVitaminK': minVitaminK,
        'maxVitaminK': maxVitaminK,
        'minVitaminB1': minVitaminB1,
        'maxVitaminB1': maxVitaminB1,
        'minVitaminB2': minVitaminB2,
        'maxVitaminB2': maxVitaminB2,
        'minVitaminB5': minVitaminB5,
        'maxVitaminB5': maxVitaminB5,
        'minVitaminB3': minVitaminB3,
        'maxVitaminB3': maxVitaminB3,
        'minVitaminB6': minVitaminB6,
        'maxVitaminB6': maxVitaminB6,
        'minVitaminB12': minVitaminB12,
        'maxVitaminB12': maxVitaminB12,
        'minFiber': minFiber,
        'maxFiber': maxFiber,
        'minFolate': minFolate,
        'maxFolate': maxFolate,
        'minFolicAcid': minFolicAcid,
        'maxFolicAcid': maxFolicAcid,
        'minIodine': minIodine,
        'maxIodine': maxIodine,
        'minIron': minIron,
        'maxIron': maxIron,
        'minMagnesium': minMagnesium,
        'maxMagnesium': maxMagnesium,
        'minManganese': minManganese,
        'maxManganese': maxManganese,
        'minPhosphorus': minPhosphorus,
        'maxPhosphorus': maxPhosphorus,
        'minPotassium': minPotassium,
        'maxPotassium': maxPotassium,
        'minSelenium': minSelenium,
        'maxSelenium': maxSelenium,
        'minSodium': minSodium,
        'maxSodium': maxSodium,
        'minSugar': minSugar,
        'maxSugar': maxSugar,
        'minZinc': minZinc,
        'maxZinc': maxZinc,
        'offset': offset,
        'number': number,
        'ranking': ranking,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_recipes_complex(limitLicense: Annotated[bool, Field(description='Whether the recipes should have an open license that allows for displaying with proper attribution.')],
                           offset: Annotated[Union[int, float], Field(description='The number of results to skip (between 0 and 900). Default: 0')],
                           number: Annotated[Union[int, float], Field(description='The number of results to return (between 1 and 100). Default: 10')],
                           minIron: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of iron the recipe must have. Default: 0')] = None,
                           minCalcium: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of calcium the recipe must have. Default: 0')] = None,
                           maxVitaminB2: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of Vitamin B2 the recipe can have. Default: 1000')] = None,
                           maxMagnesium: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of magnesium the recipe can have. Default: 1000')] = None,
                           minPotassium: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of potassium the recipe must have. Default: 0')] = None,
                           maxVitaminB6: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of Vitamin B6 the recipe can have. Default: 1000')] = None,
                           intolerances: Annotated[Union[str, None], Field(description='A comma-separated list of intolerances. All found recipes must not have ingredients that could cause problems for people with one of the given tolerances. Possible values are: dairy, egg, gluten, peanut, sesame, seafood, shellfish, soy, sulfite, tree nut, and wheat.')] = None,
                           maxVitaminB5: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of Vitamin B5 the recipe can have. Default: 1000')] = None,
                           minFolicAcid: Annotated[Union[int, float, None], Field(description='The minimum number of micrograms of folic acid the recipe must have. Default: 0')] = None,
                           minVitaminA: Annotated[Union[int, float, None], Field(description='The minimum number of IU of Vitamin A the recipe must have. Default: 0')] = None,
                           maxSodium: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of sodium the recipe can have. Default: 1000')] = None,
                           maxSugar: Annotated[Union[int, float, None], Field(description='The maximum number of grams of sugar the recipe can have. Default: 1000')] = None,
                           diet: Annotated[Union[str, None], Field(description='The diet to which the recipes must be compliant. Possible values are: pescetarian, lacto vegetarian, ovo vegetarian, vegan, paleo, primal, and vegetarian.')] = None,
                           maxVitaminA: Annotated[Union[int, float, None], Field(description='The maximum number of IU of Vitamin A the recipe can have. Default: 5000')] = None,
                           maxFluoride: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of fluoride the recipe can have. Default: 1000')] = None,
                           minFluoride: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of fluoride the recipe must have. Default: 0')] = None,
                           instructionsRequired: Annotated[Union[bool, None], Field(description='Whether the recipes must have instructions.')] = None,
                           minVitaminB1: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of Vitamin B1 the recipe must have. Default: 0')] = None,
                           minCholine: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of choline the recipe must have. Default: 0')] = None,
                           ranking: Annotated[Union[int, float, None], Field(description='Whether to minimize missing ingredients (0), maximize used ingredients (1) first, or rank recipes by relevance (2). Default: 2')] = None,
                           minFat: Annotated[Union[int, float, None], Field(description='The minimum number of grams of fat the recipe must have. Default: 5')] = None,
                           maxVitaminB1: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of Vitamin B1 the recipe can have. Default: 1000')] = None,
                           addRecipeInformation: Annotated[Union[bool, None], Field(description='If set to true, you get more information about the recipes returned. This saves the calls to get recipe information.')] = None,
                           minVitaminB12: Annotated[Union[int, float, None], Field(description='The minimum number of micrograms of Vitamin B12 the recipe must have. Default: 0')] = None,
                           maxSelenium: Annotated[Union[int, float, None], Field(description='The maximum number of micrograms of selenium the recipe can have. Default: 1000')] = None,
                           minZinc: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of zinc the recipe must have. Default: 0')] = None,
                           minFolate: Annotated[Union[int, float, None], Field(description='The minimum number of micrograms of folate the recipe must have. Default: 0')] = None,
                           maxManganese: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of manganese the recipe can have. Default: 1000')] = None,
                           maxVitaminB12: Annotated[Union[int, float, None], Field(description='The maximum number of micrograms of Vitamin B12 the recipe can have. Default: 1000')] = None,
                           maxPotassium: Annotated[Union[int, float, None], Field(description='The maxnimum number of milligrams of potassium the recipe can have. Default: 1000')] = None,
                           maxIron: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of iron the recipe can have. Default: 1000')] = None,
                           minSelenium: Annotated[Union[int, float, None], Field(description='The minimum number of micrograms of selenium the recipe must have. Default: 0')] = None,
                           minVitaminK: Annotated[Union[int, float, None], Field(description='The minimum number of micrograms of Vitamin K the recipe must have. Default: 0')] = None,
                           maxFiber: Annotated[Union[int, float, None], Field(description='The maximum number of grams of fiber the recipe can have. Default: 1000')] = None,
                           fillIngredients: Annotated[Union[bool, None], Field(description='Add information about the used and missing ingredients in each recipe.')] = None,
                           minSodium: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of sodium the recipe must have. Default: 0')] = None,
                           maxCopper: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of copper the recipe can have. Default: 1000')] = None,
                           minCalories: Annotated[Union[int, float, None], Field(description='The minimum number of calories the recipe must have. Default: 150')] = None,
                           maxCholine: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of choline the recipe can have. Default: 1000')] = None,
                           minCholesterol: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of cholesterol the recipe must have. Default: 0')] = None,
                           maxVitaminE: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of Vitamin E the recipe can have. Default: 1000')] = None,
                           minProtein: Annotated[Union[int, float, None], Field(description='The minimum number of grams of protein the recipe must have. Default: 5')] = None,
                           minVitaminB3: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of Vitamin B3 the recipe must have. Default: 0')] = None,
                           minVitaminB6: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of Vitamin B6 the recipe must have. Default: 0')] = None,
                           maxIodine: Annotated[Union[int, float, None], Field(description='The maximum number of micrograms of iodine the recipe can have. Default: 1000')] = None,
                           excludeIngredients: Annotated[Union[str, None], Field(description='An comma-separated list of ingredients that must not be contained in the recipes.')] = None,
                           maxProtein: Annotated[Union[int, float, None], Field(description='The maximum number of grams of protein the recipe can have. Default: 100')] = None,
                           minMagnesium: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of magnesium the recipe must have. Default: 0')] = None,
                           minCarbs: Annotated[Union[int, float, None], Field(description='The minimum number of grams of carbohydrates the recipe must have. Default: 5')] = None,
                           cuisine: Annotated[Union[str, None], Field(description='The cuisine(s) of the recipes. One or more (comma separated) of the following: african, chinese, japanese, korean, vietnamese, thai, indian, british, irish, french, italian, mexican, spanish, middle eastern, jewish, american, cajun, southern, greek, german, nordic, eastern european, caribbean, or latin american.')] = None,
                           maxCaffeine: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of caffeine the recipe can have. Default: 1000')] = None,
                           maxSaturatedFat: Annotated[Union[int, float, None], Field(description='The maximum number of grams of saturated fat the recipe can have. Default: 50')] = None,
                           maxVitaminK: Annotated[Union[int, float, None], Field(description='The maximum number of micrograms of Vitamin K the recipe can have. Default: 1000')] = None,
                           author: Annotated[Union[str, None], Field(description='The username of the recipe author.')] = None,
                           minAlcohol: Annotated[Union[int, float, None], Field(description='The minimum number of grams of alcohol the recipe must have. Default: 0')] = None,
                           minIodine: Annotated[Union[int, float, None], Field(description='The minimum number of micrograms of iodine the recipe must have. Default: 0')] = None,
                           query: Annotated[Union[str, None], Field(description='The recipe search query.')] = None,
                           minSaturatedFat: Annotated[Union[int, float, None], Field(description='The minimum number of grams of saturated fat the recipe must have. Default: 0')] = None,
                           includeIngredients: Annotated[Union[str, None], Field(description='A comma-separated list of ingredients that should/must be contained in the recipe.')] = None,
                           minVitaminE: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of Vitamin E the recipe must have. Default: 0')] = None,
                           maxCalcium: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of calcium the recipe can have. Default: 1000')] = None,
                           minFiber: Annotated[Union[int, float, None], Field(description='The minimum number of grams of fiber the recipe must have. Default: 0')] = None,
                           minVitaminC: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of Vitamin C the recipe must have. Default: 0')] = None,
                           maxZinc: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of zinc the recipe can have. Default: 1000')] = None,
                           maxCalories: Annotated[Union[int, float, None], Field(description='The maximum number of calories the recipe can have. Default: 1500')] = None,
                           maxAlcohol: Annotated[Union[int, float, None], Field(description='The maximum number of grams of alcohol the recipe can have. Default: 1000')] = None,
                           minPhosphorus: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of phosphorus the recipe must have. Default: 0')] = None,
                           minVitaminD: Annotated[Union[int, float, None], Field(description='The minimum number of micrograms of Vitamin D the recipe must have. Default: 0')] = None,
                           minVitaminB2: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of Vitamin B2 the recipe must have. Default: 0')] = None,
                           minSugar: Annotated[Union[int, float, None], Field(description='The minimum number of grams of sugar the recipe must have. Default: 0')] = None,
                           maxFolate: Annotated[Union[int, float, None], Field(description='The maximum number of micrograms of folate the recipe can have. Default: 1000')] = None,
                           type: Annotated[Union[str, None], Field(description='The type of the recipes. One of the following: main course, side dish, dessert, appetizer, salad, bread, breakfast, soup, beverage, sauce, or drink.')] = None,
                           maxCholesterol: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of cholesterol the recipe can have. Default: 1000')] = None,
                           maxVitaminB3: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of Vitamin B3 the recipe can have. Default: 1000')] = None,
                           minCaffeine: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of caffeine the recipe must have. Default: 0')] = None,
                           minVitaminB5: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of Vitamin B5 the recipe must have. Default: 0')] = None,
                           maxFolicAcid: Annotated[Union[int, float, None], Field(description='The maximum number of micrograms of folic acid the recipe can have. Default: 1000')] = None,
                           maxCarbs: Annotated[Union[int, float, None], Field(description='The maximum number of grams of carbohydrates the recipe can have. Default: 100')] = None,
                           maxVitaminD: Annotated[Union[int, float, None], Field(description='The maximum number of micrograms of Vitamin D the recipe can have. Default: 1000')] = None,
                           equipment: Annotated[Union[str, None], Field(description='The equipment required. Multiple values will be interpreted as \'or\'. For example, value could be "blender, frying pan, bowl"')] = None,
                           maxFat: Annotated[Union[int, float, None], Field(description='The maximum number of grams of fat the recipe can have. Default: 100')] = None,
                           minCopper: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of copper the recipe must have. Default: 0')] = None,
                           maxVitaminC: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of Vitamin C the recipe can have. Default: 1000')] = None,
                           maxPhosphorus: Annotated[Union[int, float, None], Field(description='The maximum number of milligrams of phosphorus the recipe can have. Default: 1000')] = None,
                           minManganese: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of manganese the recipe must have. Default: 0')] = None) -> dict: 
    '''Search through hundreds of thousands of recipes using advanced filtering and ranking. NOTE: Since this method combines three other functionalities, each request counts as 3 requests.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/searchComplex'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limitLicense': limitLicense,
        'offset': offset,
        'number': number,
        'minIron': minIron,
        'minCalcium': minCalcium,
        'maxVitaminB2': maxVitaminB2,
        'maxMagnesium': maxMagnesium,
        'minPotassium': minPotassium,
        'maxVitaminB6': maxVitaminB6,
        'intolerances': intolerances,
        'maxVitaminB5': maxVitaminB5,
        'minFolicAcid': minFolicAcid,
        'minVitaminA': minVitaminA,
        'maxSodium': maxSodium,
        'maxSugar': maxSugar,
        'diet': diet,
        'maxVitaminA': maxVitaminA,
        'maxFluoride': maxFluoride,
        'minFluoride': minFluoride,
        'instructionsRequired': instructionsRequired,
        'minVitaminB1': minVitaminB1,
        'minCholine': minCholine,
        'ranking': ranking,
        'minFat': minFat,
        'maxVitaminB1': maxVitaminB1,
        'addRecipeInformation': addRecipeInformation,
        'minVitaminB12': minVitaminB12,
        'maxSelenium': maxSelenium,
        'minZinc': minZinc,
        'minFolate': minFolate,
        'maxManganese': maxManganese,
        'maxVitaminB12': maxVitaminB12,
        'maxPotassium': maxPotassium,
        'maxIron': maxIron,
        'minSelenium': minSelenium,
        'minVitaminK': minVitaminK,
        'maxFiber': maxFiber,
        'fillIngredients': fillIngredients,
        'minSodium': minSodium,
        'maxCopper': maxCopper,
        'minCalories': minCalories,
        'maxCholine': maxCholine,
        'minCholesterol': minCholesterol,
        'maxVitaminE': maxVitaminE,
        'minProtein': minProtein,
        'minVitaminB3': minVitaminB3,
        'minVitaminB6': minVitaminB6,
        'maxIodine': maxIodine,
        'excludeIngredients': excludeIngredients,
        'maxProtein': maxProtein,
        'minMagnesium': minMagnesium,
        'minCarbs': minCarbs,
        'cuisine': cuisine,
        'maxCaffeine': maxCaffeine,
        'maxSaturatedFat': maxSaturatedFat,
        'maxVitaminK': maxVitaminK,
        'author': author,
        'minAlcohol': minAlcohol,
        'minIodine': minIodine,
        'query': query,
        'minSaturatedFat': minSaturatedFat,
        'includeIngredients': includeIngredients,
        'minVitaminE': minVitaminE,
        'maxCalcium': maxCalcium,
        'minFiber': minFiber,
        'minVitaminC': minVitaminC,
        'maxZinc': maxZinc,
        'maxCalories': maxCalories,
        'maxAlcohol': maxAlcohol,
        'minPhosphorus': minPhosphorus,
        'minVitaminD': minVitaminD,
        'minVitaminB2': minVitaminB2,
        'minSugar': minSugar,
        'maxFolate': maxFolate,
        'type': type,
        'maxCholesterol': maxCholesterol,
        'maxVitaminB3': maxVitaminB3,
        'minCaffeine': minCaffeine,
        'minVitaminB5': minVitaminB5,
        'maxFolicAcid': maxFolicAcid,
        'maxCarbs': maxCarbs,
        'maxVitaminD': maxVitaminD,
        'equipment': equipment,
        'maxFat': maxFat,
        'minCopper': minCopper,
        'maxVitaminC': maxVitaminC,
        'maxPhosphorus': maxPhosphorus,
        'minManganese': minManganese,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_recipes_by_nutrients(minProtein: Annotated[Union[int, float, None], Field(description='The minimum number of protein in grams the recipe must have. Default: 0')] = None,
                                minVitaminC: Annotated[Union[int, float, None], Field(description='The minimum number of Vitamin C milligrams the recipe must have. Default: 0')] = None,
                                minSelenium: Annotated[Union[int, float, None], Field(description='The minimum number of selenium in grams the recipe must have. Default: 0')] = None,
                                random: Annotated[Union[bool, None], Field(description='If true, every request will give you a random set of recipes within the requested limits.')] = None,
                                maxFluoride: Annotated[Union[int, float, None], Field(description='The maximum number of fluoride in milligrams the recipe can have. Default: 50')] = None,
                                maxVitaminB5: Annotated[Union[int, float, None], Field(description='The maximum number of Vitamin B5 in milligrams the recipe can have. Default: 50')] = None,
                                maxVitaminB3: Annotated[Union[int, float, None], Field(description='The maximum number of Vitamin B3 in milligrams the recipe can have. Default: 50')] = None,
                                maxIodine: Annotated[Union[int, float, None], Field(description='The maximum number of iodine in grams the recipe must have. Default: 50')] = None,
                                minCarbs: Annotated[Union[int, float, None], Field(description='The minimum number of carbohydrates in grams the recipe must have. Default: 0')] = None,
                                maxCalories: Annotated[Union[int, float, None], Field(description='The maximum number of calories the recipe can have. Default: 250')] = None,
                                minAlcohol: Annotated[Union[int, float, None], Field(description='The minimum number of alcohol in grams the recipe must have. Default: 0')] = None,
                                maxCopper: Annotated[Union[int, float, None], Field(description='The maximum number of copper in milligrams the recipe must have. Default: 50')] = None,
                                maxCholine: Annotated[Union[int, float, None], Field(description='The maximum number of choline in milligrams the recipe can have. Default: 50')] = None,
                                maxVitaminB6: Annotated[Union[int, float, None], Field(description='The maximum number of Vitamin B6 in milligrams the recipe can have. Default: 50')] = None,
                                minIron: Annotated[Union[int, float, None], Field(description='The minimum number of iron in milligrams the recipe must have. Default: 0')] = None,
                                maxManganese: Annotated[Union[int, float, None], Field(description='The maximum number of manganese in milligrams the recipe can have. Default: 50')] = None,
                                minSodium: Annotated[Union[int, float, None], Field(description='The minimum number of sodium in milligrams the recipe must have. Default: 0')] = None,
                                minSugar: Annotated[Union[int, float, None], Field(description='The minimum number of sugar in grams the recipe must have. Default: 0')] = None,
                                maxFat: Annotated[Union[int, float, None], Field(description='The maximum number of fat in grams the recipe can have. Default: 20')] = None,
                                minCholine: Annotated[Union[int, float, None], Field(description='The minimum number of choline in milligrams the recipe must have. Default: 0')] = None,
                                maxVitaminC: Annotated[Union[int, float, None], Field(description='The maximum number of Vitamin C in milligrams the recipe can have. Default: 50')] = None,
                                maxVitaminB2: Annotated[Union[int, float, None], Field(description='The maximum number of Vitamin B2 in milligrams the recipe must have. Default: 50')] = None,
                                minVitaminB12: Annotated[Union[int, float, None], Field(description='The minimum number of Vitamin B12 in micrograms the recipe must have. Default: 0')] = None,
                                maxFolicAcid: Annotated[Union[int, float, None], Field(description='The maximum number of folic acid in grams the recipe must have. Default: 50')] = None,
                                minZinc: Annotated[Union[int, float, None], Field(description='The minimum number of zinc in milligrams the recipe must have. Default: 0')] = None,
                                offset: Annotated[Union[int, float, None], Field(description='The offset number for paging in the interval [0,990]. Default: 0')] = None,
                                maxProtein: Annotated[Union[int, float, None], Field(description='The maximum number of protein in grams the recipe can have. Default: 100')] = None,
                                minCalories: Annotated[Union[int, float, None], Field(description='The minimum number of calories the recipe must have. Default: 0')] = None,
                                minCaffeine: Annotated[Union[int, float, None], Field(description='The minimum number of milligrams of caffeine the recipe must have. Default: 0')] = None,
                                minVitaminD: Annotated[Union[int, float, None], Field(description='The minimum number of Vitamin D in micrograms the recipe must have. Default: 0')] = None,
                                maxVitaminE: Annotated[Union[int, float, None], Field(description='The maximum number of Vitamin E in milligrams the recipe must have. Default: 50')] = None,
                                minVitaminB2: Annotated[Union[int, float, None], Field(description='The minimum number of Vitamin B2 in milligrams the recipe must have. Default: 0')] = None,
                                minFiber: Annotated[Union[int, float, None], Field(description='The minimum number of fiber in grams the recipe must have. Default: 0')] = None,
                                minFolate: Annotated[Union[int, float, None], Field(description='The minimum number of folate in grams the recipe must have. Default: 0')] = None,
                                minManganese: Annotated[Union[int, float, None], Field(description='The minimum number of manganese in milligrams the recipe must have. Default: 0')] = None,
                                maxPotassium: Annotated[Union[int, float, None], Field(description='The maximum number of potassium in milligrams the recipe can have. Default: 50')] = None,
                                maxSugar: Annotated[Union[int, float, None], Field(description='The maximum number of sugar in grams the recipe must have. Default: 50')] = None,
                                maxCaffeine: Annotated[Union[int, float, None], Field(description='The maximum number of alcohol in grams the recipe must have. Default: 50')] = None,
                                maxCholesterol: Annotated[Union[int, float, None], Field(description='The maximum number of cholesterol in milligrams the recipe must have. Default: 50')] = None,
                                maxSaturatedFat: Annotated[Union[int, float, None], Field(description='The maximum number of saturated fat in grams the recipe must have. Default: 50')] = None,
                                minVitaminB3: Annotated[Union[int, float, None], Field(description='The minimum number of Vitamin B3 in milligrams the recipe must have. Default: 0')] = None,
                                maxFiber: Annotated[Union[int, float, None], Field(description='The maximum number of fiber in grams the recipe must have. Default: 50')] = None,
                                maxPhosphorus: Annotated[Union[int, float, None], Field(description='The maximum number of phosphorus in milligrams the recipe can have. Default: 50')] = None,
                                minPotassium: Annotated[Union[int, float, None], Field(description='The minimum number of potassium in milligrams the recipe must have. Default: 0')] = None,
                                maxSelenium: Annotated[Union[int, float, None], Field(description='The maximum number of selenium in grams the recipe must have. Default: 50')] = None,
                                maxCarbs: Annotated[Union[int, float, None], Field(description='The maximum number of carbohydrates in grams the recipe can have. Default: 100')] = None,
                                minCalcium: Annotated[Union[int, float, None], Field(description='The minimum number of calcium in milligrams the recipe must have. Default: 0')] = None,
                                minCholesterol: Annotated[Union[int, float, None], Field(description='The minimum number of cholesterol in milligrams the recipe must have. Default: 0')] = None,
                                minFluoride: Annotated[Union[int, float, None], Field(description='The minimum number of fluoride in milligrams the recipe must have. Default: 0')] = None,
                                maxVitaminD: Annotated[Union[int, float, None], Field(description='The maximum number of Vitamin D in micrograms the recipe must have. Default: 50')] = None,
                                maxVitaminB12: Annotated[Union[int, float, None], Field(description='The maximum number of Vitamin B12 in micrograms the recipe must have. Default: 50')] = None,
                                minIodine: Annotated[Union[int, float, None], Field(description='The minimum number of Iodine in grams the recipe must have. Default: 0')] = None,
                                maxZinc: Annotated[Union[int, float, None], Field(description='The maximum number of zinc in milligrams the recipe can have. Default: 50')] = None,
                                minSaturatedFat: Annotated[Union[int, float, None], Field(description='The minimum number of saturated fat in grams the recipe must have. Default: 0')] = None,
                                minVitaminB1: Annotated[Union[int, float, None], Field(description='The minimum number of Vitamin B1 in milligrams the recipe must have. Default: 0')] = None,
                                maxFolate: Annotated[Union[int, float, None], Field(description='The maximum number of folate in grams the recipe must have. Default: 50')] = None,
                                minFolicAcid: Annotated[Union[int, float, None], Field(description='The minimum number of folic acid in grams the recipe must have. Default: 0')] = None,
                                maxMagnesium: Annotated[Union[int, float, None], Field(description='The maximum number of magnesium in milligrams the recipe can have. Default: 50')] = None,
                                minVitaminK: Annotated[Union[int, float, None], Field(description='The minimum number of Vitamin K in micrograms the recipe must have. Default: 0')] = None,
                                maxSodium: Annotated[Union[int, float, None], Field(description='The maximum number of sodium in milligrams the recipe must have. Default: 50')] = None,
                                maxAlcohol: Annotated[Union[int, float, None], Field(description='The maximum number of alcohol in grams the recipe must have. Default: 50')] = None,
                                maxCalcium: Annotated[Union[int, float, None], Field(description='The maximum number of calcium in milligrams the recipe must have. Default: 50')] = None,
                                maxVitaminA: Annotated[Union[int, float, None], Field(description='The maximum number of Vitamin A in IU the recipe must have. Default: 50')] = None,
                                maxVitaminK: Annotated[Union[int, float, None], Field(description='The maximum number of Vitamin K in micrograms the recipe must have. Default: 50')] = None,
                                minVitaminB5: Annotated[Union[int, float, None], Field(description='The minimum number of Vitamin B5 in milligrams the recipe must have. Default: 0')] = None,
                                maxIron: Annotated[Union[int, float, None], Field(description='The maximum number of iron in milligrams the recipe can have. Default: 50')] = None,
                                minCopper: Annotated[Union[int, float, None], Field(description='The minimum number of copper in milligrams the recipe must have. Default: 0')] = None,
                                maxVitaminB1: Annotated[Union[int, float, None], Field(description='The maximum number of Vitamin B1 in milligrams the recipe must have. Default: 50')] = None,
                                number: Annotated[Union[int, float, None], Field(description='The number of expected results in the interval [1,10]. Default: 10')] = None,
                                minVitaminA: Annotated[Union[int, float, None], Field(description='The minimum number of Vitamin A in IU the recipe must have. Default: 0')] = None,
                                minPhosphorus: Annotated[Union[int, float, None], Field(description='The minimum number of phosphorus in milligrams the recipe must have. Default: 0')] = None,
                                minVitaminB6: Annotated[Union[int, float, None], Field(description='The minimum number of Vitamin B6 in milligrams the recipe must have. Default: 0')] = None,
                                minFat: Annotated[Union[int, float, None], Field(description='The minimum number of fat in grams the recipe must have. Default: 5')] = None,
                                minVitaminE: Annotated[Union[int, float, None], Field(description='The minimum number of Vitamin E in milligrams the recipe must have. Default: 0')] = None) -> dict: 
    '''Find a set of recipes that adhere to the given nutrient limits. All the found recipes will have macro nutrients within the calories, protein, fat, and carbohydrate limits.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByNutrients'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'minProtein': minProtein,
        'minVitaminC': minVitaminC,
        'minSelenium': minSelenium,
        'random': random,
        'maxFluoride': maxFluoride,
        'maxVitaminB5': maxVitaminB5,
        'maxVitaminB3': maxVitaminB3,
        'maxIodine': maxIodine,
        'minCarbs': minCarbs,
        'maxCalories': maxCalories,
        'minAlcohol': minAlcohol,
        'maxCopper': maxCopper,
        'maxCholine': maxCholine,
        'maxVitaminB6': maxVitaminB6,
        'minIron': minIron,
        'maxManganese': maxManganese,
        'minSodium': minSodium,
        'minSugar': minSugar,
        'maxFat': maxFat,
        'minCholine': minCholine,
        'maxVitaminC': maxVitaminC,
        'maxVitaminB2': maxVitaminB2,
        'minVitaminB12': minVitaminB12,
        'maxFolicAcid': maxFolicAcid,
        'minZinc': minZinc,
        'offset': offset,
        'maxProtein': maxProtein,
        'minCalories': minCalories,
        'minCaffeine': minCaffeine,
        'minVitaminD': minVitaminD,
        'maxVitaminE': maxVitaminE,
        'minVitaminB2': minVitaminB2,
        'minFiber': minFiber,
        'minFolate': minFolate,
        'minManganese': minManganese,
        'maxPotassium': maxPotassium,
        'maxSugar': maxSugar,
        'maxCaffeine': maxCaffeine,
        'maxCholesterol': maxCholesterol,
        'maxSaturatedFat': maxSaturatedFat,
        'minVitaminB3': minVitaminB3,
        'maxFiber': maxFiber,
        'maxPhosphorus': maxPhosphorus,
        'minPotassium': minPotassium,
        'maxSelenium': maxSelenium,
        'maxCarbs': maxCarbs,
        'minCalcium': minCalcium,
        'minCholesterol': minCholesterol,
        'minFluoride': minFluoride,
        'maxVitaminD': maxVitaminD,
        'maxVitaminB12': maxVitaminB12,
        'minIodine': minIodine,
        'maxZinc': maxZinc,
        'minSaturatedFat': minSaturatedFat,
        'minVitaminB1': minVitaminB1,
        'maxFolate': maxFolate,
        'minFolicAcid': minFolicAcid,
        'maxMagnesium': maxMagnesium,
        'minVitaminK': minVitaminK,
        'maxSodium': maxSodium,
        'maxAlcohol': maxAlcohol,
        'maxCalcium': maxCalcium,
        'maxVitaminA': maxVitaminA,
        'maxVitaminK': maxVitaminK,
        'minVitaminB5': minVitaminB5,
        'maxIron': maxIron,
        'minCopper': minCopper,
        'maxVitaminB1': maxVitaminB1,
        'number': number,
        'minVitaminA': minVitaminA,
        'minPhosphorus': minPhosphorus,
        'minVitaminB6': minVitaminB6,
        'minFat': minFat,
        'minVitaminE': minVitaminE,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_recipes_by_ingredients(ingredients: Annotated[str, Field(description='A comma-separated list of ingredients that the recipes should contain.')],
                                  number: Annotated[Union[int, float, None], Field(description='The maximal number of recipes to return (default = 5). Default: 5')] = None,
                                  ignorePantry: Annotated[Union[bool, None], Field(description='Whether to ignore pantry ingredients such as water, salt, flour etc..')] = None,
                                  ranking: Annotated[Union[int, float, None], Field(description='Whether to maximize used ingredients (1) or minimize missing ingredients (2) first. Default: 1')] = None) -> dict: 
    '''Find recipes that use as many of the given ingredients as possible and have as little as possible missing ingredients. This is a whats in your fridge API endpoint.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ingredients': ingredients,
        'number': number,
        'ignorePantry': ignorePantry,
        'ranking': ranking,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_recipe_information(includeNutrition: Annotated[Union[bool, None], Field(description='Include nutrition data to the recipe information. Nutrition data is per serving. If you want the nutrition data for the entire recipe, just multiply by the number of servings.')] = None) -> dict: 
    '''Get information about a recipe.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/479101/information'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'includeNutrition': includeNutrition,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_recipe_information_bulk(ids: Annotated[str, Field(description='A comma-separated list of recipe ids.')],
                                includeNutrition: Annotated[Union[bool, None], Field(description='Include nutrition data to the recipe information.')] = None) -> dict: 
    '''Get information about multiple recipes at once. That is equivalent of calling the Get Recipe Information endpoint multiple times but is faster. Note that each returned recipe counts as one request.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/informationBulk'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ids': ids,
        'includeNutrition': includeNutrition,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_similar_recipes() -> dict: 
    '''Find recipes which are similar to the given one.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/156992/similar'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_random_recipes(tags: Annotated[Union[str, None], Field(description='Tags that the random recipe(s) must adhere to.')] = None,
                       number: Annotated[Union[int, float, None], Field(description='The number of random recipes to be returned. Must be in interval [1,100]. NOTE: Each random recipe returned counts as one request. Default: 1')] = None) -> dict: 
    '''Find random (popular) recipes.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tags': tags,
        'number': number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def autocomplete_recipe_search(query: Annotated[str, Field(description='The query to be autocompleted.')],
                               number: Annotated[Union[int, float, None], Field(description='The number of results between [1,25]. Default: 10')] = None) -> dict: 
    '''Autocomplete a partial input to possible recipe names.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/autocomplete'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'number': number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def taste_by_id(normalize: Annotated[Union[bool, None], Field(description='Normalize to the strongest taste.')] = None) -> dict: 
    '''Get a recipe's taste. The tastes supported are sweet, salty, sour, bitter, savory, and fatty. These tastes are between 0 and 100 while the spiciness value is in scoville on an open scale of 0 and above. Every ingredient has each of these values and it is weighted by how much they contribute to the recipe. Spiciness is taking the weight of the spicy ingredient and multiplying it with its scoville amount. Of course, taste is also very personal and it depends on how it is prepared so all of the values should only give you an indication of how the dish tastes.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/69095/tasteWidget.json'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'normalize': normalize,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def equipment_by_id() -> dict: 
    '''Get a recipe's equipment list.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/1003464/equipmentWidget.json'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def price_breakdown_by_id() -> dict: 
    '''Get a recipe's price breakdown data.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/1003464/priceBreakdownWidget.json'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def ingredients_by_id() -> dict: 
    '''Get a recipe's ingredient list.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/1003464/ingredientWidget.json'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def nutrition_by_id() -> dict: 
    '''Get a recipe's nutrition widget data.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/1003464/nutritionWidget.json'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_analyzed_recipe_instructions(stepBreakdown: Annotated[Union[bool, None], Field(description='Whether to break down the recipe steps even more.')] = None) -> dict: 
    '''Get an analyzed breakdown of a recipe's instructions. Each step is enriched with the ingredients and the equipment that is used.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/324694/analyzedInstructions'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'stepBreakdown': stepBreakdown,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def extract_recipe_from_website(url: Annotated[str, Field(description='The URL of the recipe page.')],
                                forceExtraction: Annotated[Union[bool, None], Field(description='If true, the extraction will be triggered no matter whether we know the recipe already. Use that only if information is missing as this operation is slower.')] = None) -> dict: 
    '''Extract recipe data from a recipe blog or Web page.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/extract'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
        'forceExtraction': forceExtraction,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def analyze_recipe(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''This endpoint allows you to send raw recipe information, such as title, servings, and ingredients, to then see what we compute (badges, diets, nutrition, and more). This is useful if you have your own recipe data and want to enrich it with our semantic analysis.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/analyze'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def summarize_recipe() -> dict: 
    '''Summarize the recipe in a short text.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/4632/summary'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def analyze_recipe_instructions(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Extract ingredients and equipment from the recipe instruction steps.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/analyzeInstructions'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def classify_cuisine(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Classify the recipe's cuisine.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/cuisine'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def analyze_arecipe_search_query(q: Annotated[str, Field(description='The recipe search query.')]) -> dict: 
    '''Parse a recipe search query to find out its intention.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/queries/analyze'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def guess_nutrition_by_dish_name(title: Annotated[str, Field(description='The title of the dish.')]) -> dict: 
    '''Guess the macro nutrients of a dish given its title.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/guessNutrition'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'title': title,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def ingredient_search(query: Annotated[str, Field(description='The partial or full ingredient name.')],
                      addChildren: Annotated[Union[bool, None], Field(description='Whether to add children of found foods.')] = None,
                      minProteinPercent: Annotated[Union[int, float, None], Field(description='The minimum percentage of protein the food must have (between 0 and 100). Default: 5')] = None,
                      maxProteinPercent: Annotated[Union[int, float, None], Field(description='The maximum percentage of protein the food can have (between 0 and 100). Default: 50')] = None,
                      minFatPercent: Annotated[Union[int, float, None], Field(description='The minimum percentage of fat the food must have (between 0 and 100). Default: 1')] = None,
                      maxFatPercent: Annotated[Union[int, float, None], Field(description='The maximum percentage of fat the food can have (between 0 and 100). Default: 10')] = None,
                      minCarbsPercent: Annotated[Union[int, float, None], Field(description='The minimum percentage of carbs the food must have (between 0 and 100). Default: 5')] = None,
                      maxCarbsPercent: Annotated[Union[int, float, None], Field(description='The maximum percentage of carbs the food can have (between 0 and 100). Default: 30')] = None,
                      metaInformation: Annotated[Union[bool, None], Field(description='Whether to return more meta information about the ingredients.')] = None,
                      intolerances: Annotated[Union[str, None], Field(description='A comma-separated list of intolerances. All recipes returned must not contain ingredients that are not suitable for people with the intolerances entered. See a full list of supported intolerances.')] = None,
                      sort: Annotated[Union[str, None], Field(description='The strategy to sort recipes by. See a full list of supported sorting options.')] = None,
                      sortDirection: Annotated[Union[str, None], Field(description="The direction in which to sort. Must be either 'asc' (ascending) or 'desc' (descending).")] = None,
                      offset: Annotated[Union[str, None], Field(description='The number of results to skip (between 0 and 990).')] = None,
                      number: Annotated[Union[int, float, None], Field(description='The number of expected results (between 1 and 100). Default: 10')] = None) -> dict: 
    '''Search for simple whole foods (e.g. fruits, vegetables, nuts, grains, meat, fish, dairy etc.).'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/ingredients/search'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'addChildren': addChildren,
        'minProteinPercent': minProteinPercent,
        'maxProteinPercent': maxProteinPercent,
        'minFatPercent': minFatPercent,
        'maxFatPercent': maxFatPercent,
        'minCarbsPercent': minCarbsPercent,
        'maxCarbsPercent': maxCarbsPercent,
        'metaInformation': metaInformation,
        'intolerances': intolerances,
        'sort': sort,
        'sortDirection': sortDirection,
        'offset': offset,
        'number': number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_ingredient_information(amount: Annotated[Union[int, float, None], Field(description='The amount of that food. Default: 150')] = None,
                               unit: Annotated[Union[str, None], Field(description='The unit for the given amount.')] = None) -> dict: 
    '''Use an ingredient id to get all available information about an ingredient, such as its image and supermarket aisle.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/ingredients/9266/information'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'amount': amount,
        'unit': unit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def compute_ingredient_amount(nutrient: Annotated[str, Field(description='')],
                              target: Annotated[Union[int, float], Field(description='The target number of the given nutrient. Default: 10')],
                              unit: Annotated[Union[str, None], Field(description='The target unit.')] = None) -> dict: 
    '''Compute the amount you need of a certain ingredient for a certain nutritional goal. For example, how much soy milk do you have to drink to get 10 grams of protein?'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/ingredients/16223/amount'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'nutrient': nutrient,
        'target': target,
        'unit': unit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def convert_amounts(ingredientName: Annotated[str, Field(description='The ingredient which you want to convert, e.g. the flour in "2.5 cups of flour to grams"')],
                    targetUnit: Annotated[str, Field(description='The unit to which you want to convert, e.g. the grams in "2.5 cups of flour to grams". You can also use "piece", e.g. "3.4 oz tomatoes to piece"')],
                    sourceUnit: Annotated[Union[str, None], Field(description='The unit from which you want to convert, e.g. the cups in "2.5 cups of flour to grams". You can also use "serving" or "piece".')] = None,
                    sourceAmount: Annotated[Union[int, float, None], Field(description='The amount from which you want to convert, e.g. the 2.5 in "2.5 cups of flour to grams" Default: 2.5')] = None) -> dict: 
    '''Convert amounts like "2 cups of flour to grams".'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/convert'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ingredientName': ingredientName,
        'targetUnit': targetUnit,
        'sourceUnit': sourceUnit,
        'sourceAmount': sourceAmount,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def parse_ingredients(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Extract an ingredient from plain text.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/parseIngredients'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def compute_glycemic_load(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Retrieve the glycemic index for a list of ingredients and compute the individual and total glycemic load.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/ingredients/glycemicLoad'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def autocomplete_ingredient_search(query: Annotated[str, Field(description='The query - a partial or full ingredient name.')],
                                   number: Annotated[Union[int, float, None], Field(description='The number of results to return, between [1,100] Default: 10')] = None,
                                   metaInformation: Annotated[Union[bool, None], Field(description='Whether to return more meta information about the ingredients.')] = None,
                                   intolerances: Annotated[Union[str, None], Field(description='A comma-separated list of intolerances. All found ingredients must not cause problems for people with one of the given tolerances. Possible values are: dairy, egg, gluten, peanut, sesame, seafood, shellfish, soy, sulfite, tree nut, and wheat.')] = None) -> dict: 
    '''Autocomplete a search for an ingredient.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/ingredients/autocomplete'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'number': number,
        'metaInformation': metaInformation,
        'intolerances': intolerances,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_ingredient_substitutes(ingredientName: Annotated[str, Field(description='The name of the ingredient you want to replace.')]) -> dict: 
    '''Get ingredient substitutes by ingredient name.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/ingredients/substitutes'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ingredientName': ingredientName,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_ingredient_substitutes_by_id() -> dict: 
    '''Search for substitutes for a given ingredient.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/ingredients/1001/substitutes'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_grocery_products(query: Annotated[str, Field(description='The search query.')],
                            maxCalories: Annotated[Union[int, float, None], Field(description='The maximum number of calories the product can have. Default: 5000')] = None,
                            minProtein: Annotated[Union[int, float, None], Field(description='The minimum number of grams of protein the product can have. Default: 0')] = None,
                            maxProtein: Annotated[Union[int, float, None], Field(description='The maximum number of grams of protein the product can have. Default: 100')] = None,
                            minFat: Annotated[Union[int, float, None], Field(description='The minimum number of grams of fat the product can have. Default: 0')] = None,
                            maxFat: Annotated[Union[int, float, None], Field(description='The maximum number of grams of fat the product can have. Default: 100')] = None,
                            minCarbs: Annotated[Union[int, float, None], Field(description='The minimum number of grams of carbs the product can have. Default: 0')] = None,
                            maxCarbs: Annotated[Union[int, float, None], Field(description='The maximum number of grams of carbs the product can have. Default: 100')] = None,
                            minCalories: Annotated[Union[int, float, None], Field(description='The minimum number of calories the product can have. Default: 0')] = None,
                            offset: Annotated[Union[int, float, None], Field(description='The number of results to skip, defaults to 0. Default: 0')] = None,
                            number: Annotated[Union[int, float, None], Field(description='The number of results to retrieve, defaults to 10. Default: 10')] = None) -> dict: 
    '''Search packaged food products like frozen pizza and snickers bars.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/search'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'maxCalories': maxCalories,
        'minProtein': minProtein,
        'maxProtein': maxProtein,
        'minFat': minFat,
        'maxFat': maxFat,
        'minCarbs': minCarbs,
        'maxCarbs': maxCarbs,
        'minCalories': minCalories,
        'offset': offset,
        'number': number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_grocery_products_by_upc() -> dict: 
    '''Get information about a food product given its UPC.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/upc/041631000564'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_product_information() -> dict: 
    '''Get information about a packaged food product.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/22347'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_comparable_products() -> dict: 
    '''Find comparable products to the given one.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/upc/033698816271/comparable'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def autocomplete_product_search(query: Annotated[str, Field(description='The (partial) search query.')],
                                number: Annotated[Union[int, float, None], Field(description='The number of results to return. Must be between 1 and 25. Default: 10')] = None) -> dict: 
    '''Generate suggestions for grocery products based on a (partial) query. The matches will be found by looking in the title only.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/suggest'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'number': number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def classify_agrocery_product(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Given a grocery product title, this endpoint allows you to detect what basic ingredient it is.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/classify'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def classify_grocery_product_bulk(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Provide a set of product jsons, get back classified products.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/classifyBatch'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def map_ingredients_to_grocery_products(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Map a set of ingredients to products you can buy in the grocery store.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/ingredients/map'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def search_menu_items(query: Annotated[str, Field(description='The search query.')],
                      offset: Annotated[Union[int, float, None], Field(description='The search offset. Default: 0')] = None,
                      number: Annotated[Union[int, float, None], Field(description='The number of results to return. Default: 10')] = None,
                      minCalories: Annotated[Union[int, float, None], Field(description='The minimum number of calories the menu item can have Default: 0')] = None,
                      maxCalories: Annotated[Union[int, float, None], Field(description='The maximum number of calories the menu item can have Default: 5000')] = None,
                      minProtein: Annotated[Union[int, float, None], Field(description='The minimum number of grams of protein the menu item can have Default: 0')] = None,
                      maxProtein: Annotated[Union[int, float, None], Field(description='The maximum number of grams of protein the menu item can have Default: 100')] = None,
                      minFat: Annotated[Union[int, float, None], Field(description='The minimum number of grams of fat the menu item can have. Default: 0')] = None,
                      maxFat: Annotated[Union[int, float, None], Field(description='The maximum number of grams of fat the menu item can have. Default: 100')] = None,
                      minCarbs: Annotated[Union[int, float, None], Field(description='The minimum number of grams of carbs the menu item can have. Default: 0')] = None,
                      maxCarbs: Annotated[Union[int, float, None], Field(description='The maximum number of grams of carbs the menu item can have. Default: 100')] = None) -> dict: 
    '''Search menu items (such as McDonalds Big Mac)'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/menuItems/search'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'offset': offset,
        'number': number,
        'minCalories': minCalories,
        'maxCalories': maxCalories,
        'minProtein': minProtein,
        'maxProtein': maxProtein,
        'minFat': minFat,
        'maxFat': maxFat,
        'minCarbs': minCarbs,
        'maxCarbs': maxCarbs,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_menu_item_information() -> dict: 
    '''Get information about a certain menu item.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/menuItems/%7Bid%7D'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def autocomplete_menu_item_search(query: Annotated[str, Field(description='The (partial) search query.')],
                                  number: Annotated[Union[int, float, None], Field(description='The number of results to return. Must be between 1 and 25. Default: 10')] = None) -> dict: 
    '''Generate suggestions for menu items based on a (partial) query. The matches will be found by looking in the title only.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/menuItems/suggest'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'number': number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_meal_plan_week(hash: Annotated[Union[str, None], Field(description='The private hash for the username.')] = None) -> dict: 
    '''Retrieve a meal planned week for the given user. The username must be a spoonacular user and the hash must the the user's hash that can be found in his/her account.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/dsky/week/2020-06-01'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hash': hash,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_meal_plan_day(hash: Annotated[Union[str, None], Field(description='The private hash for the username.')] = None) -> dict: 
    '''Retrieve a meal planned day for the given user. The username must be a spoonacular user and the hash must the the user's hash that can be found in his/her account.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/dsky/day/2020-06-01'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hash': hash,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def generate_meal_plan(timeFrame: Annotated[Union[str, None], Field(description="Either for one 'day' or an entire 'week'.")] = None,
                       targetCalories: Annotated[Union[int, float, None], Field(description='What is the caloric target for one day? The meal plan generator will try to get as close as possible to that goal. Default: 2000')] = None,
                       diet: Annotated[Union[str, None], Field(description='Enter a diet that the meal plan has to adhere to, e.g. "vegetarian", "vegan", "paleo" etc.')] = None,
                       exclude: Annotated[Union[str, None], Field(description='A comma-separated list of allergens or ingredients that must be excluded.')] = None) -> dict: 
    '''Generate a meal plan with three meals per day (breakfast, lunch, and dinner).'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'timeFrame': timeFrame,
        'targetCalories': targetCalories,
        'diet': diet,
        'exclude': exclude,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def add_to_meal_plan(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Add an item to the user's meal plan. The Add to Meal Plan endpoint is complex, be sure to review the [guide here](https://spoonacular.com/food-api/docs#Add-to-Meal-Plan)'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/dsky/items'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def clear_meal_plan_day(hash: Annotated[str, Field(description='')]) -> dict: 
    '''Delete all planned items from the user's meal plan for a specific day.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/dsky/day/2020-06-01'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hash': hash,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.delete(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def delete_from_meal_plan(hash: Annotated[str, Field(description='The private hash for the username.')]) -> dict: 
    '''Delete an item from the user's meal plan.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/dsky/items/15678'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hash': hash,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.delete(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_meal_plan_templates(hash: Annotated[str, Field(description='The private hash for the username.')]) -> dict: 
    '''Get meal plan templates from user or public ones. This documentation is for getting user templates. You can also get public templates. Read more about this [here](https://spoonacular.com/food-api/docs#Get-Meal-Plan-Templates).'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/dsky/templates'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hash': hash,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_meal_plan_template(hash: Annotated[str, Field(description='The private hash for the username.')]) -> dict: 
    '''Get information about a meal plan template.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/dsky/templates/15678'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hash': hash,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def add_meal_plan_template(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Add a meal plan template for a user.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/dsky/templates'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def delete_meal_plan_template(hash: Annotated[str, Field(description='The private hash for the username.')]) -> dict: 
    '''Delete a meal plan template for a user.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/dsky/templates/15678'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hash': hash,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.delete(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_shopping_list(hash: Annotated[str, Field(description='The private hash for the username.')]) -> dict: 
    '''Get the current shopping list for the given user.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/dsky/shopping-list'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hash': hash,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def add_to_shopping_list(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Add an item to the current shopping list of a user.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/dsky/shopping-list/items'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def delete_from_shopping_list(hash: Annotated[str, Field(description='The private hash for the username.')]) -> dict: 
    '''Delete an item from the current shopping list of the user.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/dsky/shopping-list/items/15678'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hash': hash,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.delete(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def generate_shopping_list(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Generate the shopping list for a user from the meal planner in a given time frame.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/dsky/shopping-list/2020-06-01/2020-06-07'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def compute_shopping_list(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Compute a shopping list from a set of simple foods. This endpoint does not require usernames.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/shopping-list/compute'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def search_custom_foods(query: Annotated[str, Field(description='The search query.')],
                        username: Annotated[str, Field(description='The username.')],
                        hash: Annotated[str, Field(description='The private hash for the username.')],
                        offset: Annotated[Union[int, float, None], Field(description='The number of results to skip (between 0 and 990). Default: 0')] = None,
                        number: Annotated[Union[int, float, None], Field(description='The number of expected results (between 1 and 100). Default: 10')] = None) -> dict: 
    '''Search custom foods in a user's account.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/customFoods/search'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'username': username,
        'hash': hash,
        'offset': offset,
        'number': number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def connect_user(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''In order to call user-specific endpoints, you need to connect your app's users to spoonacular users. Just call this endpoint with your user's information and you will get back a username and hash that you must save on your side. In future requests that you make on this user's behalf you simply pass their username and hash alongside your API key.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/users/connect'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def dish_pairing_for_wine(wine: Annotated[str, Field(description='The type of wine that should be paired, e.g. "merlot", "riesling", or "malbec".')]) -> dict: 
    '''Find a dish that goes well with a given wine.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/wine/dishes'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'wine': wine,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def wine_pairing(food: Annotated[str, Field(description='The food to get a pairing for. This can be a dish ("steak"), an ingredient ("salmon"), or a cuisine ("italian").')],
                 maxPrice: Annotated[Union[int, float, None], Field(description='The maximum price for the specific wine recommendation. Default: 50')] = None) -> dict: 
    '''Find a wine that goes well with a food. Food can be a dish name ("lasagna"), an ingredient name ("salmon"), or a cuisine ("italian").'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/wine/pairing'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'food': food,
        'maxPrice': maxPrice,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def wine_description(wine: Annotated[str, Field(description='The name of the wine, e.g. "malbec", "riesling", or "merlot".')]) -> dict: 
    '''Get a simple description of a certain wine, e.g. "malbec", "riesling", or "merlot".'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/wine/description'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'wine': wine,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def wine_recommendation(wine: Annotated[str, Field(description='The name of the wine to get a specific product recommendation for.')],
                        maxPrice: Annotated[Union[int, float, None], Field(description='The maximum price of the recommended wine. Default: 50')] = None,
                        minRating: Annotated[Union[int, float, None], Field(description='The minimum rating of the recommended wine between 0 and 1. For example, 0.8 equals 4 out of 5 stars. Default: 0.7')] = None,
                        number: Annotated[Union[int, float, None], Field(description='The number of wine recommendations expected. Default: 3')] = None) -> dict: 
    '''Get a specific wine recommendation (concrete product) for a given wine type, e.g. "merlot".'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/wine/recommendation'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'wine': wine,
        'maxPrice': maxPrice,
        'minRating': minRating,
        'number': number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_all_food(query: Annotated[str, Field(description='')],
                    offset: Annotated[Union[str, None], Field(description='')] = None,
                    number: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search all food content with one call. That includes recipes, grocery products, menu items, simple foods (ingredients), and food videos.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/search'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'offset': offset,
        'number': number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def image_classification(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Classify a food image.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/images/classify'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def image_analysis(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Classify and analyze a food image.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/images/analyze'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def search_food_videos(query: Annotated[Union[str, None], Field(description='The search query.')] = None,
                       type: Annotated[Union[str, None], Field(description='The type of the recipe, e.g. one of the following: main course, side dish, dessert, appetizer, salad, bread, breakfast, soup, beverage, sauce, or drink.')] = None,
                       minLength: Annotated[Union[int, float, None], Field(description='Minimum video length in seconds. Default: 0')] = None,
                       maxLength: Annotated[Union[int, float, None], Field(description='Maximum video length in seconds. Default: 999')] = None,
                       number: Annotated[Union[int, float, None], Field(description='The number of results [1,100]. Default: 10')] = None,
                       cuisine: Annotated[Union[str, None], Field(description='The cuisine of the videos, e.g. one of the following: african, chinese, japanese, korean, vietnamese, thai, indian, british, irish, french, italian, mexican, spanish, middle eastern, jewish, american, cajun, southern, greek, german, nordic, eastern european, caribbean, latin american')] = None,
                       includeingredients: Annotated[Union[str, None], Field(description='Ingredients the recipe videos must contain.')] = None,
                       excludeingredients: Annotated[Union[str, None], Field(description='Ingredients the recipe videos must not contain.')] = None,
                       offset: Annotated[Union[int, float, None], Field(description='The offset in the result set [0,900]. Default: 0')] = None) -> dict: 
    '''Find recipe and other food related videos.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/videos/search'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'type': type,
        'minLength': minLength,
        'maxLength': maxLength,
        'number': number,
        'cuisine': cuisine,
        'includeingredients': includeingredients,
        'excludeingredients': excludeingredients,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def quick_answer(q: Annotated[str, Field(description='The nutrition-related question.')]) -> dict: 
    '''Answer a nutrition related natural language question.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/quickAnswer'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def detect_food_in_text(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Detect ingredients and dishes in texts.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/detect'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def search_site_content(query: Annotated[str, Field(description='The query to search for. You can also use partial queries such as "spagh" to already find spaghetti recipes, articles, grocery products, and other content.')]) -> dict: 
    '''Search spoonacular's site content. You'll be able to find everything that you could also find using the search suggests on spoonacular.com. This is a suggest API so you can send partial strings as queries.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/site/search'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_arandom_food_joke() -> dict: 
    '''Get a random joke that includes or is about food.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/jokes/random'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_random_food_trivia() -> dict: 
    '''Returns random food trivia.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/trivia/random'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def talk_to_chatbot(text: Annotated[str, Field(description='The request/question/answer from the user to the chat bot.')],
                    contextId: Annotated[Union[str, None], Field(description='An arbitrary globally unique id for your conversation. The conversation can contain states so you should pass your context id if you want the bot to be able to remember the conversation.')] = None) -> dict: 
    '''This endpoint can be used to have a conversation about food with the spoonacular chat bot. Use the chat suggests endpoint to show your user what he or she can say.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/converse'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'text': text,
        'contextId': contextId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def conversation_suggests(query: Annotated[str, Field(description='A (partial) query from the user. The endpoint will return if it matches topics it can talk about.')],
                          number: Annotated[Union[int, float, None], Field(description='The number of suggestions to return must be in interval [1,25]. Default: 10')] = None) -> dict: 
    '''This endpoint returns suggestions for things the user can say or ask the chat bot.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/converse/suggest'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'number': number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def recipe_nutrition_label_widget(defaultCss: Annotated[Union[bool, None], Field(description='Whether the default CSS should be added to the response.')] = None,
                                  showOptionalNutrients: Annotated[Union[bool, None], Field(description='')] = None,
                                  showZeroValues: Annotated[Union[bool, None], Field(description='')] = None,
                                  showIngredients: Annotated[Union[bool, None], Field(description='')] = None) -> dict: 
    '''Get a recipe's nutrition label as an HTML widget.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/641166/nutritionLabel'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'defaultCss': defaultCss,
        'showOptionalNutrients': showOptionalNutrients,
        'showZeroValues': showZeroValues,
        'showIngredients': showIngredients,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def recipe_nutrition_label_image(showOptionalNutrients: Annotated[Union[bool, None], Field(description='')] = None,
                                 showZeroValues: Annotated[Union[bool, None], Field(description='')] = None,
                                 showIngredients: Annotated[Union[bool, None], Field(description='')] = None) -> dict: 
    '''Get a recipe's nutrition label as an image.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/641166/nutritionLabel.png'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'showOptionalNutrients': showOptionalNutrients,
        'showZeroValues': showZeroValues,
        'showIngredients': showIngredients,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def recipe_nutrition_widget(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Visualize a recipe's nutritional information as HTML including CSS. Full example code of how to work with widgets can be found in our [spoonacular-widget GitHub](https://github.com/ddsky/spoonacular-widgets).'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/visualizeNutrition'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def recipe_nutrition_by_id_widget(defaultCss: Annotated[Union[bool, None], Field(description='')] = None) -> dict: 
    '''Visualize a recipe's nutritional information as HTML including CSS.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/1082038/nutritionWidget'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'defaultCss': defaultCss,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def recipe_nutrition_by_id_image() -> dict: 
    '''Visualize a recipe's nutritional information as an image.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/1082038/nutritionWidget.png'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def equipment_by_id_widget(defaultCss: Annotated[Union[bool, None], Field(description='')] = None) -> dict: 
    '''Visualize a recipe's equipment list.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/44860/equipmentWidget'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'defaultCss': defaultCss,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def equipment_widget(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Visualize the equipment used to make a recipe.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/visualizeEquipment'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def equipment_by_id_image() -> dict: 
    '''Visualize a recipe's equipment list as an image.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/44860/equipmentWidget.png'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def ingredients_widget(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Visualize ingredients of a recipe.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/visualizeIngredients'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def ingredients_by_id_widget(defaultCss: Annotated[Union[bool, None], Field(description='Whether the default CSS should be added to the response.')] = None,
                             measure: Annotated[Union[str, None], Field(description="Whether the the measures should be 'us' or 'metric'.")] = None) -> dict: 
    '''Visualize a recipe's ingredient list.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/1082038/ingredientWidget'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'defaultCss': defaultCss,
        'measure': measure,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def ingredients_by_id_image(measure: Annotated[Union[str, None], Field(description="Whether the the measures should be 'us' or 'metric'.")] = None) -> dict: 
    '''Visualize a recipe's ingredient list.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/1082038/ingredientWidget.png'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'measure': measure,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def price_breakdown_widget(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Visualize the price breakdown of a recipe.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/visualizePriceEstimator'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def price_breakdown_by_id_image(mode: Annotated[Union[int, float, None], Field(description='The mode in which the widget should be delivered. 1 = separate views (compact), 2 = all in one view (full). Default: 1')] = None) -> dict: 
    '''Visualize a recipe's price breakdown.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/1082038/priceBreakdownWidget.png'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'mode': mode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def product_nutrition_label_widget(defaultCss: Annotated[Union[bool, None], Field(description='Whether the default CSS should be added to the response.')] = None,
                                   showOptionalNutrients: Annotated[Union[bool, None], Field(description='Whether to show optional nutrients.')] = None,
                                   showZeroValues: Annotated[Union[bool, None], Field(description='Whether to show zero values.')] = None,
                                   showIngredients: Annotated[Union[bool, None], Field(description='Whether to show a list of ingredients.')] = None) -> dict: 
    '''Get a product's nutrition label as an HTML widget.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/22347/nutritionLabel'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'defaultCss': defaultCss,
        'showOptionalNutrients': showOptionalNutrients,
        'showZeroValues': showZeroValues,
        'showIngredients': showIngredients,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def product_nutrition_label_image(showOptionalNutrients: Annotated[Union[bool, None], Field(description='Whether to show optional nutrients.')] = None,
                                  showZeroValues: Annotated[Union[bool, None], Field(description='Whether to show zero values.')] = None,
                                  showIngredients: Annotated[Union[bool, None], Field(description='Whether to show a list of ingredients.')] = None) -> dict: 
    '''Get a product's nutrition label as an image.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/22347/nutritionLabel.png'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'showOptionalNutrients': showOptionalNutrients,
        'showZeroValues': showZeroValues,
        'showIngredients': showIngredients,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def product_nutrition_by_id_widget(defaultCss: Annotated[Union[bool, None], Field(description='Whether the default CSS should be added to the response.')] = None) -> dict: 
    '''Visualize a product's nutritional information as HTML including CSS.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/7657/nutritionWidget'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'defaultCss': defaultCss,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def product_nutrition_by_id_image() -> dict: 
    '''Visualize a product's nutritional information as an image.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/7657/nutritionWidget.png'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def menu_item_nutrition_label_widget(defaultCss: Annotated[Union[bool, None], Field(description='Whether the default CSS should be added to the response.')] = None,
                                     showOptionalNutrients: Annotated[Union[bool, None], Field(description='Whether to show optional nutrients.')] = None,
                                     showZeroValues: Annotated[Union[bool, None], Field(description='Whether to show zero values.')] = None,
                                     showIngredients: Annotated[Union[bool, None], Field(description='Whether to show a list of ingredients.')] = None) -> dict: 
    '''Visualize a menu item's nutritional label information as HTML including CSS.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/menuItems/342313/nutritionLabel'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'defaultCss': defaultCss,
        'showOptionalNutrients': showOptionalNutrients,
        'showZeroValues': showZeroValues,
        'showIngredients': showIngredients,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def menu_item_nutrition_label_image(showOptionalNutrients: Annotated[Union[bool, None], Field(description='Whether to show optional nutrients.')] = None,
                                    showZeroValues: Annotated[Union[bool, None], Field(description='Whether to show zero values.')] = None,
                                    showIngredients: Annotated[Union[bool, None], Field(description='Whether to show a list of ingredients.')] = None) -> dict: 
    '''Visualize a menu item's nutritional label information as an image.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/menuItems/342313/nutritionLabel.png'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'showOptionalNutrients': showOptionalNutrients,
        'showZeroValues': showZeroValues,
        'showIngredients': showIngredients,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def menu_item_nutrition_by_id_widget(defaultCss: Annotated[Union[bool, None], Field(description='Whether the default CSS should be added to the response.')] = None) -> dict: 
    '''Visualize a menu item's nutritional information as HTML including CSS.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/menuItems/424571/nutritionWidget'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'defaultCss': defaultCss,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def menu_item_nutrition_by_id_image() -> dict: 
    '''Visualize a menu item's nutritional information as HTML including CSS.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/menuItems/424571/nutritionWidget.png'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_recipe_card(mask: Annotated[Union[str, None], Field(description='The mask to put over the recipe image ("ellipseMask", "diamondMask", "starMask", "heartMask", "potMask", "fishMask").')] = None,
                    backgroundImage: Annotated[Union[str, None], Field(description='The background image ("none","background1", or "background2").')] = None,
                    backgroundColor: Annotated[Union[str, None], Field(description='The background color for the recipe card as a hex-string.')] = None,
                    fontColor: Annotated[Union[str, None], Field(description='The font color for the recipe card as a hex-string.')] = None) -> dict: 
    '''Generate a recipe card for a recipe.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/1446603/card'
    headers = {'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'mask': mask,
        'backgroundImage': backgroundImage,
        'backgroundColor': backgroundColor,
        'fontColor': fontColor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def create_recipe_card(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Create a recipe card given a recipe.'''
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/visualizeRecipe'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
