找煤宝网站运行

运行环境: linux, python, 根据实际需要而安装的数据库
默认已经安装好python, 项目根目录为zhaomeibao/

1. 安装依赖包.
   在 zhaomeibao/ 目录下(与manage.py同目录), 命令行执行:
   $ pip install -r requirement.txt


2. 相关配置.
    1) 配置连接的数据库.

       编辑项目根目录下 app/database.py #5行原为:
       engine = create_engine('sqlite:///product.db', convert_unicode=True, echo=False)

       将'sqlite:///product.db'修改为所需连接的数据库, 如: 
       -- 连接postgresql为'postgresql://scott:tiger@localhost:5432/mydatabase'.
       -- 连接mysql为'mysql://scott:tiger@localhost/foo'.

       详情请参考sqlalchemy文档的create_engine模块: http://docs.sqlalchemy.org/en/latest/core/engines.html#sqlalchemy.create_engine


    2) 编辑报错邮件.

       该设置用于在部署环境下应用发生错误时通知到相应的邮箱(可不设置). 

       编辑项目根目录下 config.py 中的ProductConfig类. 
       -- 其中MAIL_USERNAME和MAIL_PASSWORD是用于登陆的邮箱的账号和密码. 
       -- MAIL_SERVER为用于登陆的邮箱的smtp服务器的网址, 如: smtp.163.com. 
       -- MAIL_PORT是该smtp服务器的服务端口, 如: smtp.163.com的服务端口为25.
       -- ADMINS是一个字符串列表, 列表中的每个字符串是用于接收错误邮件的邮箱, 如: ['1234@qq.com', 'example@163.com']

    3) 设置运行环境.
 
       默认情况下, 该应用运行在产品环境下, 若需要debug等而要在生产环境下运行程序, 可将manage.py的#11行 app = create_app('product')中的'product'换成'development'.


3. 初始化数据库.
   在项目根目录下(与manage.py同目录), 命令行执行:
   $ python manage.py init_db


4. 创建管理员账号.
   在项目根目录下(与manage.py同目录), 命令行执行:
   $ python manage.py create_superuser
   之后命令行提示输入用户名和两次密码.

5. 运行程序.
   该步骤一般用于生产环境(debug)下运行
   在项目根目录下(与manage.py同目录), 命令行执行:
   $ python manage.py runserver
   若命令行提示:
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   即可在浏览器输入 127.0.0.1:5000 或 localhost:5000访问.
   
   1) 修改服务端口.
      在命令行下输入: 
      $ python manage.py runserver --port [port] 
      将[port]替换为所需的端口即可

   2) 令Web服务器监听公共网络接口上的连接,允许同网中的其他计算机连接服务器.
      在命令行输入:
      $ python manage.py runserver --host 0.0.0.0

   3) 1)和2)可同时设置.


6. 部署.
   部署方案: ubuntu + nginx + gunicorn
   
   1) 安装nginx, 命令行执行:
      $ sudo apt-get install nginx-full

   2) 配置nginx.
   
      -- 备份/etc/nginx/sites-enabled/default, 命令行执行: 
         $ sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default-bak
      
      -- 修改 /etc/nginx/sites-available/default 里面的内容. 假定项目目录的绝对路径为 ~/zhaomeibao/.
          server {
              listen 80;
              server_name 127.0.0.1;
              root ~/zhaomeibao/;
              access_log ~/zhaomeibao/logs/access.log;
              error_log ~/zhaomeibao/logs/error.log;
              location / {
                try_files $uri @gunicorn_proxy;
              }
              location @gunicorn_proxy {
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $http_host;
                proxy_redirect off;
                proxy_pass http://127.0.0.1:8000;
            }
          }

      -- 重启nginx, 命令行下执行: $ sudo service nginx restart


   3) 安装gunicorn, 命令行执行:
      $ pip install gunicorn
    
      -- 运行gunicorn, 命令行执行(与manage.py在同一目录):
         $ gunicorn -w 4 manage:app
         若要后台运行:
         $ nohup gunicorn -w 4 manage:app &

