import json
import pprint


def get_settings():
    with open("settings.json", "r", encoding="utf-8") as f:
        data_json = json.load(f)
    return data_json


def get_candidates():
    with open("candidates.json", "r", encoding="utf-8") as f:
        data_json = json.load(f)
    return data_json


def get_candidates_by_id(id):
    candidates = get_candidates()
    for candidate in candidates:
        if candidate.get("id") == id_candidate:
            return candidate


def search_name(name):
    settings = get_settings()
    case_sensitive = settings["case-sensitive"]

    candidates = get_candidates()
    candidates_match = []

    for candidate in candidates:
        if name in candidate["name"]:
            candidates_match.append(candidate)
            continue

        if not case_sensitive:
            if name.lower() in candidate["name"].lower():
                candidates_match.append(candidate)

    return candidates_match


def get_skills(skill_name):
    settings = get_settings()
    limit = settings.get('limit', 3)
    candidates = get_candidates()
    candidates_match = []

    skill_name = skill_name.lower()
    for candidate in candidates:
        skills = candidate["skills"].lower().split(", ")
        if skill_name in skills:
            candidates_match.append(candidate)

    return candidates_match[:limit]




