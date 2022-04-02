import pandas as pd
from pathlib import Path 
from datetime import datetime
from Pubmed_Tools import get_title, get_first_author, get_date, get_doi

i = 1
index = ['Title','First Author','Date and Citation','doi']
articles = pd.DataFrame(index=index)

topic = str(input('Please enter a name or topic for your search:'))
topic = topic.replace(' ','_')

while True:
    option1 = int(input('Enter 1 to add a new article, 0 to stop and record results, or 00 to stop and quit without saving:'))
    if option1 == 1:
        link = str(input('Journal Article NCBI link:'))
        heading = get_title(link)
        first_author = get_first_author(link)
        date = get_date(link)
        doi = get_doi(link)
        article_info = [heading, first_author, date, doi]
        articles[f'Article_{i}'] = article_info
        i += 1
    elif option1 == 0:
        #Date and topic change the file name with every search so that file is not overwritten.
        now = datetime.now()
        date = now.strftime('%B_%d_%Y_%H-%M-%S')
        filepath = Path(f'Search_Results\{topic}_search_results_{date}.csv')  
        filepath.parent.mkdir(parents=True, exist_ok=True)  
        articles.to_csv(filepath)
        print('All done! A CSV file containing your results has been saved.')
        break
    else:
        print('Your results were not saved. Goodbye.')
        break

