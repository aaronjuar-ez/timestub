## timestub
a basic cli tool written in python to help with time sheet prediction
---
my first project since returning to coding after 4 years away from it 
---
todo:
- [x] create a cli using textual
- [x] finish basic calculations for money earned
- [ ] add tax calculations
    - [ ] add tax presets
    - [ ] add custom tax rates
---
## install
```bash
pipx install git+https://github.com/aaronjuar-ez/timestub.git
timestub
```
no pipx? `pip install git+https://github.com/aaronjuar-ez/timestub.git`

## run from source
```bash
git clone https://github.com/aaronjuar-ez/timestub.git
cd timestub
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python tui.py
```
