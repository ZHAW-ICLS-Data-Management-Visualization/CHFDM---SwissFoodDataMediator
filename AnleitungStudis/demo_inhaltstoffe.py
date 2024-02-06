
import requests
import pandas as pd
import sparql_dataframe

# Define the SPARQL endpoint
endpoint = "http://microserver.zhaw.ch:3030/DaPro/sparql"

# Define the SPARQL query
query = """
SELECT ?subject ?object
WHERE {
    ?subject <http://www.w3.org/2000/01/rdf-schema#label> ?object
}
LIMIT 1000
"""

# ?predicate mit <http://www.w3.org/2000/01/rdf-schema#label> ersetzen

df = sparql_dataframe.get(endpoint, query, post=True)

# Print the DataFrame as a table
print(df.to_string(index=False))
