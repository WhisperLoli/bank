from scrapy import cmdline

if __name__ == "__main__":
    cmdline.execute("scrapy crawl bankinfo -s LOG_FILE=all.log -o bank.csv".split(" "))