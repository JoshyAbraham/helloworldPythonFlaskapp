from app import app
from app.security import require_appkey

@app.route('/') 
@require_appkey
def index():
    return 'hello world'