from flask import Flask, request, jsonify
import uvicorn
from ariadne import ObjectType, load_schema_from_path, make_executable_schema
from dotenv import dotenv_values
from ariadne.asgi import GraphQL
from src.jobsResolvers import create_jobs_resolvers

config = dotenv_values(".env")

app=Flask(__name__)

query = ObjectType("Query")
mutation = ObjectType("Mutation")

mutation.set_field("createEvent", create_jobs_resolvers)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation
)

app=GraphQL(schema, debug=True)

if __name__=='__main__':
    uvicorn.run("main:app", host="127.0.0.1", port="4000")