from agents.simulation_agent import SimulationAgent

sim = SimulationAgent()

alerts = sim.run_scenario("flood")

for alert in alerts:
    print(alert)