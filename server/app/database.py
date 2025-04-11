from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings
import os
import logging
from dotenv import load_dotenv

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 加载环境变量
load_dotenv()


# 数据库配置类
class DatabaseSettings(BaseSettings):
    MYSQL_USER: str = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", "root")
    MYSQL_SERVER: str = os.getenv("MYSQL_SERVER", "localhost")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT", "3306")
    MYSQL_DB: str = os.getenv("MYSQL_DB", "videoroomdb")
    
    @property
    def DATABASE_URL(self) -> str:
        # 添加字符集和排序规则参数到连接URL
        conn_str = f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_SERVER}:{self.MYSQL_PORT}/{self.MYSQL_DB}?charset=utf8mb4"
        logger.info(f"数据库连接URL: {conn_str}")
        return conn_str


# 初始化数据库设置
try:
    db_settings = DatabaseSettings()
    logger.info("数据库设置已初始化")
except Exception as e:
    logger.error(f"初始化数据库设置时出错: {e}")
    raise

# 创建数据库引擎
try:
    engine = create_engine(
        db_settings.DATABASE_URL,
        pool_pre_ping=True,  # 检查连接是否有效
        pool_recycle=3600,   # 连接回收时间（适用于MySQL）
        connect_args={
            "charset": "utf8mb4"
        }
    )
    logger.info("数据库引擎已创建")
except Exception as e:
    logger.error(f"创建数据库引擎时出错: {e}")
    raise

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建Base类，用于创建数据库模型类
Base = declarative_base()


# 依赖函数，用于获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
