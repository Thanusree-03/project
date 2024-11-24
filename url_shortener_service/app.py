from flask import Flask, request, redirect, render_template, url_for, flash
from database import db, init_db
from models import URL

app = Flask(__name__)
app.secret_key = 'your_secret_key'
init_db(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form.get('original_url')
        if not original_url:
            flash("Please enter a valid URL!")
            return redirect(url_for('index'))

        # Check if the URL already exists in the database
        existing_url = URL.query.filter_by(original_url=original_url).first()
        if existing_url:
            short_url = existing_url.short_url
        else:
            # Create a new short URL
            short_url = URL.generate_short_url()
            new_url = URL(original_url=original_url, short_url=short_url)
            db.session.add(new_url)
            db.session.commit()

        flash(f"Short URL created: {request.host_url}{short_url}")
        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_original(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)

if __name__ == '__main__':
    app.run(debug=True)
