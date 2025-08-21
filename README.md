# Streaming Feature AB Test Pet Project

# В этом проекте анализируется поведение пользователей стриминговой платформы и оценивается результаты A/B-тестов.
# В нём можно увидеть такие данные, как синтетические события пользователей, группы A/B, конверсии, DAU, а также визуализацию этих метрик в дашборде и примеры SQL-запросов для анализа.


## Установка
```bash
git clone <repo_url>
cd streaming-feature-abtest
pip install -r requirements.txt
```

## Запуск дашборда
```bash
cd dashboard
streamlit run app.py
```

## Airflow DAG
- Скопируйте `airflow_dags/` в ваш Airflow home
- DAG `dau_dag` считает DAU и сохраняет в `data/dau.csv`

## SQL
- `sql/ab_analysis.sql` содержит примеры запросов для A/B-теста
