from flask import Flask, request, render_template, debughelpers
from my_code import get_settings
from my_code import get_candidates_by_id
from my_code import search_name
from my_code import get_skills
from my_code import get_candidates

app = Flask(__name__)


@app.route('/')
def page_index():
    settings = get_settings()
    online = settings.get("online", False)
    #if online:
     #   return render_template('page_index.html', yeas="приложение работает")
    #return render_template('page_index.html', no="приложение не работает")
    return render_template('page_index.html')

@app.route("/candidate/<int:id>")
def page_candidates(id):
    candidate = get_candidates_by_id(id)
    #page_content = f"""
    #<h1>{candidate["name"]}</h1>
    #<p>{candidate["position"]}</p>
    #<img src = "{candidate["picture"]} width = 200/>
    #<p>{candidate["skills"]}</p>
  #  """
    return render_template('page_candidates.html', name = candidate["name"], position = candidate["position"], photo = candidate["picture"], skills = candidate["skills"])


@app.route("/list")
def list():
    candidates = get_candidates()
    for candidate in candidates:
      return render_template('list.html', eho = "Все кандидаты", cid = candidate["id"], ut = candidate["name"])


@app.route("/search")
def page_search():
    name = request.args.get("name", "")
    candidates = search_name(name)
    #candidates_count = len(candidates)
  #  page_content = f"<h2>Найдено кандидатов {candidates_count}</h2>"
    for candidate in candidates:
      return render_template('page_search.html', count = len(candidates), cid = candidate["id"], name = candidate["name"])
        #page_content += f"""
         #      <p><a href = "/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
          # """



@app.route("/skill/<skill_name>")
def page_skills(skill_name):
    candidates = get_skills(skill_name)

    #candidates_count = len(candidates)
   # page_content = f"<h2>Найдено кандидатов со скиллом {skill_name} : {candidates_count}</h2>"

    for candidate in candidates:
        #page_content += f"""
         #      <p><a href = "/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
          # """

        return render_template('page_skills.html', name = skill_name, count = len(candidates), id = candidate["id"], candidate_name = candidate["name"])


app.run(debug=True)
