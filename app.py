from flask import Flask, jsonify, request

class IrrigationSystem:
    def calculate_demand(self, moisture, temperature):
        """Calculates water requirements based on humidity and temperature."""
        if moisture < 0 or moisture > 100:
            raise ValueError("Moisture must be between 0 and 100")
            
        # Use more water when the temperature is high and humidity is low
        if moisture < 30:
            return "High" if temperature > 86 else "Medium"
        elif moisture < 60:
            return "Low"
        return "None"

app = Flask(__name__)
system = IrrigationSystem()

@app.route('/status')
def status():
    # Simulate sample values (typically from sensors)
    m = float(request.args.get('m', 50))
    t = float(request.args.get('t', 20))
    
    demand = system.calculate_demand(m, t)
    return jsonify({
        "project": "UrbanPlow",
        "sensor_data": {"moisture": m, "temp": t},
        "irrigation_demand": demand
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
