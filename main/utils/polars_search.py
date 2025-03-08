"""
Polarsデータフレームを使用した検索機能のユーティリティモジュール
"""
import polars as pl


def search_dataframe(df, query, columns=None, case_sensitive=False):
    """
    指定されたクエリでデータフレームを検索する
    
    Parameters:
    -----------
    df : pl.DataFrame
        検索対象のデータフレーム
    query : str
        検索クエリ
    columns : list, optional
        検索対象の列名のリスト。Noneの場合は全ての文字列列を検索
    case_sensitive : bool, optional
        大文字小文字を区別するかどうか。デフォルトはFalse（区別しない）
        
    Returns:
    --------
    pl.DataFrame
        検索結果を含むデータフレーム
    """
    if not query:
        return df
    
    # 検索対象の列を決定
    if columns is None:
        # 文字列型の列のみを対象にする
        columns = [col for col in df.columns if df[col].dtype == pl.Utf8]
    
    # 検索条件を構築
    conditions = []
    for col in columns:
        if case_sensitive:
            conditions.append(df[col].str.contains(query))
        else:
            conditions.append(df[col].str.to_lowercase().str.contains(query.lower()))
    
    # OR条件で結合
    if not conditions:
        return df
        
    combined_condition = conditions[0]
    for condition in conditions[1:]:
        combined_condition = combined_condition | condition
    
    # 条件に合致する行を返す
    return df.filter(combined_condition)


def search_with_multiple_keywords(df, keywords, columns=None, case_sensitive=False, match_all=False):
    """
    複数のキーワードでデータフレームを検索する
    
    Parameters:
    -----------
    df : pl.DataFrame
        検索対象のデータフレーム
    keywords : list
        検索キーワードのリスト
    columns : list, optional
        検索対象の列名のリスト。Noneの場合は全ての文字列列を検索
    case_sensitive : bool, optional
        大文字小文字を区別するかどうか。デフォルトはFalse（区別しない）
    match_all : bool, optional
        全てのキーワードに一致する行のみを返すかどうか。
        Trueの場合はAND条件、Falseの場合はOR条件で検索する。
        
    Returns:
    --------
    pl.DataFrame
        検索結果を含むデータフレーム
    """
    if not keywords:
        return df
    
    if match_all:
        # AND条件（全てのキーワードに一致する行を返す）
        result = df
        for keyword in keywords:
            result = search_dataframe(result, keyword, columns, case_sensitive)
        return result
    else:
        # OR条件（いずれかのキーワードに一致する行を返す）
        results = [search_dataframe(df, keyword, columns, case_sensitive) for keyword in keywords]
        if not results:
            return df
        
        # 結果を結合して重複を削除
        combined_result = results[0]
        for result in results[1:]:
            combined_result = pl.concat([combined_result, result])
        
        return combined_result.unique()


def advanced_search(df, query=None, filters=None, columns=None, case_sensitive=False):
    """
    検索とフィルタリングを組み合わせた高度な検索
    
    Parameters:
    -----------
    df : pl.DataFrame
        検索対象のデータフレーム
    query : str, optional
        検索クエリ
    filters : dict, optional
        列名と値のペアを含むディクショナリ。完全一致でフィルタリングする。
        例: {'department': '営業部', 'active': True}
    columns : list, optional
        検索対象の列名のリスト
    case_sensitive : bool, optional
        大文字小文字を区別するかどうか
        
    Returns:
    --------
    pl.DataFrame
        検索結果を含むデータフレーム
    """
    result = df
    
    # テキスト検索を実行
    if query:
        result = search_dataframe(result, query, columns, case_sensitive)
    
    # フィルタリングを適用
    if filters:
        for col, value in filters.items():
            if col in result.columns:
                result = result.filter(result[col] == value)
    
    return result


def search_numeric_range(df, column, min_value=None, max_value=None):
    """
    数値列の範囲検索
    
    Parameters:
    -----------
    df : pl.DataFrame
        検索対象のデータフレーム
    column : str
        検索対象の数値列名
    min_value : float, optional
        最小値（この値以上）
    max_value : float, optional
        最大値（この値以下）
        
    Returns:
    --------
    pl.DataFrame
        検索結果を含むデータフレーム
    """
    result = df
    
    if column not in df.columns:
        return result
    
    if min_value is not None:
        result = result.filter(result[column] >= min_value)
    
    if max_value is not None:
        result = result.filter(result[column] <= max_value)
    
    return result
