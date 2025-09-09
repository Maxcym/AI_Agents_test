#!/usr/bin/env python
"""
Main entry point for interacting with the Latest AI Development crew.

This file is designed to be used with the `crewai` CLI:
    crewai run      → Runs the crew (calls run())
    crewai train    → Trains the crew (calls train())
    crewai replay   → Replays execution from a given task (calls replay())
    crewai test     → Tests the crew (calls test())

Each function below is a thin wrapper around `LatestAiDevelopment().crew()`
and should not contain additional business logic.

Environment variables:
    MODEL (str):     The model identifier to be used by the crew (optional).
    API_BASE (str):  The base URL of the API used by the crew (optional).
"""

import os
import sys
import warnings
from datetime import datetime
from latest_ai_development.crew import LatestAiDevelopment

# Ignore SyntaxWarnings coming from the pysbd dependency
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

MODEL = os.getenv("MODEL")
API_BASE = os.getenv("API_BASE")


def run():
    """
    Run the crew with default inputs.

    Inputs:
        - topic (str): "AI LLMs"
        - current_year (str): Current year at runtime.

    Raises:
        Exception: If an error occurs while running the crew.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year),
    }
    try:
        LatestAiDevelopment().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.

    Command-line arguments (automatically passed by `crewai`):
        sys.argv[1] (int): Number of training iterations.
        sys.argv[2] (str): Filename where training results will be saved.

    Inputs:
        - topic (str): "AI LLMs"

    Raises:
        Exception: If an error occurs during training.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        LatestAiDevelopment().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs,
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.

    Command-line arguments (automatically passed by `crewai`):
        sys.argv[1] (str): Task ID from which to replay the execution.

    Raises:
        Exception: If an error occurs while replaying the crew.
    """
    try:
        LatestAiDevelopment().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and return the results.

    Command-line arguments (automatically passed by `crewai`):
        sys.argv[1] (int): Number of iterations for testing.
        sys.argv[2] (str): Evaluation LLM identifier.

    Inputs:
        - topic (str): "AI LLMs"
        - current_year (str): Current year at runtime.

    Raises:
        Exception: If an error occurs during testing.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year),
    }
    try:
        LatestAiDevelopment().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=str(sys.argv[2]),
            inputs=inputs,
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
