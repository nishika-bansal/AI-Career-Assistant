from flask import Flask, render_template, request

app = Flask(__name__)

jobs_data = [
    {"title": "Java Developer", "company": "Infosys", "location": "India"},
    {"title": "Full Stack Developer", "company": "Capgemini", "location": "USA"},
    {"title": ".NET Developer", "company": "JPMorgan", "location": "Remote"},
    {"title": "Python Developer", "company": "Amazon", "location": "USA"},
    {"title": "Backend Java Engineer", "company": "Google", "location": "USA"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword'].lower()

    skill_map = {
        "java": ["java", "backend"],
        "python": ["python", "ai", "data"],
        "full stack": ["full stack", "frontend", "backend"],
        ".net": [".net", "dotnet"]
    }

    keywords = skill_map.get(keyword, [keyword])

    matched = []
    for job in jobs_data:
        for k in keywords:
            if k in job["title"].lower():
                matched.append(job)
                break

    return render_template('index.html', jobs=matched, keyword=keyword)

if __name__ == "__main__":
    app.run(debug=True)