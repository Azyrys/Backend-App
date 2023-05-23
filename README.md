# Backend-App - Projekt WSEI
## Requirements:
-Python3.9
-Node.js

## To run application execute
### To run backend
```
edit .\backend\build_env\pyenv.cfg
home = "your-python3.9-location"
python .\backend\app.py
```

### To run frontend
```
cd .\frontend
npm install
npm run serve
```

### To run backend tests
```
python -m unittest .\backend\unit_tests\tests.py
```

### To run frontend tests
```
npx jest .\unit_tests\"TestName".spec.js
```
