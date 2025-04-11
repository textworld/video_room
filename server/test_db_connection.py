"""
测试数据库连接的简单脚本
"""
import logging
import sys

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

try:
    # 导入数据库模块
    from app.database import engine, Base, db_settings, SessionLocal
    
    # 导入模型确保它们已注册
    from app.models.database_models import RoomDB
    
    logger.info("成功导入数据库模块和模型")
    logger.info(f"数据库URL: {db_settings.DATABASE_URL}")
    
    # 测试连接
    try:
        logger.info("测试数据库连接...")
        with engine.connect() as connection:
            logger.info("成功连接到数据库！")
            
            # 检查字符集和排序规则
            logger.info("检查数据库字符集和排序规则...")
            result = connection.execute("SHOW VARIABLES WHERE Variable_name IN ('character_set_database', 'collation_database')")
            for row in result:
                logger.info(f"{row[0]}: {row[1]}")
                
            # 检查表的字符集和排序规则
            logger.info("检查表字符集和排序规则...")
            
            # 先创建表，确保表存在
            Base.metadata.create_all(bind=engine)
            
            # 检查rooms表的字符集和排序规则
            result = connection.execute("SHOW TABLE STATUS LIKE 'rooms'")
            for row in result:
                logger.info(f"表名: {row[0]}, 排序规则: {row[14]}")
                
            # 检查每列的字符集和排序规则
            result = connection.execute("SHOW FULL COLUMNS FROM rooms")
            for row in result:
                if row[1].startswith('varchar') or row[1].startswith('text'):
                    logger.info(f"列名: {row[0]}, 类型: {row[1]}, 排序规则: {row[2]}")
        
    except Exception as e:
        logger.error(f"连接数据库或检查字符集时出错: {e}")
        raise
except Exception as e:
    logger.error(f"导入模块时出错: {e}")
    raise

if __name__ == "__main__":
    logger.info("数据库连接和字符集测试完成") 