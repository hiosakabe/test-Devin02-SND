# Devin使用方法説明アプリ

このプロジェクトはDevinの使い方を日本語で説明するためのDjangoウェブアプリケーションです。

## セットアップ方法 (uvを使用)

```bash
# uvをインストール
pip install uv

# 仮想環境を作成
uv venv .uvenv

# 仮想環境を有効化
source .uvenv/bin/activate

# 依存関係をインストール
uv pip install -e .

# 開発用依存関係をインストール (オプション)
uv pip install -e ".[dev]"

# または、セットアップスクリプトを使用
./uvenv.sh

# マイグレーションを実行
python manage.py migrate

# サーバーを起動
python manage.py runserver
```

## 依存関係の管理

新しい依存関係を追加するには、`pyproject.toml`ファイルを編集し、以下のコマンドを実行します：

```bash
# プロジェクト依存関係を更新
uv pip install -e .

# または開発用依存関係を更新
uv pip install -e ".[dev]"
```

## 機能

- Devinの基本的な使い方の説明
- 効果的な指示の出し方
- 使用例
