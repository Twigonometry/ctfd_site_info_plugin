from flask import request, send_from_directory
from CTFd.plugins import register_plugin_assets_directory
def load(app):
    base_path='plugins/ctfd_site_info_plugin/assets/'
    register_plugin_assets_directory(app,base_path=base_path)
    @app.route('/robots.txt')
    def send_robots():
        return send_from_directory(base_path.strip("/"),request.path[1:])