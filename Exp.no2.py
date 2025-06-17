import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

data = {
    'Sender': ['alice@example.com', 'bob@example.com', 'alice@example.com', 'carol@example.com', 'bob@example.com'],
    'Subject': ['Meeting Tomorrow', 'Urgent Update', 'Lunch?', 'Weekly Report', 'Deadline Reminder'],
    'Date': ['2024-06-01', '2024-06-01', '2024-06-02', '2024-06-03', '2024-06-03'],
    'Content': [
        'Hi, are we meeting tomorrow at 10 AM?',
        'Please update the document ASAP.',
        'Wanna grab lunch today?',
        'Attached is the weekly report for review.',
        'Reminder: Submit the project by EOD.'
    ]
}

df = pd.DataFrame(data)


df['Date'] = pd.to_datetime(df['Date'])

df['ContentLength'] = df['Content'].apply(len)

print("\n📊 Basic Info:")
print(df.info())

print("\n📝 First Few Rows:")
print(df.head())


plt.figure(figsize=(6, 4))
sns.countplot(x='Sender', data=df, palette='Set2')
plt.title('Emails Sent by Each Sender')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
df.groupby('Sender')['ContentLength'].mean().plot(kind='bar', color='orange')
plt.title('Average Email Length per Sender')
plt.ylabel('Characters')
plt.tight_layout()
plt.show()


plt.figure(figsize=(6, 4))
df.groupby('Date').size().plot(marker='o', color='purple')
plt.title('Email Volume Over Time')
plt.ylabel('Number of Emails')
plt.tight_layout()
plt.show()

text = ' '.join(df['Subject'])
wordcloud = WordCloud(background_color='white').generate(text)
plt.figure(figsize=(6, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Subject Word Cloud')
plt.tight_layout()
plt.show()
