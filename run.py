import nonebot,sys,logging
import config_dev,config_test,config_prod
from os import path

if __name__ == '__main__':
    # logging.basicConfig(level=logging.NOTSET)
    try:
        DEPLOYMENT_ENV = sys.argv[1]

        if DEPLOYMENT_ENV == 'dev':
            # 开发环境
            logging.info(f'部署成功！当前环境:{DEPLOYMENT_ENV}')
            nonebot.init(config_dev)
        elif DEPLOYMENT_ENV == 'test':
            # 测试环境
            logging.info(f'部署成功！当前环境:{DEPLOYMENT_ENV}')
            nonebot.init(config_test)
        elif DEPLOYMENT_ENV == 'prod':
            # 生产环境
            logging.info(f'部署成功！当前环境:{DEPLOYMENT_ENV}')
            nonebot.init(config_prod)
        else:
            logging.warning('参数错误！请输入正确的运行参数:\ndev:开发环境\nprod:生产环境\ntest:测试环境')
            sys.exit(1)

        nonebot.load_plugins(
            path.join(path.dirname(__file__), 'awesome', 'plugins'),
            'awesome.plugins'
        )
        nonebot.run()
    except Exception as e:
        logging.error(e)
        logging.error('获取参数失败！请输入运行参数:\ndev:开发环境\nprod:生产环境\ntest:测试环境')