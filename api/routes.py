from flask import Flask, request, jsonify
from infra.adapters.jira_adapter import JiraAdapter, jira_client
import logging

app = Flask(__name__)

@app.route("/projects", methods=["GET"])
def get_projects():
    logging.info("Listando todos os projetos disponiveis no Jira")

    try:
        projects = JiraAdapter.jira_client.projects()
        projects_list = [{"key": project.key, "name": project.name} for project in projects]
        return jsonify(projects_list)
    except Exception as e:
        logging.info("error: ", str(e))
        return jsonify({"error": str(e)}), 500

@app.route("/create_ticket", methods=["POST"])
def create_ticket():
    logging.info("Criando ticket no Jira.")
    data = request.get_json()
    project_key = data.get("project_key")
    summary = data.get("summary")
    description = data.get("description")

    try:
        issue  = jira_client.create_issue(
            fields={
                "project": {"key": project_key},
                "summary": summary,
                "description": description,
                "issuetype": {"name": "Task"},
            }
        )
        return jsonify({"ticket_id  ": issue.key, "message": "Ticket criado com sucesso!", "status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500    

