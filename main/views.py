from django.shortcuts import render

def home(request):
    context = {
        'title': 'Devinの使い方',
        'features': [
            {
                'title': 'コード開発支援',
                'description': 'Devinはコードの作成、バグ修正、リファクタリングなどの開発タスクを支援します。'
            },
            {
                'title': 'プロジェクト理解',
                'description': 'コードベースを理解し、適切な修正や機能追加を提案します。'
            },
            {
                'title': 'PRの作成',
                'description': 'コード変更のPull Requestを自動的に作成します。'
            }
        ],
        'usage_tips': [
            '具体的なタスクを明確に説明する',
            '必要なコンテキストを提供する',
            '大きなタスクは小さく分割する',
            'フィードバックを提供して改善を促す'
        ],
        'examples': [
            {
                'title': 'バグ修正依頼',
                'description': '@Devin このバグを修正してください: ログイン時にユーザー名が正しく表示されません。エラーログには「TypeError: Cannot read property of undefined」と表示されています。',
            },
            {
                'title': '新機能の実装',
                'description': '@Devin ユーザープロフィールページに「最近の活動」セクションを追加してください。最新の10件のアクションを表示する必要があります。',
            }
        ]
    }
    return render(request, 'main/home.html', context)
