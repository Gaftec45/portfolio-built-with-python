from flask import Flask, render_template

app = Flask(__name__)

services = [
    {"name": "YouTube", "desc": "Elevate your brand with compelling video content tailored for YouTube audiences."},
    {"name": "TikTok", "desc": "Capture attention fast with trendy, scroll-stopping TikTok videos."},
    {"name": "Animation", "desc": "Bring ideas to life with smooth and engaging animations."},
    {"name": "2D Animation", "desc": "Classic, eye-catching 2D animations to tell your story beautifully."},
    {"name": "3D Animation", "desc": "Immersive 3D animations that captivate and inspire."},
    {"name": "Character Design", "desc": "Unique characters crafted to fit your vision and style."},
    {"name": "Character Modeling", "desc": "Detailed 3D character models ready for games and films."},
    {"name": "Mobile App", "desc": "Innovative and user-friendly mobile app development."},
    {"name": "Game Development", "desc": "From concept to launch, creative game experiences that engage."},
    {"name": "Pumpfun Development", "desc": "Smart, efficient solutions built for the Pumpfun ecosystem."},
    {"name": "Wallet App Development", "desc": "Secure and intuitive crypto wallet applications."},
    {"name": "Web Automation", "desc": "Automate repetitive web tasks to boost productivity and scale."},
    {"name": "Crypto Development", "desc": "Blockchain-powered solutions, from tokens to full ecosystems."},
    {"name": "Software Development", "desc": "Robust and scalable custom software solutions tailored to your needs."},
]

portfolio_images = [
    "images/WhatsApp Image 2025-05-19 at 14.48.52_91b1a12a.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.05_1eb12c9c.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.07_b0ce0761.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.06_c21027ed.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.07_72f316d7.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.07_b0ce0761.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.41_2cd1c85a.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.41_40cb612d.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.41_2cd1c85a.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.49_4fc5f635.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.48_d6fbc76e.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.48_c0247515.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.48_48194b80.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.48_79192a7a.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.48_5b704510.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.06_af5e854f.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.46_c6de2587.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.45_ab13ec6d.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.44_3eac9d59.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.43_1ac80ffe.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.43_63f21385.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.44_b3e696ee.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.45_6d8a1eae.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.45_a058f1b4.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.45_c892e956.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.46_3333b2b0.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.46_bd57c007.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.47_da87dc6a.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.47_ca35e0e3.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.47_0879f6f2.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.46_bd981dd9.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.44_d5873954.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.44_313378e4.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.42_f7f723a2.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.42_61442704.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.42_7075104a.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.41_247f9498.jpg",
    "images/WhatsApp Image 2025-05-19 at 14.49.42_e169f52c.jpg",
    ]

# @app.route('/portfolio')
# def portfolio():
#     return render_template('portfolio.html', images=portfolio_images)

@app.route('/')
def home():
    return render_template('index.html', services=services, images=portfolio_images)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
