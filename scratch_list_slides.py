with open('doodle_by_district_presentation.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 'id="slide-' in line:
            print(f'{i}: {line.strip()}')
