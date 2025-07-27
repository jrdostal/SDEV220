def what_time_is_it(when):
    import time
    from datetime import datetime, timedelta
    import random
    current = time.localtime()
    before = datetime.now()
    fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
    print(time.strftime(fmt, current))
    time.sleep(random.randrange(0,1))
    current = time.localtime()
    after  = datetime.now()
    fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
    print(time.strftime(fmt, current))
    wait = str(after - before)
    print(f"waited: {wait} seconds")
