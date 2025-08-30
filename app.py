from flask import Flask, render_template, request
from sap_simulator import Pet, simulate_battle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        team1 = []
        team2 = []
        for i in range(1, 6):
            a1 = int(request.form[f'team1_attack_{i}'])
            h1 = int(request.form[f'team1_health_{i}'])
            team1.append(Pet(a1, h1))
            a2 = int(request.form[f'team2_attack_{i}'])
            h2 = int(request.form[f'team2_health_{i}'])
            team2.append(Pet(a2, h2))
        outcome, log = simulate_battle(team1, team2)
        return render_template('battle.html', log=log, outcome=outcome)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
