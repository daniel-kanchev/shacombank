BOT_NAME = 'shacombank'
SPIDER_MODULES = ['shacombank.spiders']
NEWSPIDER_MODULE = 'shacombank.spiders'
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'WARNING'
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
ITEM_PIPELINES = {
   'shacombank.pipelines.DatabasePipeline': 300,
}
