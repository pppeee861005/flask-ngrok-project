from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """首頁路由，回傳歡迎頁面"""
    return '''
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask 示範應用程式</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            .container {
                text-align: center;
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            }
            h1 {
                color: #333;
                margin: 0 0 20px 0;
            }
            p {
                color: #666;
                font-size: 16px;
                line-height: 1.6;
            }
            .info {
                background: #f0f0f0;
                padding: 15px;
                border-radius: 5px;
                margin-top: 20px;
                text-align: left;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>歡迎使用 Flask 示範應用程式</h1>
            <p>這是一個簡單的 Flask 網頁應用程式示範。</p>
            <div class="info">
                <p><strong>功能：</strong></p>
                <ul>
                    <li>提供基本的 HTML 歡迎頁面</li>
                    <li>支援錯誤處理</li>
                    <li>可透過 ngrok 分享到公網</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    '''


@app.errorhandler(404)
def not_found(error):
    """404 錯誤處理器"""
    return '''
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>頁面不存在</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            }
            .container {
                text-align: center;
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            }
            h1 {
                color: #f5576c;
                margin: 0 0 20px 0;
                font-size: 48px;
            }
            p {
                color: #666;
                font-size: 16px;
                line-height: 1.6;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: background 0.3s;
            }
            a:hover {
                background: #764ba2;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>404</h1>
            <p>抱歉，您訪問的頁面不存在。</p>
            <a href="/">返回首頁</a>
        </div>
    </body>
    </html>
    ''', 404


@app.errorhandler(500)
def internal_error(error):
    """500 錯誤處理器"""
    return '''
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>伺服器錯誤</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            }
            .container {
                text-align: center;
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            }
            h1 {
                color: #fa709a;
                margin: 0 0 20px 0;
                font-size: 48px;
            }
            p {
                color: #666;
                font-size: 16px;
                line-height: 1.6;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: background 0.3s;
            }
            a:hover {
                background: #764ba2;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>500</h1>
            <p>抱歉，伺服器發生錯誤。請稍後再試。</p>
            <a href="/">返回首頁</a>
        </div>
    </body>
    </html>
    ''', 500


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
