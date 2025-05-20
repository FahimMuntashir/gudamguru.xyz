# Gudam Guru Website

This is the official website for Gudam Guru, an inventory and stock management Android application.

## Features

- Modern, responsive design
- Contact form for potential users
- Secure download system with code verification
- Email notifications for new requests

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/yourusername/gudamguru.xyz.git
cd gudamguru.xyz
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables:

- Copy `.env.example` to `.env`
- Update the following variables in `.env`:
  - `EMAIL_USER`: Your Gmail address
  - `EMAIL_PASSWORD`: Your Gmail app-specific password
  - `ADMIN_EMAIL`: Email address to receive notifications

5. Place your APK file:

- Create a directory: `static/apk/`
- Place your `gudamguru.apk` file in this directory

6. Run the development server:

```bash
python app.py
```

## Deployment

1. Set up a production server (e.g., DigitalOcean, AWS, etc.)
2. Install required system packages:

```bash
sudo apt-get update
sudo apt-get install python3-venv nginx
```

3. Configure Nginx as a reverse proxy
4. Set up SSL certificates using Let's Encrypt
5. Use Gunicorn as the WSGI server:

```bash
pip install gunicorn
gunicorn -w 4 -b 127.0.0.1:8000 app:app
```

## Security Notes

- Keep your `.env` file secure and never commit it to version control
- Use strong passwords and enable 2FA for your email account
- Regularly update dependencies to patch security vulnerabilities
- Monitor server logs for suspicious activity

## License

This project is proprietary and confidential. Unauthorized copying, distribution, or use is strictly prohibited.
