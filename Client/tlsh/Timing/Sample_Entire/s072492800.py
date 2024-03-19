def cross_section_area(data):
    area = 0;
    sections = [];
    stack = [];
    for i in range(len(data)):
        if data[i] == '\\':
            stack.append(i);
        elif data[i] == '/' and len(stack) > 0:
            j = stack.pop();
            section_area = i - j;
            area += section_area;
            while len(sections) > 0 and sections[-1][0] > j:
                section_area += sections[-1][1];
                sections.pop();
            sections.append([j, section_area]);
    print(area);
    print(len(sections), *[n[1] for n in sections]);

cross_section_area(input());
