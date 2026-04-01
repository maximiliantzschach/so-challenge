# 001 — Project Setup
**Date**: 2026-04-01 **Tool**: Copilot CLI **Model**: GPT-4.1
**Iterations**: 1
## Prompt
**2026-04-01 00:52**
Create a Python project called so-challenge using uv for
dependency management. Separate data collection
(data_fetcher.py) from visualization (plotter.py), with a
module for milestones (milestones.py).
Set up pytest with test files for each module. Manage all
dependencies through pyproject.toml. Include a README.md.
Create a diary/ folder for tracking AI interactions.

For every prompt cycle, save the interaction record to
diary/ as a numbered markdown file. Use this format:
# NNN — Short Title
**Date**: YYYY-MM-DD **Tool**: [name] **Model**: [name]
**Iterations**: [number]
## Prompt
**YYYY-MM-DD HH:MM**
[The full prompt text as given by the user.]
Save this setup prompt as diary/001-project-setup.md.

Do NOT implement any logic yet — just create the project
structure, configuration, and empty module files with
docstrings describing their purpose.
Initialize a git repository and create an initial commit.
Then create a GitHub repository using the gh CLI and push.
