"""
uvを使用したDjangoプロジェクト管理ガイド

このスクリプトはuvパッケージマネージャーを使用してDjangoプロジェクトを
管理する方法を示すためのものです。実行するものではなく、参考資料です。
"""

# 1. uvのインストール
# pip install uv

# 2. 仮想環境の作成
# uv venv .uvenv

# 3. 仮想環境の有効化
# source .uvenv/bin/activate  # Linux/Mac
# .uvenv\Scripts\activate     # Windows

# 4. 依存関係のインストール
# uv pip install -e .         # pyproject.tomlから依存関係をインストール

# 5. 新しいパッケージの追加
# uv pip install django-debug-toolbar
# その後、pyproject.tomlを手動で更新

# 6. 依存関係の更新
# uv pip sync                 # pyproject.tomlに基づいて依存関係を同期

# 7. 依存関係のエクスポート
# uv pip export > requirements.txt  # 現在の依存関係をrequirements.txtにエクスポート

# 8. Djangoコマンドの実行
# python manage.py runserver
# python manage.py migrate
# python manage.py createsuperuser

# 9. 開発環境と本番環境の分離
# pyproject.tomlで[project.optional-dependencies]セクションを使用
# uv pip install -e ".[dev]"  # 開発用依存関係をインストール
