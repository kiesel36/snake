import screeninfo 
for monitor in screeninfo.get_monitors():
    print(monitor.height)
    print(monitor.width)
    print(monitor.is_primary)