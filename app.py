from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Nécessite que index.html soit dans un sous-dossier /templates/
    return render_template('index.html')

@app.route('/get_solar_data')
def get_solar_data():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    # Appel API PVGIS (On utilise PVcalc)
    url = f"https://re.jrc.ec.europa.eu/api/v5_2/PVcalc?lat={lat}&lon={lon}&peakpower=1&loss=0&outputformat=json"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            # Correction des clés : l'API utilise 'H(i)_m' (mois) et 'H(i)_d' (jour)
            monthly_data = [month['H(i)_m'] for month in data['outputs']['monthly']['fixed']]
            yearly_avg = data['outputs']['totals']['fixed']['H(i)_d'] 
            
            return jsonify({'monthly': monthly_data, 'daily_avg': yearly_avg})
        else:
            return jsonify({'error': f'Erreur API PVGIS (Code: {response.status_code}). Zone possiblement non couverte.'}), response.status_code
            
    except Exception as e:
        print(f"Erreur backend : {e}")
        return jsonify({'error': 'Erreur interne du serveur Python'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)