# from datetime import datetime
#
# from apscheduler.schedulers.background import BackgroundScheduler
#
# from api.info import InfoLoader
# import env
# from files.service import FileStorage
# from api.seller import WbLoader
# from api.market import MarketLoader
#
# scheduler = BackgroundScheduler(timezone=env.TZ)
#
#
# if env.SCHEDULER_WORKS:
#     scheduler.add_job(
#         WbLoader.hourly_load,
#         trigger="interval",
#         hours=1,
#         next_run_time=datetime.now(),
#         id="wb_data_hourly_update",
#     )
#     scheduler.add_job(
#         WbLoader.daily_load,
#         trigger="cron",
#         hour="0",
#         minute="0",
#         id="wb_data_daily_update",
#     )
#     scheduler.add_job(
#         MarketLoader.hourly_load,
#         trigger="interval",
#         hours=1,
#         next_run_time=datetime.now(),
#         id="market_data_hourly_update",
#     )
#     scheduler.add_job(
#         MarketLoader.daily_load,
#         trigger="cron",
#         hour="0",
#         minute="0",
#         id="market_data_daily_update",
#     )
#     scheduler.add_job(
#         FileStorage.clean,
#         trigger="cron",
#         hour="0",
#         minute="0",
#         id="media_cleanup",
#     )
