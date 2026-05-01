def build_sections(index, total_pages):
    sections = []
    
    for i in range(len(index)):
        name, start = index[i]
        
        if i < len(index) - 1:
            end = index[i+1][1] - 1
        else:
            end = total_pages
        
        sections.append((name, start, end))  # 0-based
    
    return sections