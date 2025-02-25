"""
env.pyは、Alembicの設定ファイルです。

"""
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from app.database import Base
from app import models

# これはAlembicのConfigオブジェクトで、
# 使用中の.iniファイル内の値にアクセスするためのものです。
config = context.config

# Pythonのロギング設定ファイルを解釈します。
# この行は基本的にロガーを設定します。
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ここにモデルのMetaDataオブジェクトを追加します
# 'autogenerate'サポートのために
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# env.pyのニーズに応じて定義された他の値は、
# 取得できます：
# my_important_option = config.get_main_option("my_important_option")
# ... など。

def run_migrations_offline() -> None:
    """'オフライン'モードでマイグレーションを実行します。

    これはコンテキストをURLだけで構成し、
    エンジンを使用しませんが、エンジンも許容されます。
    エンジンの作成をスキップすることで、
    DBAPIが利用可能である必要すらありません。

    ここでcontext.execute()を呼び出すと、
    指定された文字列がスクリプト出力に出力されます。

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """'オンライン'モードでマイグレーションを実行します。

    このシナリオでは、エンジンを作成し、
    コンテキストと接続を関連付ける必要があります。

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


"""
Alembicは、オフラインモードとオンラインモードの両方で実行できます。
オフラインモードでは、URLだけが必要です。
オンラインモードでは、エンジンを作成し、コンテキストと接続を関連付ける必要があります。
"""
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()