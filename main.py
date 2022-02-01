from flask import Flask, request, render_template, debughelpers
from my_code import get_settings


app = Flask(__name__)


@app.route('/')
def page_index():
    settings = get_settings()
    online = settings.get("online", False)
    if online:
        return "приложение работает"
    return "приложение не работает"


@app.route("/candidate/<int:id>")
def page_candidate(id):
    candidate = get_candidates_by_cid(id)
    page_content = f"""
    <h1>{candidate["name"]}</h1>
    <p>{candidate["position"]}</p>
    <img src = "{candidate["picture"]} width = 200/>
    <p>{candidate["skills"]}</p>
    """
    return page_content


@app.route("/list")
def page_list_of_candidates():
    candidates = get_candidates()
    page_content = "<h1>Все кандидаты</h1>"

    for candidate in candidates:
        page_content += f"""
            <p><a href = "/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
        """
        return page_content


@app.route("/search")
def page_search():
    name = request.args.get("name", "")
    candidates = search_name(name)

    candidates_count = len(candidates)
    page_content = f"<h2>Найдено кандидатов {candidates_count}</h2>"

    for candidate in candidates:
        page_content += f"""
               <p><a href = "/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
           """
        return page_content


@app.route("/skill/<skill_name>")
def get_skills(skill_name):
    candidates = get_skills(skill_name)

    candidates_count = len(candidates)
    page_content = f"<h2>Найдено кандидатов со скиллом {skill_name} : {candidates_count}</h2>"

    for candidate in candidates:
        page_content += f"""
               <p><a href = "/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
           """
        return page_content


app.run()
