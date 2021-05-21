
from flask import render_template, request, flash

from rainfall import app
from rainfall.models import Model
import numpy as np

# Route
@app.route("/", methods=['GET', 'POST'])
def index():
	data_kemarin = None
	prediksi = None
	if len(request.form) > 0:
		try:
			data_kemarin = int(request.form["kemarin"])
			data_input = np.array([data_kemarin])
			data_input = data_input.reshape((1, Model.look_back, Model.features))
			prediksi = Model.models.predict(data_input, verbose=0)
		except:
			flash("Input Error or Cant get Models")

	return render_template('home.html', kemarin=data_kemarin, hasil=prediksi)


