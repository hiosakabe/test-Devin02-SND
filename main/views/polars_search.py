"""
Polarsデータフレームを使用した検索機能のデモビュー
"""
from django.shortcuts import render
import polars as pl

from main.utils.polars_search import (
    search_dataframe,
    search_with_multiple_keywords,
    advanced_search,
    search_numeric_range
)


def load_sample_data():
    """サンプルデータフレームを作成する"""
    return pl.DataFrame({
        'id': range(1, 8),
        'name': ['田中太郎', '佐藤花子', '鈴木一郎', '高橋次郎', '伊藤三郎', '山田四郎', '中村五郎'],
        'department': ['営業部', '開発部', 'マーケティング部', '営業部', '開発部', '人事部', '総務部'],
        'skills': ['Python,SQL', 'JavaScript,React', 'Marketing,SNS', 'Sales,Negotiation', 
                'Python,TypeScript', 'HR,Communication', 'Accounting,Excel'],
        'rating': [4.2, 3.8, 4.5, 3.9, 4.7, 4.1, 3.5],
        'active': [True, True, False, True, True, False, True]
    })


def polars_search_demo(request):
    """Polarsデータフレームを使用した検索機能のデモビュー"""
    # サンプルデータの読み込み
    df = load_sample_data()
    
    # リクエストパラメータの取得
    query = request.GET.get('q', '')
    department = request.GET.get('department', '')
    min_rating = request.GET.get('min_rating', '')
    case_sensitive = request.GET.get('case_sensitive') == 'on'
    match_all = request.GET.get('match_all') == 'on'
    
    # 検索条件の構築
    filters = {}
    if department:
        filters['department'] = department
    
    # 検索の実行
    if query and match_all and ' ' in query:
        # 複数キーワードでAND検索
        keywords = query.split()
        results = search_with_multiple_keywords(df, keywords, case_sensitive=case_sensitive, match_all=True)
    elif query:
        # 単一キーワードまたはOR検索
        if ' ' in query and not match_all:
            keywords = query.split()
            results = search_with_multiple_keywords(df, keywords, case_sensitive=case_sensitive, match_all=False)
        else:
            results = advanced_search(df, query=query, filters=filters, case_sensitive=case_sensitive)
    else:
        # クエリがない場合は全てのデータを返す（フィルタのみ適用）
        results = df
        if filters:
            for col, value in filters.items():
                if col in results.columns:
                    results = results.filter(results[col] == value)
    
    # 評価でのフィルタリング
    if min_rating:
        try:
            min_rating = float(min_rating)
            results = search_numeric_range(results, 'rating', min_value=min_rating)
        except ValueError:
            pass
    
    # Polarsデータフレームを辞書のリストに変換
    results_list = results.to_dicts()
    
    # 部署のリストを取得
    departments = df['department'].unique().to_list()
    
    return render(request, 'main/polars_search_demo.html', {
        'query': query,
        'department': department,
        'min_rating': min_rating,
        'case_sensitive': case_sensitive,
        'match_all': match_all,
        'results': results_list,
        'departments': departments
    })
