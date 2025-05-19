import re

def organize_stories(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all story numbers
    story_numbers = re.findall(r'story-number">(\d+)', content)
    story_numbers = sorted(set(story_numbers), key=int)  # Remove duplicates and sort
    
    # Create a mapping of old numbers to new sequential numbers
    number_mapping = {old: str(new + 1) for new, old in enumerate(story_numbers)}
    
    # Replace all story numbers
    for old_number, new_number in number_mapping.items():
        content = content.replace(f'story-number">{old_number}', f'story-number">{new_number}')
    
    # Update the story comments
    for old_number, new_number in number_mapping.items():
        content = content.replace(f'<!-- قصة {old_number} -->', f'<!-- قصة {new_number} -->')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Run the function
organize_stories('fi-rehab-alquran.html')
