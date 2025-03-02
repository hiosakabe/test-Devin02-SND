#!/bin/bash

# uvを使用したDjangoプロジェクトのデモスクリプト
# このスクリプトはuvの基本的な使い方を示します

# 色の設定
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}===== uvを使用したDjangoプロジェクト管理デモ =====${NC}"

# 1. uvがインストールされているか確認
if ! command -v uv &> /dev/null; then
    echo "uvをインストールしています..."
    pip install uv
else
    echo "uvは既にインストールされています"
fi

# 2. 仮想環境の作成（デモのため）
echo -e "\n${GREEN}仮想環境を作成しています...${NC}"
echo "コマンド: uv venv .uvenv_demo"
# 実際には実行しません
# uv venv .uvenv_demo

# 3. 仮想環境の有効化（デモのため）
echo -e "\n${GREEN}仮想環境を有効化します...${NC}"
echo "コマンド: source .uvenv_demo/bin/activate"
# 実際には実行しません
# source .uvenv_demo/bin/activate

# 4. 依存関係のインストール（デモのため）
echo -e "\n${GREEN}pyproject.tomlから依存関係をインストールします...${NC}"
echo "コマンド: uv pip install -e ."
# 実際には実行しません
# uv pip install -e .

# 5. 新しいパッケージの追加（デモのため）
echo -e "\n${GREEN}新しいパッケージを追加します...${NC}"
echo "コマンド: uv pip install django-debug-toolbar"
# 実際には実行しません
# uv pip install django-debug-toolbar

echo -e "\n${GREEN}pyproject.tomlを更新します...${NC}"
echo 'dependencies = [
    "django>=5.0.0",
    "django-debug-toolbar>=4.0.0",
]'

# 6. 依存関係の更新（デモのため）
echo -e "\n${GREEN}依存関係を同期します...${NC}"
echo "コマンド: uv pip sync"
# 実際には実行しません
# uv pip sync

# 7. 依存関係のエクスポート（デモのため）
echo -e "\n${GREEN}依存関係をrequirements.txtにエクスポートします...${NC}"
echo "コマンド: uv pip export > requirements.txt"
# 実際には実行しません
# uv pip export > requirements.txt

# 8. Djangoコマンドの実行（デモのため）
echo -e "\n${GREEN}Djangoコマンドを実行します...${NC}"
echo "コマンド: python manage.py runserver"
echo "コマンド: python manage.py migrate"
echo "コマンド: python manage.py createsuperuser"

echo -e "\n${BLUE}===== デモ終了 =====${NC}"
echo "詳細はREADME.mdとuv_django_guide.pyを参照してください。"
