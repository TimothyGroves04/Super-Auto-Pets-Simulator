import logging
from flask import Flask, render_template, request
from sap_simulator import Pet, simulate_battle

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        logger.debug("Received POST request with form data: %s", request.form)
        team1 = []
        team2 = []

        def get_int_field(name: str) -> int:
            value = request.form.get(name)
            if value is None or value == "":
                raise ValueError(f"Missing field: {name}")
            return int(value)

        try:
            for i in range(1, 6):
                a1 = get_int_field(f'team1_attack_{i}')
                h1 = get_int_field(f'team1_health_{i}')
                logger.debug("Team1 Pet %d: attack=%d health=%d", i, a1, h1)
                team1.append(Pet(a1, h1))
                a2 = get_int_field(f'team2_attack_{i}')
                h2 = get_int_field(f'team2_health_{i}')
                logger.debug("Team2 Pet %d: attack=%d health=%d", i, a2, h2)
                team2.append(Pet(a2, h2))
        except ValueError as e:
            logger.exception("Invalid or missing form data: %s", e)
            return render_template('index.html', error=str(e)), 400

        logger.debug("Constructed teams: team1=%s team2=%s", team1, team2)
        outcome, log = simulate_battle(team1, team2)
        logger.info("Battle outcome: %s", outcome)
        return render_template('battle.html', log=log, outcome=outcome)
    logger.debug("GET request for index page")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
