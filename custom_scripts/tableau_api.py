import tableauserverclient as TSC


class Tableau:
    def __init__(self, username: str, password: str, site: str = 'gradeup', server_url: str = 'https://eu-west-1a.online.tableau.com', api_version: str = '2.6') -> None:
        self.tableau_auth = TSC.TableauAuth(username, password, site_id=site)
        self.server = TSC.Server(server_url)
        self.server.version = api_version

    def export_view_as_image(self, image_file_path: str, view_id: str, filters: list = []):
        image_req_option = TSC.ImageRequestOptions(imageresolution=TSC.ImageRequestOptions.Resolution.High)
        for filter in filters:
            image_req_option.vf(filter.get('filter_name'), filter.get('filter_value'))
        with self.server.auth.sign_in(self.tableau_auth):
            for view_item in TSC.Pager(self.server.views):
                if view_item.id == view_id:
                    self.server.views.populate_image(view_item, req_options=image_req_option)
                    with open(image_file_path, 'wb') as f:
                        f.write(view_item.image)
                    break
        self.server.auth.sign_out()
