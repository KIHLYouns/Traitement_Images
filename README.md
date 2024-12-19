# 1. Vérifier la version de Python
python3 --version
# Assurez-vous que la sortie est Python 3.12.x

# 2. Créer un environnement virtuel nommé 'venv'
python3 -m venv venv

# 3. Activer l'environnement virtuel
source venv/bin/activate

# 4. Mettre à jour pip dans l'environnement virtuel
pip install --upgrade pip

# 5. Installer les modules requis
pip install numpy matplotlib Pillow tqdm

# 6. Exécuter votre script Python
python3 q1.py