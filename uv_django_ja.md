# uvを使用したDjangoプロジェクト管理ガイド

## uvとは？

uvは高速なPythonパッケージマネージャーで、以下の特徴があります：

- pipよりも高速なパッケージインストール
- 依存関係の解決が優れている
- 仮想環境の管理が簡単
- 依存関係のロックファイルのサポート

## インストール方法

```bash
pip install uv
```

## 基本的な使い方

### 仮想環境の作成

```bash
# 仮想環境を作成
uv venv .uvenv

# 仮想環境を有効化（Linux/Mac）
source .uvenv/bin/activate

# 仮想環境を有効化（Windows）
.uvenv\Scripts\activate
```

### パッケージのインストール

```bash
# pyproject.tomlから依存関係をインストール
uv pip install -e .

# 開発用依存関係をインストール
uv pip install -e ".[dev]"

# 特定のパッケージをインストール
uv pip install django-debug-toolbar
```

### 依存関係の管理

```bash
# 依存関係を同期（pyproject.tomlに基づいて）
uv pip sync

# 現在の依存関係をrequirements.txtにエクスポート
uv pip export > requirements.txt

# requirements.txtから依存関係をインストール
uv pip install -r requirements.txt
```

## Djangoプロジェクトでの使用例

### プロジェクトのセットアップ

```bash
# uvをインストール
pip install uv

# 仮想環境を作成
uv venv .uvenv

# 仮想環境を有効化
source .uvenv/bin/activate

# Djangoをインストール
uv pip install django

# Djangoプロジェクトを作成
django-admin startproject myproject .

# アプリケーションを作成
python manage.py startapp myapp

# マイグレーションを実行
python manage.py migrate

# サーバーを起動
python manage.py runserver
```

### pyproject.tomlの例

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "myproject"
version = "0.1.0"
description = "My Django Project"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
dependencies = [
    "django>=5.0.0",
    "django-debug-toolbar>=4.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "isort>=5.0.0",
]
```

### uv.tomlの例

```toml
[tool]
# uv specific configuration
python-version = "3.12"
resolution-mode = "highest"

[venv]
# Virtual environment configuration
path = ".uvenv"
prompt = "myproject"
```

## 開発ワークフロー

1. プロジェクトのクローン
2. uvをインストール: `pip install uv`
3. 仮想環境を作成: `uv venv .uvenv`
4. 仮想環境を有効化: `source .uvenv/bin/activate`
5. 依存関係をインストール: `uv pip install -e .`
6. 開発作業を行う
7. 新しい依存関係を追加する場合は、pyproject.tomlを更新し、`uv pip install -e .`を実行
8. 変更をコミット

## pipとの違い

| 機能 | uv | pip |
|------|----|----|
| インストール速度 | 高速 | 標準 |
| 依存関係の解決 | 優れている | 基本的 |
| 仮想環境の管理 | 組み込み | 別ツール（venv）が必要 |
| ロックファイル | サポート | 未サポート |
| エコシステム統合 | 発展中 | 広く統合済み |

## 参考リンク

- [uv公式ドキュメント](https://github.com/astral-sh/uv)
- [uvとpipの比較](https://astral.sh/blog/uv)
