from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    rules = pd.read_csv('association_rules.csv')  # Save your analysis result to CSV
    return render_template('index.html', rules=rules)

if __name__ == '__main__':
    app.run(debug=True)

