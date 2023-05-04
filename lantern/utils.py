from IPython import get_ipython


class LanternException(Exception):
    pass


def in_ipynb():
    if ip := get_ipython():
        cfg = ip.config
        return bool(cfg.get('IPKernelApp', False))
    return False


def download(df):
    from IPython.display import HTML
    import base64
    csv = base64.b64encode(df.reset_index().to_csv().encode()).decode()
    html = '<a download="download.csv" href="data:text/csv;base64,{payload}" target="_blank">Download</a>'.format(payload=csv)
    return HTML(html)
