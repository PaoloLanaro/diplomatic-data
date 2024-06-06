import pandas as pd
import datetime 

def escape_single_quotes(value):
    if isinstance(value, str):
        return value.replace("'", "''")
    return value

def csv_to_sql(csv_file):
        """
        Description: Takes a provided csv file and turns into SQL???? 

        Args:
            csv_file (str): file path to the intended csv file
        
        Returns:
            n/a
        """
        df = pd.read_csv(csv_file)
# ,url,Safety Index
        # Create the INSERT INTO statements
        insert_statements = []
        for _, row in df.iterrows():
            publication_date = row['date']
            sentiment = row['sentiment']
            article_link = row['url']
            source_country = row ['source_country']
            content = escape_single_quotes(row['text'])
            saftey_index = (row['Safety Index'])
            queried_country = escape_single_quotes(row['queried_country'])
            insert_stmt = f"INSERT INTO article (content, publication_date, article_link, saftey_index, source_country, sentiment, queried_country) VALUES ('{content}', '{publication_date}', '{article_link}', {saftey_index}, '{source_country}', {sentiment}, '{queried_country}');"
            insert_statements.append(insert_stmt)


# Write the INSERT INTO statements to a .sql file
        print(f"insert statements object={insert_statements}")
        with open('database/insert_article.sql', 'w') as f:
            f.write('\n'.join(insert_statements))

        print("SQL file created successfully.")

csv_to_sql('api/backend/assets/Data News Sources.csv')


        

