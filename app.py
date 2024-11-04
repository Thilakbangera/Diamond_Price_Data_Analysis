from flask import Flask, render_template, request
import pandas as pd
import seaborn as sns

app = Flask(__name__)

# Load the diamonds dataset from seaborn
diamonds_df = sns.load_dataset('diamonds')

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        weight = request.form.get('weight', type=float)
        if weight is not None:
            # Filter the dataframe for the given weight
            results = diamonds_df[diamonds_df['carat'] == weight]
    
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
