python -m venv .venv
pip install -r requirements.txt

.venv\Scripts\activate

cd visualization
streamlit run app.py

data taken from:
- TransportAPI