import re

with open('index.html.bak', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the comment issue from sed
text = text.replace('//                                            <button onClick={() => setMenuVertical', '                                            <button onClick={() => setMenuVertical')
text = text.replace('//                                             style={Object.assign({}, (modeMenuPos.y', '                                             style={Object.assign({}, (modeMenuPos.y')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
