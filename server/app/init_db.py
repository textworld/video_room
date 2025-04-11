from .database import Base, engine, SessionLocal
from .models.database_models import RoomDB
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def ensure_charset_and_collation():
    """确保数据库已配置正确的字符集和排序规则"""
    db = SessionLocal()
    try:
        logger.info("检查数据库字符集和排序规则...")
        # 执行查询以检查数据库字符集和排序规则
        result = db.execute("SHOW VARIABLES WHERE Variable_name LIKE 'character\\_set\\_%' OR Variable_name LIKE 'collation%'")
        
        for row in result:
            logger.info(f"{row[0]}: {row[1]}")
            
        # 设置数据库默认字符集和排序规则（如果需要）
        db.execute("ALTER DATABASE videoroomdb CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci")
        logger.info("数据库字符集和排序规则已设置为 utf8mb4/utf8mb4_general_ci")
    except Exception as e:
        logger.error(f"检查或设置字符集和排序规则时出错: {e}")
    finally:
        db.close()

def create_tables():
    """创建所有数据库表"""
    logger.info("正在创建数据库表...")
    Base.metadata.create_all(bind=engine)
    logger.info("数据库表创建完成")

def initialize_data():
    """初始化一些示例数据"""
    db = SessionLocal()
    try:
        # 检查数据库中是否已有房间数据
        existing_rooms = db.query(RoomDB).count()
        if existing_rooms == 0:
            logger.info("初始化示例房间数据...")
            # 创建示例房间
            sample_rooms = [
                RoomDB(
                    room_id="LIVE123XYZ01",
                    name="编程直播间",
                    status="living",
                    description="分享编程技巧和项目开发",
                    is_public=True
                ),
                RoomDB(
                    room_id="OFF456ABC02",
                    name="游戏直播间",
                    status="offline",
                    description="各种游戏直播",
                    is_public=True
                ),
                RoomDB(
                    room_id="LIVE789DEF03",
                    name="音乐制作直播",
                    status="living",
                    description="音乐制作教程和演示",
                    is_public=True
                )
            ]
            
            db.add_all(sample_rooms)
            db.commit()
            logger.info(f"已创建{len(sample_rooms)}个示例房间")
        else:
            logger.info(f"数据库中已有{existing_rooms}个房间，跳过初始化")
    except Exception as e:
        db.rollback()
        logger.error(f"初始化数据时出错: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    # 确保数据库字符集和排序规则正确
    ensure_charset_and_collation()
    # 创建表
    create_tables()
    # 初始化数据
    initialize_data()
    logger.info("数据库初始化完成") 