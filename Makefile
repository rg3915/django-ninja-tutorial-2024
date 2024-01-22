indenter:
    find backend -name "*.html" | xargs djhtml -t 2 -i

ruff:
    ruff check --fix --show-fixes .
    ruff format --exclude migrations .

lint: indenter ruff
