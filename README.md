# Flask + ngrok 示範應用程式

## 專案用途

本專案是一個 Flask 示範網頁應用程式，展示如何快速建立一個簡單的網頁服務，並透過 ngrok 將本地開發中的應用程式暴露到公網。這對於以下場景非常有用：

- 快速驗證開發環境是否正常運作
- 與他人分享開發中的作品，無需部署到伺服器
- 測試 Webhook 或第三方服務的回調功能
- 展示本地開發的應用程式給遠端使用者

## 系統需求

- Python 3.8 或更高版本
- pip（Python 套件管理工具）
- ngrok 帳戶（免費）
- Windows 作業系統（本專案使用 .bat 腳本）

## 快速開始

### 1. 啟動虛擬環境

虛擬環境用於隔離專案的 Python 相依套件，避免與系統全域套件衝突。

**首次設定：**

```bash
# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境（Windows）
.\venv\Scripts\activate

# 啟動虛擬環境（macOS/Linux）
source venv/bin/activate
```

**驗證虛擬環境已啟動：**

命令列提示符應該顯示 `(venv)` 前綴，例如：
```
(venv) C:\project>
```

**安裝相依套件：**

```bash
pip install -r requirements.txt
```

### 2. 運行 Flask 應用程式

#### 方式一：使用啟動腳本（推薦）

```bash
# Windows
.\run_flask.bat
```

#### 方式二：手動運行

```bash
# 確保虛擬環境已啟動
.\venv\Scripts\activate

# 運行應用程式
python src/app.py
```

**預期輸出：**

```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

**驗證應用程式：**

在瀏覽器中訪問 `http://localhost:5000`，應該看到歡迎頁面。

### 3. 安裝和設定 ngrok

#### 步驟 1：建立 ngrok 帳戶

1. 訪問 [ngrok 官方網站](https://ngrok.com)
2. 點擊「Sign Up」建立免費帳戶
3. 使用電子郵件或 GitHub 帳戶註冊

#### 步驟 2：下載 ngrok

1. 登入 ngrok 帳戶
2. 進入 [下載頁面](https://ngrok.com/download)
3. 下載 Windows 版本（.zip 檔案）
4. 解壓縮到方便的位置，例如 `C:\ngrok`

#### 步驟 3：設定 authtoken

1. 登入 ngrok 帳戶後，進入 [Auth 頁面](https://dashboard.ngrok.com/auth)
2. 複製您的 authtoken（一長串字符）
3. 在命令列中執行以下命令設定 authtoken：

```bash
# Windows
ngrok config add-authtoken <YOUR_AUTHTOKEN>

# 或使用以下命令
ngrok authtoken <YOUR_AUTHTOKEN>
```

**驗證設定：**

```bash
ngrok --version
```

應該顯示 ngrok 的版本號。

### 4. 透過 ngrok 分享應用程式

#### 步驟 1：啟動 Flask 應用程式

在第一個終端機視窗中運行：

```bash
.\run_flask.bat
```

或手動運行：

```bash
.\venv\Scripts\activate
python src/app.py
```

#### 步驟 2：啟動 ngrok 隧道

在第二個終端機視窗中運行：

```bash
# 方式一：使用啟動腳本
.\run_ngrok.bat

# 方式二：手動運行
ngrok http 5000
```

**預期輸出：**

```
ngrok                                       (Ctrl+C to quit)

Session Status                online
Account                       <your-email>
Version                        3.x.x
Region                         us (United States)
Forwarding                     https://xxxx-xx-xxx-xxx.ngrok.io -> http://localhost:5000
Forwarding                     http://xxxx-xx-xxx-xxx.ngrok.io -> http://localhost:5000

Connections                    ttl     opn     rt1     rt5     p50     p95
                               0       0       0.00    0.00    0.00    0.00
```

#### 步驟 3：分享公開 URL

複製 ngrok 輸出中的 `Forwarding` URL（例如 `https://xxxx-xx-xxx-xxx.ngrok.io`），與他人分享。

**重要提示：**

- 每次重新啟動 ngrok，URL 會改變（除非使用付費帳戶）
- 免費帳戶的隧道在 2 小時後會自動關閉
- 確保 Flask 應用程式持續運行，否則外部使用者無法存取

## 專案結構

```
project/
├── venv/                    # Python 虛擬環境（自動建立）
├── src/
│   ├── app.py              # Flask 應用程式主檔案
│   └── test_app.py         # 單元測試檔案
├── requirements.txt         # Python 相依套件清單
├── run_flask.bat           # Flask 啟動腳本
├── run_ngrok.bat           # ngrok 啟動腳本
├── README.md               # 本檔案
└── flask-ngrok-architecture.html  # 架構圖
```

## 常見問題

### Q1：如何停止 Flask 應用程式？

在運行 Flask 的終端機中按 `Ctrl+C`。

### Q2：如何停止 ngrok 隧道？

在運行 ngrok 的終端機中按 `Ctrl+C`。

### Q3：ngrok URL 為什麼每次都不同？

免費帳戶每次啟動 ngrok 時會獲得新的 URL。如果需要固定 URL，可升級到付費帳戶。

### Q4：外部使用者無法存取我的應用程式？

請檢查以下項目：

1. Flask 應用程式是否正在運行（檢查第一個終端機）
2. ngrok 隧道是否已建立（檢查第二個終端機）
3. 防火牆是否阻止了連線
4. 是否使用了正確的 ngrok URL

### Q5：如何在 macOS 或 Linux 上運行此專案？

本專案的啟動腳本使用 Windows 批次檔案（.bat）。在 macOS 或 Linux 上，請手動運行命令：

```bash
# 啟動虛擬環境
source venv/bin/activate

# 運行 Flask
python src/app.py

# 在另一個終端機運行 ngrok
ngrok http 5000
```

### Q6：如何更新相依套件？

```bash
# 啟動虛擬環境
.\venv\Scripts\activate

# 升級 pip
python -m pip install --upgrade pip

# 安裝新的相依套件
pip install -r requirements.txt
```

## 故障排除

### 問題：「python: 找不到命令」

**解決方案：**

- 確認 Python 已正確安裝
- 在 Windows 上，使用 `python --version` 檢查版本
- 如果仍無法找到，請重新安裝 Python 並勾選「Add Python to PATH」選項

### 問題：「虛擬環境無法啟動」

**解決方案：**

```bash
# 刪除舊的虛擬環境
rmdir /s /q venv

# 重新建立虛擬環境
python -m venv venv

# 啟動虛擬環境
.\venv\Scripts\activate
```

### 問題：「埠 5000 已被佔用」

**解決方案：**

```bash
# 查找佔用埠 5000 的程式（Windows）
netstat -ano | findstr :5000

# 終止該程式（將 PID 替換為實際的程式 ID）
taskkill /PID <PID> /F

# 或修改 Flask 應用程式使用不同的埠
# 編輯 src/app.py，將 app.run(port=5000) 改為 app.run(port=5001)
```

### 問題：「ngrok authtoken 無效」

**解決方案：**

1. 重新登入 ngrok 帳戶
2. 複製新的 authtoken
3. 重新執行設定命令：`ngrok authtoken <YOUR_NEW_AUTHTOKEN>`

## 開發工作流程

### 修改應用程式

1. 編輯 `src/app.py`
2. 由於啟用了除錯模式，Flask 會自動重新載入
3. 在瀏覽器中重新整理頁面查看變更

### 運行測試

```bash
# 啟動虛擬環境
.\venv\Scripts\activate

# 運行所有測試
pytest src/test_app.py

# 運行特定測試
pytest src/test_app.py::test_index_returns_html

# 顯示詳細輸出
pytest src/test_app.py -v
```

## 相關資源

- [Flask 官方文件](https://flask.palletsprojects.com/)
- [ngrok 官方文件](https://ngrok.com/docs)
- [Python 虛擬環境指南](https://docs.python.org/3/tutorial/venv.html)
- [pytest 文件](https://docs.pytest.org/)

## 授權

本專案為示範用途，可自由使用和修改。

## 支援

如有任何問題或建議，請檢查上述「常見問題」和「故障排除」部分。
