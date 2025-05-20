from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
import secrets

load_dotenv()

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('EMAIL_USER')

mail = Mail(app)

# Store download codes (in production, use a database)
download_codes = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        store_name = request.form.get('store_name')
        
        # Generate a unique code
        code = secrets.token_hex(4).upper()
        download_codes[code] = {
            'name': name,
            'email': email,
            'phone': phone,
            'store_name': store_name,
            'used': False
        }
        
        # Send email to admin
        msg = Message(
            'New Gudam Guru Download Request',
            recipients=[os.getenv('ADMIN_EMAIL')]
        )
        msg.body = f"""
        New download request received:
        
        Name: {name}
        Email: {email}
        Phone: {phone}
        Store Name: {store_name}
        Download Code: {code}
        """
        mail.send(msg)
        
        flash('Thank you for your interest! We will contact you shortly with your download code.', 'success')
        return redirect(url_for('home'))
    
    return render_template('contact.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        code = request.form.get('code').upper()
        
        if code in download_codes and not download_codes[code]['used']:
            download_codes[code]['used'] = True
            return render_template('download.html', code=code)
        else:
            flash('Invalid or already used code. Please try again.', 'error')
    
    return render_template('download.html')

if __name__ == '__main__':
    app.run(debug=True) 