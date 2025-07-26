"""Prototype scoring pipeline using LangChain and OpenAI."""

from __future__ import annotations

import os
from typing import List

from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import PydanticOutputParser


class Score(BaseModel):
    """Structured scoring output."""

    fit: int = Field(ge=0, le=5)
    pain: int
    ai_maturity: int
    intent: int
    budget_authority: int
    timing: int
    rationale: str
    evidence: List[str]
    final_score: int


def build_chain(model: str = "gpt-3.5-turbo-0613"):
    llm = ChatOpenAI(model=model, temperature=0)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a B2B sales analyst scoring how likely a company is to buy AI agents from Fineguide.ai.",
            ),
            (
                "user",
                """Company: {name}\nWebsite text: {web_context}\nStructured data: {firmo}\nInstructions: Score each category 0-5 and explain. Return JSON only.""",
            ),
        ]
    )

    parser = PydanticOutputParser(pydantic_object=Score)
    return prompt | llm | parser


if __name__ == "__main__":
    if "OPENAI_API_KEY" not in os.environ:
        raise SystemExit("Please set the OPENAI_API_KEY environment variable")

    chain = build_chain()

    # Example usage with dummy data
    result = chain.invoke(
        {
            "name": "Example Corp",
            "web_context": "Example Corp provides 24/7 online retail services.",
            "firmo": "Employees: 1000, Industry: e-commerce",
        }
    )
    print(result.json())
