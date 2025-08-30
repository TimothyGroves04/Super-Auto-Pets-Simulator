# Super Auto Pets Simulator

This project provides a basic battle simulator for the game **Super Auto Pets**.

## Command Line Usage

Run the simulator in demo mode:

```bash
python sap_simulator.py --demo
```

Run interactively and enter pet stats at the prompt:

```bash
python sap_simulator.py
```

## Web Interface

A simple Flask web application is included for a nicer user interface. Install
dependencies and start the server with:

```bash
pip install -r requirements.txt
python app.py
```

Open your browser at [http://localhost:5000](http://localhost:5000) to enter the
attack and health for each team's pets. After submitting the form you can step
through each stage of the battle by clicking **Next Step**.
