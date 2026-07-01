class SimulationAgent:

    def run_scenario(self, scenario):

        alerts = []

        if scenario == "flood":
            alerts.append("Water Agent: Flood warning.")
            alerts.append("Healthcare Agent: Disease risk.")
            alerts.append("Education Agent: Schools closed.")

        elif scenario == "drought":
            alerts.append("Agriculture Agent: Drought detected.")
            alerts.append("Water Agent: Irrigation shortage.")

        elif scenario == "disease":
            alerts.append("Healthcare Agent: Disease outbreak.")
            alerts.append("Education Agent: Attendance decreasing.")

        elif scenario == "education":
            alerts.append("Education Agent: Dropout risk increasing.")

        return alerts