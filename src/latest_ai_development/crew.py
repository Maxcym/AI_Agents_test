"""
Crew definition for the Latest AI Development project.

This module defines the `LatestAiDevelopment` crew using the CrewAI framework.
It includes agent definitions, task configurations, and the crew assembly logic.

Key concepts:
    - Agents: Independent roles that handle parts of the workflow.
    - Tasks: Units of work executed by agents.
    - Crew: Orchestrates agents and tasks together under a process.

Environment variables:
    MODEL (str):     The model identifier used by CrewAI agents.
    API_BASE (str):  The base URL of the API used by CrewAI agents.

References:
    CrewAI documentation:
        Agents: https://docs.crewai.com/concepts/agents
        Tasks:  https://docs.crewai.com/concepts/tasks
        Crews:  https://docs.crewai.com/concepts/crews
"""

import os
from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

MODEL = os.getenv("MODEL")
API_BASE = os.getenv("API_BASE")


@CrewBase
class LatestAiDevelopment:
    """
    Crew definition for the Latest AI Development workflow.

    This crew includes:
        - Researcher agent: Gathers and analyzes AI-related information.
        - Reporting analyst agent: Summarizes findings into reports.
        - Manager agent: Oversees the process, manages delegation.
        - Research and reporting tasks: Define the workflow outputs.
    """

    # Paths to configuration files for agents and tasks.
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        """
        Researcher agent responsible for exploring the latest AI developments.

        Returns:
            Agent: Configured Researcher agent.
        """
        return Agent(
            config=self.agents_config["researcher"],
            verbose=True,
            llm=LLM(model=MODEL, base_url=API_BASE),
        )

    @agent
    def reporting_analyst(self) -> Agent:
        """
        Reporting Analyst agent responsible for summarizing research findings.

        Returns:
            Agent: Configured Reporting Analyst agent.
        """
        return Agent(
            config=self.agents_config["reporting_analyst"],
            verbose=True,
            llm=LLM(model=MODEL, base_url=API_BASE),
        )

    def manager(self) -> Agent:
        """
        Manager agent that oversees workflow execution
        and can delegate tasks to other agents.

        Returns:
            Agent: Configured Manager agent with delegation enabled.
        """
        return Agent(
            config=self.agents_config["manager"],
            verbose=True,
            allow_delegation=True,
            llm=LLM(model=MODEL, base_url=API_BASE),
        )

    @task
    def research_task(self) -> Task:
        """
        Task for researching the latest AI developments.

        Returns:
            Task: Configured research task.
        """
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def reporting_task(self) -> Task:
        """
        Task for generating a structured report from research findings.

        The output is saved to a Markdown file.

        Returns:
            Task: Configured reporting task with output file.
        """
        return Task(
            config=self.tasks_config["reporting_task"],
            output_file="report.md",
        )

    @crew
    def crew(self) -> Crew:
        """
        Creates and configures the Latest AI Development crew.

        This crew uses a hierarchical process where the manager agent
        oversees and coordinates the researcher and reporting analyst agents.

        Returns:
            Crew: Configured Crew instance.
        """
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            manager_agent=self.manager(),
            process=Process.hierarchical,
            verbose=True,
        )
