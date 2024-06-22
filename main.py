from apiData.loadData import load_json
from textProcessing.analyzeData import summarize_data, count_unique_values, filter_data, group_data
from visualization.visualizeData import plot_count

def main():
    # Carregar dados
    file_path = './crawler-script/data/test.json'
    df = load_json(file_path)
    
    # Exibir as primeiras linhas do DataFrame
    print(df.head())
    
    # Análise de dados
    summary = summarize_data(df)
    print("Resumo Estatístico:\n", summary)
    
    column_name = 'cleaned_tweet'  # Usando o tweet limpo
    unique_values = count_unique_values(df, column_name)
    print(f"Contagem de valores únicos em '{column_name}':\n", unique_values)
    
    # Filtragem e agrupamento
    column_to_filter = 'name'  # Nome da coluna para filtro, ajuste conforme necessário
    filter_value = 'Mário Flávio'  # Valor específico para filtro, ajuste conforme necessário
    
    if column_to_filter in df.columns:  
        filtered_df = filter_data(df, column_to_filter, filter_value)
        print(f"Dados filtrados onde '{column_to_filter}' == '{filter_value}':\n", filtered_df)
    
        grouped_df = group_data(df, column_to_filter)
        print(f"Dados agrupados por '{column_to_filter}':\n", grouped_df)
    
    # Agrupamento por username, texto publicado e número de RTs
    grouped_general = df.groupby(['screen_name', 'tweet_text', 'retweet_count']).size().reset_index(name='count')
    print(f"Agrupamento generalista por username, texto e RTs:\n", grouped_general)
    
    # Visualização dos dados
    plot_count(df, column_name)

    # Exibir análises adicionais
    print(f"Tokens dos tweets:\n", df['tokens'].head())
    print(f"Análise de sentimentos dos tweets:\n", df[['cleaned_tweet', 'sentiment_score']].head())

if __name__ == "__main__":
    main()
