# AI agents development test 

## Résumé
Ce projet met en œuvre un **workflow multi-agents** avec le framework [CrewAI](https://docs.crewai.com/) pour rechercher et rapporter les dernières avancées en intelligence artificielle.  
Il définit un *crew* (équipe) d’agents capables de **rechercher**, **analyser** et **rédiger un rapport** sur un sujet donné (par défaut : « AI LLMs »).

---

## 1. Contexte et objectifs
- **Agents autonomes** : chaque agent a un rôle précis (recherche, analyse, gestion).  
- **Tâches configurables** : les actions sont décrites dans des fichiers YAML (`config/agents.yaml`, `config/tasks.yaml`).  
- **Orchestration hiérarchique** : un *manager agent* coordonne la recherche et la production du rapport.  
- **Entrées dynamiques** : le sujet et l’année courante sont passés comme paramètres d’exécution.

---

## 2. Composants principaux
- **Researcher Agent** : collecte et analyse les informations liées à l’IA.  
- **Reporting Analyst Agent** : synthétise les résultats et rédige un rapport structuré.  
- **Manager Agent** : supervise le flux de travail et délègue les tâches.  
- **Research Task** : définit la mission de recherche.  
- **Reporting Task** : génère un fichier `report.md` à partir des résultats.  
- **Crew** : assemble agents et tâches en un processus hiérarchique.

---

## 3. Installation

### Prérequis
- **Python ≥ 3.10**  
- Accès à une API ou un modèle compatible CrewAI (définir les variables `MODEL` et éventuellement `API_BASE`).

### Étapes
```bash
# Cloner le dépôt
git clone https://github.com/Maxcym/AI_Agents_test

# Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate   # sous Windows : .venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

#Lancer le crew
crewai run

