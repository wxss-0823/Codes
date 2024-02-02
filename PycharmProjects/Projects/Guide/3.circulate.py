sites = ['Google', 'Wiki', 'Weibo', 'Runb', 'Baid']
for site in sites:
    if len(site) != 4:
        continue
    print(f"Hello {site}")

    if site == 'Runb':
        break
print("Done")
