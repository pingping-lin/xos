from view_common import *

class DashboardUserSiteView(View):
    def get(self, request, **kwargs):
        return HttpResponse(json.dumps(getDashboardContext(request.user, tableFormat=True)), mimetype='application/javascript')
