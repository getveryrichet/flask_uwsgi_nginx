FROM richet/ubuntu-richet:0.0

ENV MD "/home/richet/TradingSystem"
ADD . /home/richet/TradingSystem
# RUN cp /home/richet/TradingSystem/sys/uwsgi/flask_trading.service /etc/systemd/system/flask_trading.service
# RUN systemctl start flask_trading
# RUN systemctl enable flask_trading


WORKDIR "/home/richet/TradingSystem"
CMD ["/virtualenv/trading_envs/bin/uwsgi","flask_trading.ini"]
# CMD ["systemctl","start","flask_trading"]