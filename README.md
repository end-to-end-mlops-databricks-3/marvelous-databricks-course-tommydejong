<h1 align="center">
Marvelous MLOps End-to-end MLOps with Databricks course

## Dataset
The "Football Players Data" dataset (from [Kaggle](https://www.kaggle.com/datasets/maso0dahmed/football-players-data/data)) offers detailed information on approximately 17,000 FIFA football players, meticulously scraped from SoFIFA.com.

It encompasses a wide array of player-specific data points, including but not limited to player names, nationalities, clubs, player ratings, potential, positions, ages, and various skill attributes. This dataset is ideal for football enthusiasts, data analysts, and researchers seeking to conduct in-depth analysis, statistical studies, or machine learning projects related to football players' performance, characteristics, and career progressions.

This dataset is ideal for data analysis, predictive modeling, and machine learning projects. It can be used for:

- Player performance analysis and comparison.
- Market value assessment and wage prediction.
- Team composition and strategy planning.
- Machine learning models to predict future player potential and career trajectories.

## Practical information
- Weekly lectures on Wednesdays 16:00-18:00 CET.
- Code for the lecture is shared before the lecture.
- Presentation and lecture materials are shared right after the lecture.
- Video of the lecture is uploaded within 24 hours after the lecture.

- Every week we set up a deliverable, and you implement it with your own dataset.
- To submit the deliverable, create a feature branch in that repository, and a PR to main branch. The code can be merged after we review & approve & CI pipeline runs successfully.
- The deliverables can be submitted with a delay (for example, lecture 1 & 2 together), but we expect you to finish all assignments for the course before the 15th of June.


## Set up your environment
In this course, we use Databricks 15.4 LTS runtime, which uses Python 3.11.
In our examples, we use UV. Check out the documentation on how to install it: https://docs.astral.sh/uv/getting-started/installation/

Install task: https://taskfile.dev/installation/

Update .env file with the following:
```
GIT_TOKEN=<your github PAT>
```

To create a new environment and create a lockfile, run:
```
task sync-dev
source .venv/bin/activate
```

Or, alternatively:
```
export GIT_TOKEN=<your github PAT>
uv venv -p 3.11 .venv
source .venv/bin/activate
uv sync --extra dev
```



